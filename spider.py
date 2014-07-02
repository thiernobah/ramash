from urllib.parse import urlparse
import urllib
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup

class Spider:

    def __init__(self, dbname):
        pass

    def __del__(self):
        pass

    def dbcommit(self):
        pass

    def getentryid(self,table,field,value,createnew=True):
        return None

    def addtoindex(self,url,soup):
        print("Indexing %s" %url)

    def gettextonly(self,soup):
        return None

    def separatewords(self,text):
        return None

    def isindexed(self, url):
        return False

    def addlinkref(self,urlFrom,urlTo,linkText):
        pass

    def crawl(self,pages,depth=2):
        for i in range(depth):
            newspage = set()
            for page in pages:
                try:
                    c = urllib.request.urlopen(page)
                except:
                    print("could not open %s" %page)
                    continue

                soup = BeautifulSoup(c.read())
                self.addtoindex(page,soup)
                links = soup('a')

                for link in links:
                    if('href' in dict(link.attrs)):
                        url=urljoin(page,link['href'])
                        if url.find("'")!=-1:continue
                        url=url.split('#')[0]
                        if url[0:4] == 'http' and not self.isindexed(url):
                            newspage.add(url)
                        linkText = self.gettextonly(link)
                        self.addlinkref(page,url,linkText)

                self.dbcommit()
            pages=newspage

    def createindextable(self):
        pass









