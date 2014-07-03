
__author__ = 'Thierno BAH'
from pymongo import Connection
from lxml import html
from lxml.html.clean import clean_html
from lxml.html.clean import Cleaner
from lxml import etree

class Processing:

    def __init__(self):
        try:
            self.c = Connection(host="127.0.0.1", port=27017)
        except:
            print("could not connect to mongodb")


    def data_processing(self, data):

        cleaner = Cleaner(page_structure=False, links=False)
        doc = cleaner.clean_html(data)
        #tree = html.fromstring(doc)
        ht = etree.HTMLParser(encoding="utf-8")
        tree = etree.HTML(doc, parser=ht)
        pet_type = tree.xpath(".//*[@id='main']/div/div[1]/div[1]/div[1]/a[1]/text()")
        category = tree.xpath(".//*[@id='main']/div/div[1]/div[1]/div[1]/a[2]/h1/text()")
        title = tree.xpath(".//*[@id='upperpart']/div[2]/h1/strong/text()")
        description = tree.xpath(".//*[@id='upperpart']/div[2]/div[2]/p[2]/text()")
        price = tree.xpath(".//*[@id='fiche']/div[2]/div[2]/div[5]/p/text()")
        promotion_price = tree.xpath(".//*[@id='fiche']/div[2]/div[2]/div[5]/p[2]/text()")

        print(pet_type[0])
        print(category[0])
        print(title[0])
        print(description[0])
        print(price[0])
        print(promotion_price[0])

        pass

    def storing_price(self,price,promotion_price):
         pass

    def page_rank(self,url):
        pass

    def query_query(self,hotst):
        pass


