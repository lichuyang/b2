import MySQLdb
import time

db = MySQLdb.connect("localhost","root","4253732","baiduyun" )
cursor = db.cursor()
for i in range(145):
    f=open('/root/www/BaiduYunDjango/CMS/static/sitemaps/sitemap-'+str(i)+'.xml','w')
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset>\n')
    m = i*2000
    n = i*2000 + 2000
    cursor.execute("SELECT * FROM CMS_FILEINFO LIMIT " + str(m) +"," + str(n))
    results = cursor.fetchall()
    for row in results:
        f.write('<url>\n')
        f.write('<loc>http://www.vdashuju.com/file-'+str(row[2])+'-'+str(row[0])+'.html</loc>\n')
        '''timeArray = time.localtime(float(row[3]))
        add_time = time.strftime("%Y-%m-%d", timeArray)
        f.write('<lastmod>'+add_time+'</lastmod>\n')
        f.write('<changefreq>monthly</changefreq>\n')
        f.write('<priority>0.6</priority>\n')
        '''
        f.write('</url>\n')
    f.write('</urlset>\n')
    f.close()
db.close()


