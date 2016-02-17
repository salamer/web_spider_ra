import requests
from bs4 import BeautifulSoup
import urllib
import re

class zhihu_collection_spider():

    def __init__(self):
        self.count=1

    def find_all_pic(self):
#        url_list=["http://www.zhihu.com/question/24463692"+str(i) for i in range(22,25)]
        url_list=["https://www.zhihu.com/question/31005941"]
        self.get_img(url_list)


    def get_img(self,url_list):

        for url in url_list:
            content=requests.get(url)

#            soup=BeautifulSoup(content.text,"html")

#            img_list=soup.find_all("img")

            reg=r'htt.*?\.jpg'

            im_gre=re.compile(reg)

            img_list=re.findall(im_gre,content.text)

#            attr=[]

#            for img in img_list:
#                src=str(img["src"])
#                src=src.replace("200x112","r")
#                attr.append(src)
            attr=[]

            for img in img_list:
                if len(img)<100 and "_b" not in img and "200x112" not in img and img not in attr:
                    attr.append(img)


            self.download_pic(attr)

    def download_pic(self,attr):
        path="/Users/aljun/spider/better_than_star/"

        for url in attr:
            self.count=self.count+1
            r=requests.get(url,stream=True)
            with open(path+str(self.count)+".jpg", 'wb') as fd:
                for chunk in r.iter_content():
                    fd.write(chunk)
            print "pic: %s " % url

if __name__=="__main__":
    crawler=zhihu_collection_spider()
    crawler.find_all_pic()
