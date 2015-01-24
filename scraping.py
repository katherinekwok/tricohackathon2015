# need to install lxml first
from lxml import html
import requests
import csv

basket = ['coke', 'sprite', 'red bull', 'monster energy drink']


url_before_query = "http://www.amazon.com/s/keyword="

###for later use ###
#stores_url = {'amazon': []}
# url_before_query, product, price
#amazon_list = ["http://www.amazon.com/s/keyword=", '//h2[@class="a-size-medium s-inline s-access-title a-text-normal"]/text()','//span[@class="a-size-base a-color-price s-price a-text-bold"]/text()']
#kmart_list = ["http://www.kmart.com/search=", ]
#walmart_list = ["http://www.walmart.com/search/?query=",]


for item in basket:
	page = requests.get(url_before_query + item)
	tree = html.fromstring(page.text)
	product = tree.xpath('//h2[@class="a-size-medium s-inline s-access-title a-text-normal"]/text()')
	price = tree.xpath('//span[@class="a-size-base a-color-price s-price a-text-bold"]/text()')

	# updates the data.csv 
	with open('data.csv', 'ab') as csvfile:
		fieldnames = ['product', 'price']
		writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldnames)
		for index in range(len(product)):
			writer.writerow({'product': product[index], 'price': price[index][1:]})
    
    