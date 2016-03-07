import gevent
from gevent import monkey
monkey.patch_socket()

import requests
import urllib

def fetch(url,name):
    path="/Users/aljun/spider/facejoking/"

    path=path+name+'.jpg'
    urllib.urlretrieve(url,path)
    print "dowmloaded:",url

def get_url(pid):
    return "http://www.facejoking.com/pic/"+pid+".jpg"

if __name__=="__main__":
    headers={
            'Referer': 'http://www.facejoking.com/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/601.4.4 (KHTML, like Gecko) Version/9.0.3 Safari/601.4.4',
            'X-Requested-With': 'XMLHttpRequest'
        }

    r=requests.get("http://www.facejoking.com/api/top/global/0/5",headers=headers)
    data=r.json()
    data=data['data']
    url_list=[]
    for i in range(100):
        url_list.append(get_url(data[i]['pid']))
    greenlets=[]
    for i in range(100):
        greenlets.append(gevent.spawn(fetch,url_list[i],data[i]['name']))
    gevent.joinall(greenlets)
