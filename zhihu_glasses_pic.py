import gevent.monkey
#gevent.monkey.patch_all()
import requests
from bs4 import BeautifulSoup
import urllib
import urllib2
import re
import gevent

class zhihu_collection_spider():

    def __init__(self):
        self.count=1

    def find_all_pic(self):
#        url_list=["http://www.zhihu.com/question/24463692"+str(i) for i in range(22,25)]
        url_list=["https://www.zhihu.com/question/30477915"]
        img_list=self.get_img(url_list)
        return img_list


    def get_img(self,url_list):

        for url in url_list:
            content=urllib2.urlopen(url)
            content=content.read()

#            soup=BeautifulSoup(content.text,"html")

#            img_list=soup.find_all("img")

            reg=r'htt.*?\.png'

            im_gre=re.compile(reg)

            img_list=re.findall(im_gre,content)

#            reg=r'htt.*?\.png'



#            png_list

#            attr=[]

#            for img in img_list:
#                src=str(img["src"])
#                src=src.replace("200x112","r")
#                attr.append(src)
            attr=[]

            for img in img_list:
                if len(img)<100 and "_b" not in img and "200x112" not in img and img not in attr and "_s" not in img:
                    attr.append(img)


            return attr

    def download_pic(self,attr):
        path="/Users/aljun/spider/glasses/"

        for url in attr:
            self.count=self.count+1
            r=requests.get(url,stream=True)
            with open(path+str(self.count)+".jpg", 'wb') as fd:
                for chunk in r.iter_content():
                    fd.write(chunk)
            print "pic: %s " % url

    def download_single_pic(self,url,count):
        path="/Users/aljun/spider/glasses/"



        r=requests.get(url,stream=True)
        with open(path+str(count)+".jpg", 'wb') as fd:
            for chunk in r.iter_content():
                fd.write(chunk)
        print "pic: %s " % url


def download_single_pic(url,count):
    path="/Users/aljun/spider/glasses/"
#    r=urllib.urlopen(url)
    path=path+str(count)+'.png'
    urllib.urlretrieve(url,path)
    print "pic: %s " % url

if __name__=="__main__":
    crawler=zhihu_collection_spider()
#    img_list=crawler.find_all_pic()
#    print img_list

    img_list=crawler.find_all_pic()
    threads=[]
    for count in range(len(img_list)):
        threads.append(gevent.spawn(download_single_pic,img_list[count],count))
    gevent.joinall(threads)
