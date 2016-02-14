from scrapy.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

from douban_kawaii_girl.items import DoubanKawaiiGirlItem

class douban_kawaii_girl_spider(CrawlSpider):
    name="girl_spider"

    allowed_domains=[]

    start_urls=[
        'http://www.douban.com/group/haixiuzu/',
    ]

    user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:43.0) Gecko/20100101 Firefox/43.0"

    headers = {'User-Agent': user_agent,
               'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'zh-cn',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'keep-alive',

    }

    cookies={
        'bid':'oxiFe5WhceE',
        '__utma':"30149280.1513258375.1453554550.1454730320.1455376451.7",
        '__utmz':"30149280.1453554550.1.1.utmcsr=guge.click|utmccn=(referral)|utmcmd=referral|utmcct=/",
        'll':"108288",
        "_pk_id.100001.8cb4":"7df80096ff80cdc0.1453603027.5.1455380465.1454730320.",
        "viewed":"26320485_20382244_26274624_4889838_3794471_10546125_6038371_4866934",
        "gr_user_id":"c7cb7ad3-6969-4662-87ad-b95624878367",
        "ap":"1",
        "_pk_ses.100001.8cb4":"*",
        "__utmb":"30149280.72.10.1455376451",
        "__utmc":"30149280",
    }

    DOWNLOAD_DELAY = 0.25

    rules=(
        Rule(LinkExtractor(allow=(r'http://www.douban.com/group/topic/\d+',)),callback='parse_item',follow=True),
    )

    def parse_item(self,response):


        sel=Selector(response)

        item=DoubanKawaiiGirlItem()

        item['image_urls']=sel.xpath('//div[@class="topic-figure cc"]/img/@src').extract()

        print item['image_urls']

        yield item
