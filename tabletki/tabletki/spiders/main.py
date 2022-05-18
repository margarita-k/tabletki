import scrapy
import os
from os.path import dirname
import csv

current_dir = os.path.dirname(__file__)
print(f"current dir: {current_dir}")
top_dir = dirname(dirname(dirname(current_dir)))
print(f"top dir {top_dir}")
url = os.path.join(top_dir, "html\\working-pharmacies-in-dniprovskyi-district")

class tabletki_spider(scrapy.Spider):
    name = 'tabletki'
    start_urls = [f"file:\\{url}"]
    if os.path.exists('tabletki.csv') is not True:
        with open("tabletki.csv", "w",encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['address', 'location'])    

    def parse(self, response):
        addresses = response.xpath("//div[@class='address-card__header--address']/span/text()").getall()
        location = response.xpath("//div[@class='address-card__header address-card__header--block ']").xpath('@data-location').getall()

        rows = []
        for i in range(len(location)):
            newRow = [addresses[i], location[i]]
            rows.append(newRow)
        with open('tabletki.csv', 'a',encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(rows)


