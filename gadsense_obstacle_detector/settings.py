# -*- coding: utf-8 -*-

# Scrapy settings for gadsense_obstacle_detector project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'gadsense_obstacle_detector'

SPIDER_MODULES = ['gadsense_obstacle_detector.spiders']
NEWSPIDER_MODULE = 'gadsense_obstacle_detector.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'gadsense_obstacle_detector (+http://www.yourdomain.com)'

DOWNLOAD_DELAY = 1.0
