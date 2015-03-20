#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy


class ObstaclePostItem(scrapy.Item):
    url = scrapy.Field()
