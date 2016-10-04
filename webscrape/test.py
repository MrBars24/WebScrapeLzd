import requests
import csv
from bs3 import BeautifulSoup

class WebScrape:
	def __init__(self):
		print("WebScrape Imported")

	def lazada_scrape(self,head,category,url):
		list_of_rows = []
        url = "http://www.lazada.com.ph/"+ url +"/"
        source_code = requests.get(url)
        txt = source_code.text
        soup = BeautifulSoup(txt, 'html.parser')
        max_page = int(soup.select("span.pages > a:nth-of-type(6)")[0].get_text())
        page = 1
        myfile = open(category + ".csv", 'w', newline='')
        writer = csv.DictWriter(myfile, fieldnames = ["url", "product_name", "product_header", "product_category", "product_price", "product_sale", "product_old", "installment", "rating"], delimiter=',')
        writer.writeheader()
        while page <= max_page:
                print(page)
                url = "http://www.lazada.com.ph/shop-mobiles/?page=" + str(page)
                source_code = requests.get(url)
                txt = source_code.text
                soup = BeautifulSoup(txt,'html.parser')
                for div in soup.find_all("div", {"class":"product-card"}):
                        mylist = []
        
                        for link in div.find_all("a"):
                                mylist.append(str(link.get("href")))
                        for title in div.find_all("span", {"class":"product-card__name"}):
                                mylist.append(str(title.text).replace("\u200f"," ").replace("\uFF08","(").replace("\uff09",")"))
                                mylist.append(head)
                                mylist.append(category)
                        for price in div.find_all("div", {"class":"product-card__price"}):
                                mylist.append(str(price.text.replace("\u20B1","Php ")))

                        sale = div.find_all("div", {"class":"product-card__sale"})
                        if not sale:
                            mylist.append("0%")
                        else:                            
                            for sales in sale:
                                    mylist.append(str(sales.text))

                        old = div.find_all("div", {"class":"old-price-wrap"})
                        if not old:
                            mylist.append("Php 0.00")
                        else:                            
                            for olds in old:
                                    mylist.append(str(olds.text).replace("\u20B1","Php ").replace("\n",""))

                        installment = div.find_all("span", {"class":"installment-part"})
                        if not installment:
                            mylist.append("Php 0.00")
                        else:
                            for installments in installment:
                                mylist.append(str(installments.text).replace("\u20B1","Php "))

                        rating = div.find_all("span", {"class":"rating__number"})
                        if not rating:
                            mylist.append("(0 reviews)")
                        else:
                            for ratings in rating:
                                mylist.append(str(ratings.text))
                                        
                        list_of_rows.append(mylist)
                page+=1
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerows(list_of_rows)