import scrapy
import json
from scrapy import signals
from .base_crawler import BaseCrawler

class MarketplaceCrawler(BaseCrawler):
    name = "marketplace_crawler"
    start_urls = [...]  # Replace with the actual onion marketplace URLs

    marketplaces = []

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super().from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def spider_closed(self):
        with open("marketplaces_data.json", "w") as f:
            json.dump(self.marketplaces, f, indent=4)

    def parse(self, response):
        product_listings = []

        # Parse the marketplace content and extract product information
        for product in response.css('div.product'):
            title = product.css('a.product-title::text').get()
            price = product.css('span.price::text').get()
            seller = product.css('span.seller::text').get()

        product_listings.append({
            "title": title,
            "price": price,
            "seller": seller
        })

        self.marketplaces.append({
            "url": response.url,
            "product_listings": product_listings
        })
