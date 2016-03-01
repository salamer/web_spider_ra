import re
import urllib
import urllib2
import gevent
from multiprocessing.dummy import Pool

def get_pic(img_url):
    path=img_url.replace("https://","")
    path=path.replace(".zhimg.com/","")
    path="/Users/aljun/spider/collection/"+path
    urllib.urlretrieve(img_url,path)
    print "downloaded: %s" % img_url


def make_greelets(url):
    content=urllib2.urlopen(url)
    content=content.read()

    img_list=[]

    reg=r"htt.*?\.jpg"
    reg=re.compile(reg)
    the_list=re.findall(reg,content)

    for item in the_list:
        if len(item)<100 and "_b" not in item and "200x112" not in item and "_s" not in item:
            img_list.append(item)

    reg=r"htt.*?\.png"
    reg=re.compile(reg)
    the_list=re.findall(reg,content)

    for item in the_list:
        if len(item)<100 and "_b" not in item and "200x112" not in item and "_s" not in item:
            img_list.append(item)

    greelets=[]
    for item in img_list:
        greelets.append(gevent.spawn(get_pic,item))

    gevent.joinall(greelets)
    return "got %s" % url

if __name__=='__main__':
    urls=[]
#    make_greelets("https://www.zhihu.com/collection/38624707")

    for i in range(1,11):
        urls.append("https://www.zhihu.com/collection/38624707?page=%d" % i)
    pool=Pool(processes=4)

    res=pool.map_async(make_greelets,urls)
    pool.close()
    pool.join()
