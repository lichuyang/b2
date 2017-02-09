import sqlite3
import jieba
con = sqlite3.connect('BaiduYun.db')
cur = con.cursor()
select_sql = "select title, id from CMS_fileinfo"
cur.execute(select_sql)
date_set = cur.fetchall()
for row in date_set:
    #seg_list = jieba.cut(row[0], cut_all=False)
    seg_list = jieba.analyse.extract_tags(row[0], topK=3)
    for s in seg_list:
        insert_sql = "insert into CMS_taginfo(tagName, fileId) values(?,?)"
        cur.execute(insert_sql,(s, row[1]))
con.commit()
con.close()