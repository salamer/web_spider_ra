from scrapy.spiders import Rule,CrawlSpider,Spider
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

from zhihu_girl.items import ZhihuGirlItem

class zhihu_girl_spider(Spider):
    name="zhihu_girl_spider"

    allowed_domains=[]

    start_urls=[
        'http://www.zhihu.com/collection/53719722',
    ]

    user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:43.0) Gecko/20100101 Firefox/43.0"

    headers = {'User-Agent': user_agent,
               'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'zh-cn',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'keep-alive',

    }



#    DOWNLOAD_DELAY = 0.25


    def parse(self,response):


        sel=Selector(response)

        item=ZhihuGirlItem()

        item['image_urls']=sel.xpath("//img[@class='origin_image']/@data-original").extract()

        print item['image_urls']

        yield item
