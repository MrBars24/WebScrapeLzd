import requests
import csv
import sys
import operator
import uuid
from bs4 import BeautifulSoup

class WebScrape:
	def __init__(self):
		print("WebScrape Imported")

	def lazada_scrape(self,head,category,url,mn=0,mx=0):
		list_of_rows = []
		url = "http://www.lazada.com.ph/"+ url +"/"
		source_code = requests.get(url)
		txt = source_code.text
		soup = BeautifulSoup(txt, 'html.parser')
		pages = soup.select("div.c-paging__wrapper a.c-paging__link")
		counting = int(len(pages)-1)
		max_page = 1

		try:
			max_page = int(pages[counting].get_text())
		except IndexError:
			print("Cannot Retrieve Max Page")
		except UnboundLocalError:
			max_page = 1

		sys.stdout.write("\nScraping at %s - %s\n" % (head,category))
		page = 1
		if mn != 0 and mx != 0:
			page = mn
			max_page = mx

		while page <= max_page:
			sys.stdout.write("\rScraping %d out of %d" % (page,max_page))
			source_code = requests.get(url +"/?page=" + str(page))
			txt = source_code.text
			soup = BeautifulSoup(txt,'html.parser')
			for div in soup.find_all("div", {"class":"product-card"}):
					mylist = []
					for link in div.find_all("a"):
						mylist.insert(0,str(link.get("href")))
						for title in div.find_all("span", {"class":"product-card__name"}):
							mylist.insert(1,(str(title.text).encode("utf-8")))
							mylist.insert(2,head)
							mylist.insert(3,category)
						for price in div.find_all("div", {"class":"product-card__price"}):
							mylist.insert(4,str(price.text.replace("\u20B1","").replace("\uffa0"," ").replace(",","")))
							
						sale = div.find_all("div", {"class":"product-card__sale"})
						if not sale:
							mylist.insert(5,"0%")
						else:                            
							for sales in sale:
								mylist.insert(5,str(sales.text))
						old = div.find_all("div", {"class":"old-price-wrap"})
						if not old:
							mylist.insert(6,"0.00")
						else:                            
							for olds in old:
								mylist.insert(6,str(olds.text).replace("\u20B1","").replace("\uffa0"," ").replace("\n","").replace(",",""))

						installment = div.find_all("span", {"class":"installment-part"})
						if not installment:
							mylist.insert(7,"0.00")
						else:
							for installments in installment:
								mylist.insert(7,str(installments.text).replace("\u20B1","").replace("\uffa0"," ").replace(",",""))

						rating = div.find_all("span", {"class":"rating__number"})
						if not rating:
							mylist.insert(8,"(0 reviews)")
						else:
							for ratings in rating:
								mylist.insert(8,str(ratings.text))

						img = div.find_all("img", {"data-image-key":"catalog"})
						for imgs in img:
							try:
								mylist.insert(9,str(imgs.attrs["data-original"]))
							except:
								pass

						try:
							wr = csv.writer(self.myfile, quoting=csv.QUOTE_ALL)
							wr.writerow(mylist)
						except PermissionError:
							pass

			page+=1
		sys.stdout.flush()

	def run_lazada_scrape(self,m,s):
		self.myfile = open(str(uuid.uuid4()) + ".csv", 'w', newline='')
		writer = csv.DictWriter(self.myfile, fieldnames = [ "url", "product_name", "product_header", "product_category", "product_price", "product_sale", "product_old", "installment", "rating", "product_image"], delimiter=',')
		writer.writeheader()
		for k,v in sorted(s.items(), key=operator.itemgetter(1)):
			self.lazada_scrape(m,k,v)

		print("\nDone Scraping")

	def run_custom_scrape(self,head,category,url,mn=0,mx=0):
		self.myfile = open(str(uuid.uuid4()) + ".csv", 'w', newline='')
		writer = csv.DictWriter(self.myfile, fieldnames = [ "url", "product_name", "product_header", "product_category", "product_price", "product_sale", "product_old", "installment", "rating", "product_image"], delimiter=',')
		writer.writeheader()
		self.lazada_scrape(head,category,url,mn,mx)
