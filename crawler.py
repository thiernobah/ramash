__author__ = 'thierno'

from urllib.parse import urlparse
import urllib
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import os
import urllib3

class Crawler:
    def __init__(self, start_url):
        self.start_url = start_url
        h = urlparse(start_url)
        self.host = h[1]
        self.http = urllib3.PoolManager()
    '''
    def neighbor(self, url):
        try:
            remote_data = urllib.request.urlopen(url)
            html = remote_data.read()
            soup = BeautifulSoup(html,"lxml")
            return soup
        except:
            print("could not open url %s"  %url)
    '''
    def neighbor(self,url):

         response = self.http.request("GET",url)
         html = response.data
         #print(html)
         soup = BeautifulSoup(html,"lxml")
         return soup

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


c = Crawler("https://www.google.fr/search?q=google&oq=google&aqs=chrome..69i57j0l2j69i65l3.4543j0j4&client=ubuntu-browser&sourceid=chrome&es_sm=91&ie=UTF-8#q=google&tbm=nws")
s = c.bfs()

