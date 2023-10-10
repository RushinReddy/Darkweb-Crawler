from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from .marketplace_crawler import MarketplaceCrawler
from .forum_crawler import ForumCrawler

if __name__ == "__main__":
    process = CrawlerProcess(get_project_settings())
    process.crawl(MarketplaceCrawler)
    process.crawl(ForumCrawler)
    process.start()
