# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from baidufanyi import settings

class BaidufanyiPipeline(object):

    def __init__(self):
        host = settings.MONGO_HOST
        port = settings.MONGO_PORT
        db = settings.MONGO_DBNAME
        collection = settings.MONGO_COLLECTIONNAME
        client = pymongo.MongoClient(host=host, port=port)
        mgd = client[db]
        self.post = mgd[collection]


    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item
