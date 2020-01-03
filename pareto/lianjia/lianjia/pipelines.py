import csv
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class LianjiaPipeline(object):
    def open_spider(self, spider):
        try: #打开 json 文件
            self.file = open('Data.csv', "w", encoding="utf-8")

        except Exception as err:
            print(err)
    def process_item(self, item, spider):
        writer = csv.writer(self.file)
        writer.writerow([item['total_price'], item['unit_price']])
        # self.file.write('"{}",'.format(item['total_price']))
        # self.file.write('"{}",'.format(item['unit_price']))
        return item
    def close_spider(self,spider):
        self.file.close() #关闭文件
