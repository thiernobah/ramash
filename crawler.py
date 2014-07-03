#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.parse import urlparse
import urllib
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import os
import urllib3
from processing import Processing

class Crawler:
    def __init__(self, start_url):
        self.start_url = start_url
        h = urlparse(start_url)
        self.host = h[1]
        self.http = urllib3.PoolManager()
        self.processing = Processing()

    def neighbor(self,url):
            try:
               response = self.http.request("GET",url)
               self.html = response.data
               soup = BeautifulSoup(self.html,"lxml")
               return soup
            except:
                print("could not open url %s "  %url)

    def test(self,url):

        response = self.http.request("GET",url)
        html = response.data
        self.processing.data_processing(html)


    def bfs(self):
        url = []
        visited = []
        url.append(self.start_url)

        while len(url) > 0:
            link = url.pop()
            print(len(url))

            uri = urljoin(self.start_url, link)
            parse_url = urlparse(uri)
            #f = open(self.host+"\n", 'a+')

            try:
                for tag in self.neighbor(link).findAll('a',href=True):
                    tag = urljoin(self.start_url, tag['href'])
                    tag = tag.split('#')[0]
                    junk, ext = os.path.splitext(tag)
                    if tag not in visited and ext != '.jpg' and ext != '.JPG' and ext != '.pdf':
                        visited.append(tag)
                        if parse_url[1]  == str(self.host):
                              url.append(tag)
                              self.processing.data_processing(self.html)
                              #f.writelines(tag+"\n")
                              print(tag)
            except:
                pass


c = Crawler("https://news.ycombinator.com/")
#s = c.bfs()
c.test("http://www.wanimo.com/fr/chiens/friandise-complement-sc2/coffret-gourmand-pour-chien-sf12597/")