__author__ = 'thierno'

from urllib.parse import urlparse
import urllib
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import os

class Crawler:
    def __init__(self, start_url):
        self.start_url = start_url
        h = urlparse(start_url)
        self.host = h[1]

    def neighbor(self, url):
        try:
            remote_data = urllib.request.urlopen(url)
            html = remote_data.read()
            soup = BeautifulSoup(html,"lxml")
            return soup
        except:
            print("could not open url %s"  %url)

    def bfs(self):
        url = []
        visited = []
        url.append(self.start_url)

        while len(url) > 0:
            link = url.pop()
            print(len(url))

            uri = urljoin(self.start_url, link)
            parse_url = urlparse(uri)
            f = open(self.host+"\n", 'a+')

            try:
                for tag in self.neighbor(link).findAll('a',href=True):
                    tag = urljoin(self.start_url, tag['href'])
                    tag = tag.split('#')[0]
                    junk, ext = os.path.splitext(tag)
                    if tag not in visited and ext != '.jpg' and ext != '.JPG' and ext != '.pdf':
                        visited.append(tag)
                        if parse_url[1]  == str(self.host):
                              url.append(tag)
                              f.writelines(tag+"\n")
                              print(tag)
            except:
                pass


c = Crawler("http://www.lequipe.fr/Directs/")
s = c.bfs()

'''
url = 'http://www.looping.com/uollo/mo#klll#lin'
url=url.split('#')[0]

print(url)

'''
