# -*- coding: utf-8 -*-

# Scrapy settings for baidufanyi project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'baidufanyi'
SPLASH_URL = 'http://localhost:8050'
SPIDER_MODULES = ['baidufanyi.spiders']
NEWSPIDER_MODULE = 'baidufanyi.spiders'

MONGO_DBNAME = 'baidufanyi'
MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
MONGO_COLLECTIONNAME = 'fanyi'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'baidufanyi (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}
HEADERS = {
'Accept':  '*/*',
'Accept-Encoding':  'gzip, deflate, br',
'Accept-Language':  'zh-CN,zh;q=0.9',
'Connection':  'keep-alive',
'Content-Length':  '38',
'Content-Type':  'application/x-www-form-urlencoded',
'Host':  'fanyi.baidu.com',
'Origin':  'https://www.baidu.com',
'Referer':  'https://www.baidu.com/sf_fanyi/?aldtype=16047&tpltype=sigma',
'User-Agent':  'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',}
FILEPATH = '/home/xiyujing/文档/随他吧歌词.txt'
# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {'scrapy_splash.SplashDeduplicateArgsMiddleware':100,
#
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'baidufanyi.middlewares.BaidufanyiDownloaderMiddleware': 900,
    'baidufanyi.middlewares.HttpProxyMiddleware': 300,

}
# DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'baidufanyi.pipelines.BaidufanyiPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
