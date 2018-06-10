# -*- coding: utf-8 -*-
import scrapy

from Tencent.items import TencentItem,PosiItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    offset = 0
    allowed_domains = ['hr.tencent.com']
    base_url = "https://hr.tencent.com/position.php?&start="
    start_urls = [base_url + str(page)for page in range(0, 3771, 10)]
    def parse(self, response):
        data_list = response.xpath("//tr[@class='even']|//tr[@class='odd']")
        for data in data_list:
            item = TencentItem()
            item['name']=data.xpath("./td[1]/a/text()").extract_first()
            item['name_link']="https://hr.tencent.com/"+data.xpath("./td[1]/a/@href").extract_first()
            item['type']=data.xpath("./td[2]/text()").extract_first()
            item['num']=data.xpath("./td[3]/text()").extract_first()
            item['location']=data.xpath("./td[4]/text()").extract_first()
            item['times']=data.xpath("./td[5]/text()").extract_first()



            yield item

        # if self.off < 3830:
        #     self.off +=10
        #     url = self.base_urls + str(self.off)
        # if not response.xpath("//a[@class='noactive' and @id='next']").extract_first():
        #     next_url = "https://hr.tencent.com/"+response.xpath("//a[@id='next']/@href").extract_first()
            # yield scrapy.Request(next_url, callback=self.parse)

            yield scrapy.Request(
                url = item['name_link'],callback=self.parse_page
            )

    def parse_page(self, response):
        item = PosiItem()
        # item = response.meta["obj"]
        item['zhize'] = "\n".join(response.xpath("//ul[@class='squareli']")[0].xpath("./li/text()").extract())
        item['yaoqiu'] = "\n".join(response.xpath("//ul[@class='squareli']")[1].xpath("./li/text()").extract())

        yield item
