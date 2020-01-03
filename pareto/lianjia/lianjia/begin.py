from scrapy import cmdline
import csv

csvfile = open('Data.csv', 'w', encoding='utf-8')
writer = csv.writer(csvfile)
writer.writerow(['total_price', 'unit_price'])

cmdline.execute('scrapy crawl lianjia'.split())