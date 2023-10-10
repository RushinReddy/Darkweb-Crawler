BOT_NAME = 'darkweb_crawler'

SPIDER_MODULES = ['darkweb_crawler.spiders']
NEWSPIDER_MODULE = 'darkweb_crawler.spiders'

ROBOTSTXT_OBEY = False

# Enable downloader middlewares for custom User-Agent and proxy settings
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
}

# Configure the delay between requests and randomization of delay
DOWNLOAD_DELAY = 3.0
RANDOMIZE_DOWNLOAD_DELAY = True
DOWNLOAD_DELAY_STDDEV = 1.5

# Enable auto throttling to adjust crawl rate dynamically
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 60
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

# Configure the logging settings
LOG_LEVEL = 'INFO'
LOG_FORMATTER = 'scrapy.utils.log.CleanLoggingFormatter'

DEPTH_LIMIT = 2