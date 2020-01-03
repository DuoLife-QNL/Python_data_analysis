import scrapy
import re
from lianjia.items import LianJiaItem # 引入item对象
class LianJiaSpider(scrapy.Spider):  
    name = "lianjia" # 爬虫的名字是 lianjia
    allowed_domains = ["dl.lianjia.com/"]  #允许爬取的网站域名
    start_urls = []
    for x in range(1, 101):
        url = 'https://dl.lianjia.com/ershoufang/pg{}/'.format(x)
        start_urls.append(url)

    def parse(self, response): #解析爬取的内容
        item = LianJiaItem() #生成一个在 items.py 中定义好的 xuetangitem 对象用于接收爬取的数据

        # 总价
        # /html/body/div[4]/div[1]/ul/li[1]/div[1]/div[6]/div[1]/span
        # /html/body/div[4]/div[1]/ul/li[2]/div[1]/div[6]/div[1]/span

        # 单价
        # /html/body/div[4]/div[1]/ul/li[1]/div[1]/div[6]/div[2]/span
        # /html/body/div[4]/div[1]/ul/li[2]/div[1]/div[6]/div[2]/span
        for each in response.xpath('/html/body/div[4]/div[1]/ul/li'):
            item['total_price'] = each.xpath("div[1]/div[6]/div[1]/span/text()").get()    
            temp = each.xpath("div[1]/div[6]/div[2]/span/text()").get()
            # print('******************************************************')
            # print(temp)
            # print(re.findall(r"\d+\.?\d*", temp)[0])
            # print('******************************************************')
            item['unit_price'] = re.findall(r"\d+\.?\d*", temp)[0]
            # item['unit_price'] = each.xpath("div[1]/div[6]/div[2]/span/text()").get()
            if(item['total_price'] and item['unit_price']): #去掉值为空的数据
                yield(item) #返回 item 数据给到 pipelines 模块
