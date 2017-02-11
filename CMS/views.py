#coding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import FileInfo, UserInfo, SearchInfo
from django.db import connection
import time
import json
import jieba.analyse
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    cursor = connection.cursor()
    cursor.execute("select f.addTime,u.userName , f.title, f.userId, f.id , f.hits from cms_fileinfo as f left join cms_userinfo as u on f.userId = u.id order by f.addTime desc limit 10")
    file_infos = dictfetchall(cursor)
    cursor.execute(
        "select u.userName , u.userAvaUrl, f.title, f.userId, f.id , f.hits from cms_fileinfo as f ,cms_userinfo as u where u.id=f.userId order by f.addTime desc limit 10 ")
    random_post = dictfetchall(cursor)
    random_userid = random_post[0].get('userId');
    random_username = random_post[0].get('userName');
    random_useravaurl = random_post[0].get('userAvaUrl');

    cursor.execute("select u.userName , f.title, f.userId, f.id , f.hits from cms_fileinfo as f left join cms_userinfo as u on f.userId = u.id order by f.hits desc limit 10")
    hot_read_post = dictfetchall(cursor)

    cursor.execute(
        "select u.userName , f.title, f.userId, f.id , f.downloads from cms_fileinfo as f left join cms_userinfo as u on f.userId = u.id order by f.downloads desc limit 10")
    hot_download_post = dictfetchall(cursor)

    '''cursor.execute(
        "select  u.userName , u.userAvaUrl,  u.id from cms_userinfo as u order by u.hits desc limit 40 ")
    hot_users = dictfetchall(cursor)
    '''
    hot_search_post = SearchInfo.objects.all().order_by('-searchCount')[0:10]

    return render_to_response('home.html', {'file_infos': file_infos, 'random_post':random_post,
                                            'random_userid':random_userid, 'random_username': random_username, 'random_useravaurl':random_useravaurl,
                                            'hot_read_post':hot_read_post,
                                            'hot_download_post':hot_download_post,
                                            'hot_search_post' : hot_search_post})

def file_info(request, user_id, share_id):
    cursor = connection.cursor()
    cursor.execute(
        "select f.addTime,u.userName, u.userAvaUrl, f.title, f.userId, f.id , f.hits, f.downloads from cms_fileinfo as f left join cms_userinfo as u on f.userId = u.id where f.userId="+str(user_id)+" and f.id="+str(share_id))
    file_detail = dictfetchall(cursor)[0]
    file_info = FileInfo.objects.get(userId=user_id, id=share_id)
    file_info.hits += 1
    file_info.save()

    user_add_time = FileInfo.objects.filter(userId=file_info.userId).order_by('addTime').all().values('addTime')[0]['addTime']

    #seg_list = jieba.cut(file_info.title, cut_all=False)
    #print(", ".join(seg_list))
    tags = jieba.analyse.extract_tags(file_info.title, topK=3)
    tag = jieba.analyse.extract_tags(file_info.title, topK=1)
    if len(tag) > 0:
        related_shares = FileInfo.objects.filter(title__contains=tag[0]).exclude(id=file_detail['id'])[0:10]
    else:
        related_shares = FileInfo.objects.all()[0:10]

    return render_to_response('detail.html', {'file_detail': file_detail,
                                              'user_add_time' :  time.strftime("%Y-%m-%d", time.localtime(float(user_add_time))),
                                              'tags' : tags,
                                              'related_shares' : related_shares})

def search(request, page_num):
    search_text = request.GET['wd']
    if search_text.strip() == '':
        return render_to_response('search.html', {'search_result': None, 'length': 0,
                                                  'search_text': search_text,
                                                  'page_num': 1,
                                                  'total_num': 0})
    search_result = FileInfo.objects.filter(title__contains=search_text).order_by('-addTime')[20*(int(page_num)-1):20*int(page_num)]
    length = FileInfo.objects.filter(title__contains=search_text).count()
    try:
        search_info = SearchInfo.objects.get(searchText=search_text)
        search_info.searchCount += 1
    except SearchInfo.DoesNotExist:
        search_info = SearchInfo.objects.create(searchText=search_text, searchCount=1, searchTime=time.time())
    search_info.save()
    total_num = (length-1) / 20 + 1
    return render_to_response('search.html', {'search_result': search_result, 'length': length,
                                              'search_text' : search_text,
                                              'page_num' : page_num,
                                              'total_num' : total_num})

def user(request, user_id, page_num):
    user_info = UserInfo.objects.get(id=user_id)
    user_info.hits += 1
    user_info.save()

    user_add_time = FileInfo.objects.filter(userId=user_id).order_by('addTime').all().values('addTime')[0]['addTime']

    file_list = FileInfo.objects.filter(userId=user_id).all()[10*(int(page_num)-1):10*int(page_num)]

    total_num = (len(FileInfo.objects.filter(userId=user_id))-1)/10+1
    return render_to_response('user.html', {'user_info': user_info,
                                            'user_add_time' : time.strftime("%Y-%m-%d", time.localtime(float(user_add_time))),
                                            'file_list' : file_list,
                                            'page_num' : page_num,
                                            'total_num' : total_num})

def redirect(request, user_id, share_id):
    file_info = FileInfo.objects.get(id = share_id)
    file_info.downloads += 1
    file_info.save()
    title = file_info.title
    url = 'https://pan.baidu.com/wap/link?uk='+ user_id + '&shareid='+ share_id
    return render_to_response('redirect.html',{'url':url,
                                              'title' : title})

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def apisearch(request, page_num):
    search_text = request.GET['wd']
    search_result = FileInfo.objects.filter(title__contains=search_text).order_by('-addTime')[20*(int(page_num)-1):20*int(page_num)]
    length = FileInfo.objects.filter(title__contains=search_text).count()
    try:
        search_info = SearchInfo.objects.get(searchText=search_text)
        search_info.mSearchCount += 1
    except SearchInfo.DoesNotExist:
        search_info = SearchInfo.objects.create(searchText=search_text, mSearchCount=1, searchTime=time.time())
    search_info.save()
    return_data = {}
    dataA = []
    for i in search_result:
        result_data = {}
        result_data['title'] = i.title
        result_data['id'] = i.id
        result_data['userId'] = i.userId
        dataA.append(result_data)
        return_data = {'count': length, 'index' : page_num, 'data': dataA}
    return HttpResponse(json.dumps(return_data, ensure_ascii=False))

def download(requers):
    return HttpResponseRedirect('http://www.xxx.com/static/quanlisou.apk')