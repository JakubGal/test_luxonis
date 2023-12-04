# Scrapy settings for scrapy_project
# Comprehensive documentation available at:
# https://docs.scrapy.org/en/latest/topics/settings.html

BOT_NAME = 'scrapy_project'

SPIDER_MODULES = ['scrapy_project.spiders']
NEWSPIDER_MODULE = 'scrapy_project.spiders'

# Middleware for randomizing user agents
DOWNLOADER_MIDDLEWARES = {
    'scrapy_project.middlewares.RandomUserAgentMiddleware': 400,
}

# Pipeline for storing items in a PostgreSQL database
ITEM_PIPELINES = {
    'scrapy_project.pipelines.PostgresPipeline': 300,
}

# Disable obeying robots.txt rules
ROBOTSTXT_OBEY = False

# Uncomment and customize the settings below according to your project's needs:

# User agent string (uncomment to use)
# USER_AGENT = "scrapy_project (+http://www.yourdomain.com)"

# Maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Delay for requests to the same website (default: 0)
# DOWNLOAD_DELAY = 3

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Default request headers
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }

# Enable AutoThrottle extension (disabled by default)
# AUTOTHROTTLE_ENABLED = True
# AUTOTHROTTLE_START_DELAY = 5
# AUTOTHROTTLE_MAX_DELAY = 60
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# AUTOTHROTTLE_DEBUG = False

# HTTP caching (disabled by default)
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Future-proof settings
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
