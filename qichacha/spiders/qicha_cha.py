import scrapy
from scrapy.http import Request
from qichacha.items import QichachaItem

class TaobaoSpider(scrapy.Spider):
    name = "taobao"
    allowed_domaines = ["taobao.com"]
    start_urls = ['https://gongzhuxiaowu.taobao.com/search.htm']

    def parse(self, response):
        item = QichachaItem()
        url = response.xpath('//dd[@class="detail"]')
        for ul in url:
            item['name'] = ul.xpath('a[@class="item-name J_TGoldData"]/text()').extract()
            item['price'] = ul.xpath('div[@class="attribute"]/div[@class="cprice-area"]/span[@class="c-price"]/text()').extract()
            item['sold'] = ul.xpath('div[@class="attribute"]/div[@class="sale-area"]/span[@class="sale-num"]/text()').extract()
            yield item