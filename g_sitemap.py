f=open('/usr/local/nginx-1.5.6/html/sitemap.xml','w')
f.write('<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
for i in range(145):
    f.write('<sitemap>\n')
    f.write('<loc>http://www.vdashuju.com/static/sitemaps/sitemap-'+str(i)+'.xml</loc>\n')
    '''timeArray = time.localtime(float(row[3]))
    add_time = time.strftime("%Y-%m-%d", timeArray)
    f.write('<lastmod>'+add_time+'</lastmod>\n')
    f.write('<changefreq>monthly</changefreq>\n')
    f.write('<priority>0.6</priority>\n')
    '''
    f.write('</sitemap>\n')
f.write('</sitemapindex>\n')
f.close()


