# tabletki
### This is a training project in data scraping

Here I created a spider using scrapy lib, the spider crawls the predownloaded html page. The goal is to get addresses and locations of working pharmacies in one of Kyiv districts. Dniprovskyi district was taken as an example.

In order to get data for another district, one needs to download corresponding page from the website and replace file name in `start_urls` in spiders/main.py
