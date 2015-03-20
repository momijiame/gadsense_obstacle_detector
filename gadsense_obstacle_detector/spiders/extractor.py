#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy
from bs4 import BeautifulSoup
from furl import furl

from gadsense_obstacle_detector.items import ObstaclePostItem


class EntrySpider(scrapy.Spider):
    name = 'entry'
    allowed_domains = ['momijiame.tumblr.com']

    def __init__(self, entry_id, *args, **kwargs):
        super(EntrySpider, self).__init__(*args, **kwargs)

        self.entry_id = entry_id
        url = 'http://momijiame.tumblr.com/post/{entry_id}'.format(
            entry_id=self.entry_id,
        )
        self.start_urls = [url]

    def parse(self, response):
        body = response.body
        soup = BeautifulSoup(body)

        content = soup.find('div', {'class': 'body'})

        links = content.find_all('a')
        if len(links) > 0:
            return ObstaclePostItem(url=response.request.url)

        imgs = content.find_all('img')
        if len(imgs) > 0:
            return ObstaclePostItem(url=response.request.url)


class TopSpider(scrapy.Spider):
    name = 'top'
    allowed_domains = ['momijiame.tumblr.com']
    start_urls = [
        'http://momijiame.tumblr.com/',
    ]

    def parse(self, response):
        body = response.body
        soup = BeautifulSoup(body)

        entries = soup.find_all('div', {'class': 'title'})
        for entry in entries:
            entry_url = entry.a['href']
            f = furl(entry_url)
            entry_id = f.path.segments[1]
            spider = EntrySpider(entry_id=entry_id)
            req = scrapy.Request(url=entry_url, callback=spider.parse)
            yield req

        next_page = soup.find('li', {'class': 'next'})
        if next_page is None:
            return

        next_page_path = next_page.a['href']
        f = furl('http://momijiame.tumblr.com')
        f.path.add(next_page_path)
        req = scrapy.Request(url=f.url, callback=self.parse)
        yield req
