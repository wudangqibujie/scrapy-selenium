from selenium import webdriver
from lxml import etree
import time

for i in range(1,11):
    url = "https://www.guazi.com/sz/bmw-5/o{page}/"
    url = url.format(page = i)
    r = webdriver.Chrome()
    r.get(url)
    time.sleep(5)
    text = r.page_source
    html = etree.HTML(text)
    # print(text)
    if html.xpath('//div[@class="phone-email"]/p/i/text()'):
        a = html.xpath('//ul[@class="carlist clearfix js-top"]/li')

        for one in a:
            d_c = {}
            d_c['model'] = one.xpath('a/h2/text()')
            d_c['year_age'] = one.xpath('a/div[@class="t-i"]/text()')
            d_c['now_price'] = one.xpath('a/div[@class="t-price"]/p/text()')
            d_c['ex_price'] = one.xpath('a/div[@class="t-price"]/em/text()')
            with open("BMW.json","ab") as f:
                f.write((str(d_c)+"\n").encode("utf-8"))




