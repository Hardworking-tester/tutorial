# encoding:utf-8

from scrapy.spider import Spider
from tutorial.items import TutorialItem
class DmozSpider(Spider):
	name = "dmoz"
	allowed_domains = ["meizitu.com"]
	start_urls = [
		"http://www.meizitu.com/"]
	def parse(self, response):
		# filename = response.url.split("/")[-2]
		# open(filename, 'wb').write(response.body)
		current_url = response.url  # 爬取时请求的url
		body = response.body  # 返回的html
		unicode_body = response.body_as_unicode()  # 返回的html unicode
		print 'wwg1----------------------------------------------------------'
		# print response
		# print current_url
		# print body
		# data = open(r"F:\testresult\tt.txt", 'a')
		# data.write(body)

		for sel in response.xpath("//a"):
			item=TutorialItem()
			item['desc'] = sel.xpath('@href').extract()
			# mm=item['desc'][-1].encode('utf-8')
			mm=item['desc']
			print mm
			# if mm.__len__() !=0:
			# 	mm = item['desc'][-1].encode('utf-8')
			# 	print mm
				# data = open(r"F:\testresult\tt.txt", 'a')
				# data.write(mm)
				# data.write('\n')
		print 'wwg2----------------------------------------------------------'