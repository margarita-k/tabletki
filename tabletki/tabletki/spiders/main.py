import scrapy
import os
from os.path import dirname
import csv
from datetime import datetime

current_dir = os.path.dirname(__file__)
print(f"current dir: {current_dir}")
top_dir = dirname(dirname(dirname(current_dir)))
print(f"top dir {top_dir}")
url = os.path.join(top_dir, "html\\working-pharmacies-in-dniprovskyi-district")

cur_date = datetime.now()
fileName = "tabletki-" + str(cur_date.date()) + '-' + str(cur_date.hour) + str(cur_date.minute) + str(cur_date.second) + ".csv"

class tabletki_spider(scrapy.Spider):
    name = 'tabletki'
    start_urls = [f"file:\\{url}"]
    if os.path.exists(fileName) is not True:
        with open(fileName, "w",encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["!!! Retrieved on " + str(cur_date.date()) +'-' + str(cur_date.time()) + " !!!"])
            writer.writerow(['address', 'location', 'city', 'district'])    
            print("#"*30 + "\n" + "new file created: " + fileName)

    def parse(self, response):
        addresses = response.xpath("//div[@class='address-card__header--address']/span/text()").getall()
        location = response.xpath("//div[@class='address-card__header address-card__header--block ']").xpath('@data-location').getall()
        city = response.xpath("//div[@class='selected-filter__address--city']/span/text()").get()
        district = response.xpath("//div[@class='selected-filter__address--city']/span[@class='addresses']/text()").get()

        rows = []
        for i in range(len(location)):
            newRow = [addresses[i], location[i], city, district]
            rows.append(newRow)
        with open(fileName, 'a',encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(rows)


