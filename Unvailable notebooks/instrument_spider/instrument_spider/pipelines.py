# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
from urllib.parse import urlparse
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline
from items import CrawlerItem
from scrapy.loader import ItemLoader

class FilePipeline(FilesPipeline):
    """def item_completed(self, results, item, info):
        for result in [x for ok,x in results if ok]:
            path = result['path']
            new_path = os.path.join((item['folder'],os.path.basename(path)))
            if not os.rename(path, target_path):
                raise ImageException("Could not move image to target folder")
            if self.FILES_RESULT_FIELD in item.fields:
                result['path'] = new_path
                item[self.FILES_RESULT_FIELD].append(result)
        return item"""
    
    def file_path(self, request, response=None, info=None, *,item=None):
        adapter = ItemAdapter(item)
        folder = "full/" 
        #adapter["type_name"]+r"/"
        return adapter.get("type_name")[0]+r"/" + os.path.basename(urlparse(request.url).path)