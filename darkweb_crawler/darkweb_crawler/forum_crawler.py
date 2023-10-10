import json
from scrapy import signals
from .base_crawler import BaseCrawler

class ForumCrawler(BaseCrawler):
    name = "forum_crawler"
    start_urls = [...]  # Replace with the actual onion forum URLs

    forums = []

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super().from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def spider_closed(self):
        with open("forums_data.json", "w") as f:
            json.dump(self.forums, f, indent=4)

    def parse(self, response):
        threads = []

        # Parse the forum content and extract thread information
        for thread in response.css('div.thread'):
            title = thread.css('a.thread-title::text').get()
            author = thread.css('span.author::text').get()
            thread_url = response.urljoin(thread.css('a.thread-title::attr(href)').get())

            threads.append({
                "title": title,
                "author": author,
                "url": thread_url
            })

        self.forums.append({
            "url": response.url,
            "threads": threads
        })


        threads.append({
            "title": title,
            "author": author,
            "url": thread_url
        })

        self.forums.append({
            "url": response.url,
            "threads": threads
        })
