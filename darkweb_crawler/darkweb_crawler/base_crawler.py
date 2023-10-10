import scrapy
from fake_useragent import UserAgent
from .config import TOR_SOCKS_PORT

class BaseCrawler(scrapy.Spider):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ua = UserAgent()

    def start_requests(self):
        for url in self.start_urls:
            request = scrapy.Request(url=url, callback=self.parse)
            self.set_request_headers(request)
            self.set_request_proxies(request)
            yield request

    def set_request_headers(self, request):
        request.headers['User-Agent'] = self.ua.random

    def set_request_proxies(self, request):
        request.meta['proxy'] = f'socks5://127.0.0.1:{TOR_SOCKS_PORT}'
