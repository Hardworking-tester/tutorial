# -*- coding: utf-8 -*-
from tutorial import settings
import os
import requests

class TutorialPipeline(object):
    def process_item(self, item, spider):
        if 'image_urls' in item:  # 如何‘图片地址’在项目中
            images = []  # 定义图片空集

            dir_path = '%s/%s' % (settings.IMAGES_STORE, spider.name)

            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            for image_url in item['image_urls']:
                print "--------------------------------------------wwg3-----------------------------------------------"
                print image_url
                us = image_url.split('/')[3:]
                image_file_name = '_'.join(us)
                file_path = '%s/%s' % (dir_path, image_file_name)
                images.append(file_path)
                if os.path.exists(file_path):
                    continue

                with open(file_path, 'wb') as handle:
                    response = requests.get(image_url, stream=True,headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0"})
                    for block in response.iter_content(1024):
                        if not block:
                            break

                        handle.write(block)

            item['images'] = images
        return item
