import requests
import csv
from bs4 import BeautifulSoup

class WebScrape:
	def __init__(self):
		print("WebScrape Imported")

	def lazada_scrape(self,head,category,url):
		list_of_rows = []
		url = "http://www.lazada.com.ph/"+ url +"/"
		source_code = requests.get(url)
		txt = source_code.text
		soup = BeautifulSoup(txt, 'html.parser')
		pages = soup.select("div.c-paging__wrapper a.c-paging__link")
		counting = int(len(pages)-1)
		try:
			max_page = int(pages[counting].get_text())
		except IndexError:
			print("Cannot Retrieve Max Page")
		print(head,category,max_page)
		page = 1
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

						img = div.find_all("img", {"data-image-key":"catalog"})
						for imgs in img:
							mylist.append(str(imgs.attrs["data-original"]))

						try:
							wr = csv.writer(self.myfile, quoting=csv.QUOTE_ALL)
							wr.writerow(mylist)
						except PermissionError:
							pass
			page+=1

	def run_lazada_scrape(self,c):
		if c == "electronics":
			category = {"electronics":{"mobiles":"shop-mobiles","tablets":"shop-tablets", \
			"accessories":"shop-mobile-accessories","power banks":"shop-power-bank", \
			"phone cases":"shop-mobile-cases-covers","tablet accessories":"shop-cases-covers", \
			"screen protectors":"shop-screen-protectors","batteries & chargers":"shop-chargers-batteries", \
			"cables & docks":"shop-mobile-cables","mobile accessories":"shop-mobile-charms", \
			"parts & tools":"shop-mobiles-tablets-parts-tools","selfie sticks":"shop-phone-selfie-sticks", \
			"laptops":"shop-laptops","2-in-1s":"shop-2in1-laptops", \
			"gaming":"shop-gaming-laptops","netbooks":"shop-traditional-laptops", \
			"ultrabooks":"shop-laptops","macbooks":"shop-macbook", \
			"computers":"shop-desktop-computers","storage":"shop-computer-storage", \
			"computer components":"shop-computer-components","computer accessories":"shop-computer-accessories", \
			"printers & accessories":"shop-printers-ink","network components":"shop-network-components", \
			"sports & action cameras":"shop-action-camcorders","point & shoot cameras":"shop-point-shoot", \
			"dslrs":"shop-dslr","mirrorless cameras":"shop-mirrorless", \
			"drones":"shop-camera-drones","security & gadget cameras":"shop-security-cameras", \
			"instant cameras":"shop-instant-camera","camera accessories":"shop-camera-accessories", \
			"memory cards":"shop-camera-memory-card","monopods & tripods":"shop-tripods-monopods", \
			"camera bags & cases":"shop-camera-bags","action camera accessories":"shop-sport-camera-accessories", \
			"televisions":"shop-televisions","24 inches & below":"", \
			"25 - 31 inches":"","32 inches":"", \
			"33 - 42 inches":"","43 - 54 inches":"", \
			"55 inches & above":"","audio":"shop-audio", \
			"headphones & headsets":"shop-audio-headphones","portable speakers":"shop-portable-speakers-for-tv", \
			"home & audio theater":"shop-home-audio-theater","audio players":"shop-mp3-player-ipods", \
			"video":"shop-video","projectors":"shop-projectors-2", \
			"streaming media players":"shop-video-media-players","gaming":"shop-gaming", \
			"playstation":"shop-gaming/sony/","xbox":"shop-gaming/microsoft/", \
			"nintendo":"nintendo","wearable tech":"shop-wearable-technology", \
			"smartwatches":"shop-gadgets-smart-watches","activity & fitness trackers":"shop-fitness-trackers", \
			"vr headsets":"shop-vr","smart trackers":"shop-smart-tracking"}}
		elif c == "wfashion":
			category = {"women's fashion":{"clothing":"shop-womens-clothing","dresses":"shop-womens-dresses", \
			"t-shirts & tops":"shop-womens-t-shirt-tops","jackets & coats":"shop-womens-jackets-coats", \
			"blouses & shirts":"shop-womens-blouses","pants & shorts":"shop-womens-clothing-pants", \
			"skirts":"shop-womens-skirts","jeans":"shop-womens-jeans", \
			"lingerie & nightwear":"shop-womens-lingerie-nightwear","muslim wear":"shop-womens-muslim-wear", \
			"swim wear":"shop-womens-swimwear","accessories":"shop-womens-accessories", \
			"bags":"shop-womens-bags","tote bags":"shop-womens-tote-bags", \
			"shoulder bags":"shop-womens-cross-body-bags","top handle bags":"shop-womens-top-handle-bags", \
			"cross body bags":"shop-womens-cross-body-bags","satchels":"shop-womens-cross-body-bags", \
			"sling bags":"shop-womens-cross-body-bags","backpacks":"shop-womens-backpacks", \
			"clutches":"shop-womens-clutches","wallets":"shop-womens-purses", \
			"eyewear":"shop-womens-eyewear","sunglasses":"shop-womens-sunglasses", \
			"eyeglasses":"shop-womens-eyeglasses","shoes":"shop-womens-shoes", \
			"sneakers":"shop-womens-sneakers","flat shoes":"shop-womens-flats", \
			"heels":"shop-womens-heels","boots":"shop-womens-boots", \
			"sandals":"shop-womens-sandals","flip flops":"shop-womens-shoes-flip-flops", \
			"jewellery":"shop-womens-jewellery","bracelets & bangles":"shop-womens-bracelets-bangles", \
			"necklaces & pendants":"shop-womens-necklaces-pendants","rings":"shop-womens-rings", \
			"earrings":"shop-womens-earrings","jewellery sets":"shop-womens-jewellery-sets-others", \
			"watches":"shop-womens-watches","fashion":"shop-womens-fashion-watches", \
			"business":"shop-womens-business-watches","casual":"shop-womens-casual-watches", \
			"sports":"shop-womens-sports-watches","buying guide: watches & accessories":"watches-sunglasses-jewellery-buying-guide", \
			"girl's fashion":"shop-girls-fashion","clothing":"shop-clothing-girls", \
			"shoes":"shop-shoes-girls","bags":"shop-kids-bag", \
			"watches":"shop-watches-girls","accessories":"shop-accessories-girls"}}
		elif c=="mfashion":
			category = {"men's fashion":{"clothing":"shop-mens-clothing","jacket & coats":"shop-mens-jackets & coats", \
			"t-shirts":"shop-mens-t-shirts","pants & shorts":"shop-mens-pants", \
			"jeans":"shop-mens-jeans","shirts":"shop-mens-shirts", \
			"sweaters & cardigans":"shop-mens-sweaters-cardigans","suits":"shop-mens-suits", \
			"uderwear & socks":"shop-mens-clothing-underwear","swim wear":"shop-mens-swimwear", \
			"accessories":"shop-mens-accessories","bags":"shop-mens-bags", \
			"shoulder bags":"shop-mens-messenger-bags","sling bags":"shop-mens-cross-body-bags", \
			"messenger bags":"shop-mens-messenger-bags","satchels":"shop-mens-messenger-bags", \
			"backpacks":"shop-mens-backpacks","wallets":"shop-mens-wallets", \
			"eyewear":"shop-mens-eyewear","sunglasses":"shop-mens-sunglasses", \
			"eyeglasses":"shop-mens-eyeglasses","shoes":"shop-mens-shoes", \
			"sneakers":"shop-mens-sneakers","flat shoes":"shop-mens-shoes", \
			"formal shoes":"shop-mens-formal-shoes","sandals":"shop-mens-sandals", \
			"boots":"shop-mens-boots","jewellery":"shop-mens-jewellery", \
			"bracelets":"shop-mens-bracelets","necklaces & pendants":"shop-mens-necklaces-pendants", \
			"rings":"shop-mens-rings","earrings":"shop-mens-earrings", \
			"shirt accessories":"shop-mens-shirt-accessories","watches":"shop-mens-watches", \
			"business":"shop-mens-business-watches","casual":"shop-mens-casual-watches", \
			"fashion":"shop-mens-fashion-watches","sports":"shop-mens-sports-watches", \
			"buying guide: watches & accessories":"watches-sunglasses-jewellery-buying-guide","boys fashion":"shop-fashion-boys", \
			"clothing":"shop-clothing-boys","shoes":"shop-shoes-boys", \
			"bags":"shop-kids-bag","watches":"shop-watches-boys", \
			"accessories":"shop-accessories-boys"}}
		elif c=="homeliving":
			category = {"home & living":{"small kitchen appliances":"shop-small-kitchen-appliances","food preparation":"shop-food-preparation", \
			"juicers":"shop-juicers-fruit-extractors","electric grills":"shop-electric-grills", \
			"rice cookers & steamers":"shop-rice-cookers-steamers","coffee machines & accessories":"shop-coffee-machines-accessories", \
			"water dispensers":"shop-water-dispensers-2","kettles & thermopots":"shop-electric-kettle-thermo-pots", \
			"garment care":"shop-garment-care","irons":"shop-irons", \
			"sewing machines":"shop-sewing-machines","garment steamers":"shop-steamers-presses", \
			"large appliances":"shop-large-home-appliances","refrigerators":"shop-refrigerators", \
			"washers & dryers":"shop-large-washers-dryers","microwave & ovens":"shop-large-microwaves-ovens", \
			"cooktops":"shop-large-cooktops","freezers":"shop-freezers", \
			"ice makers":"shop-ice makers","cooling & heating":"shop-cooling-heating", \
			"air conditioners":"shop-air-conditioners","air coolers":"shop-air-coolers", \
			"fans":"shop-fans","air purifiers & dehumidifiers":"shop-air-purifiers-dehumidifiers-humidifiers", \
			"water heaters":"shop-water-heaters","kitchen & dining":"shop-kitchen-dining", \
			"cookware":"shop-cookware","bakeware":"shop-bakeware", \
			"cooking knives":"shop-cooking-knives","kitchen tools":"shop-kitchen-tools-accessories", \
			"tableware":"shop-tableware","kitchen storage":"shop-kitchen-storage", \
			"house keeping":"shop-housekeeping","vacuum cleaners":"shop-vacuum-cleaners", \
			"steam mops":"shop-steam-mops","laundry accessories":"shop-laundry-accessories", \
			"cleaning products":"shop-cleaning-products","furniture":"shop-furniture", \
			"bedroom":"shop-bedroom-furniture","living room":"shop-living-room-furniture", \
			"home office":"shop-home-office-furniture","dining":"shop-kitchen-dining-furniture", \
			"hallway & entry":"shop-hallway-entry-furniture","outdoor & garden":"shop-outdoor-garden", \
			"lawn & garden":"shop-lawn-garden","grills & entertaining":"shop-grills-outdoor-entertaining", \
			"outdoor decor":"shop-outdoor-decor","outdoor furniture":"shop-outdoor-furniture", \
			"home improvement":"shop-home-improvement","power tools":"shop-power-tools", \
			"hand tools":"shop-hand-tools","flashlights":"shop-flashlights", \
			"electrical":"shop-electrical","safety & security":"shop-safety-security", \
			"lighting":"shop-lighting","home decor":"shop-home-decor", \
			"bedding":"shop-bedding","bath":"shop-bath", \
			"storage & organisation":"shop-storage-organisation","pet supplies":"shop-pet-supplies", \
			"stationery":"shop-stationery"}}
		elif c=="healthbeauty":
			category = {"health & beauty":{"skin care":"shop-face","treatments & serum":"shop-skincare-face-treatments-serums", \
			"moisturisers & cream":"shop-skincare-moisturizers-cream","toners":"shop-toner-mists", \
			"face cleansers":"shop-face-cleanser","face masks":"shop-skincare-face-mask-packs", \
			"sun protection":"shop-sunscreen-aftersun-lotion","personal care":"shop-health-personal-care", \
			"hair care":"shop-hair-care","bath & body":"shop-bath-body", \
			"hand & foot care":"shop-hand-foot-care", \
			"makeup":"shop-makeup","face":"shop-makeup-face", \
			"eyes":"shop-eyes-makeup","lips":"shop-lips", \
			"sets & palettes":"shop-makeup-kits-sets-palettes","brushes & accessories":"shop-makeup-accessories", \
			"nail care":"shop-makeup-nails","fragrances":"shop-fragrances", \
			"women":"shop-women-body-spray","men":"shop-men-eau-de-toilette", \
			"beauty tools":"shop-health-beauty-tools","hair styling":"shop-hair-styling-appliances", \
			"skin care & tools":"shop-health-beauty-skin-care-tools","slimmers & massagers":"shop-health-beauty-slimming-devices", \
			"hair removal":"shop-hair-removal-appliances","men's care":"shop-mens-care", \
			"shaving":"shop-shaving","body & skin care":"shop-body-skin-care", \
			"hair care":"shop-mens-hair-care","food supplements":"shop-food-supplements-weight-management", \
			"well being":"shop-well-being","weight management":"shop-weight-loss", \
			"beauty supplements":"shop-beauty-supplements","whitening supplements":"shop-whitening-supplements", \
			"sports nutrition":"shop-sports-nutrition","medical supplies":"shop-medical-equipment", \
			"health monitors":"shop-health-monitors","scales & body fat analysers":"shop-scale-body-fat-analyzers", \
			"personal pleasures":"shop-sexual-wellness"}}
		elif c=="babytoys":
			category = {"baby & toys":{"diapering & potty":"shop-diapers-potties","disposable diapers":"shop-disposable-diapers", \
			"diaper bags":"shop-babies-diaper-bags","cloth diapers":"shop-cloth-diapers-and-accessories", \
			"baby gear":"shop-baby-gear","strollers":"shop-baby-strollers", \
			"car seats":"shop-car-seats","carriers":"shop-baby-carriers", \
			"nursery":"shop-nursery","health & safety":"shop-health-safety", \
			"feeding":"shop-feeding-nursing","milk formula":"shop-formula-milk-baby-food", \
			"bottle-feeding":"shop-feeding-bottle","breastfeeding":"shop-breast-feeding", \
			"baby & toddler food":"shop-baby-food","clothing & accessories":"shop-baby-clothing", \
			"baby girls":"shop-baby-girls-clothing-and-accessories","baby boys":"shop-baby-boys-clothing-and-accessories", \
			"new born":"shop-new-born-baby-clothing","maternity care":"shop-maternity-care", \
			"pacifiers & accessories":"shop-pacifiers-and-accessories","sports & outdoor play":"shop-sports-and-outdoor-play", \
			"outdoor toys":"shop-outdoor-toys","play tents & tunnels":"shop-kids-tents", \
			"learning & education":"shop-educational-toys","basic & life skills toys":"shop-basic-life-skills-toys", \
			"musical instruments":"shop-musical-toys","action figures & collectibles":"shop-action-figures-collectibles", \
			"pretend play":"shop-pretend-play","puzzle":"shop-puzzles", \
			"remote control & play vehicles":"shop-remote-control-toys-and-play-vehicles","drones & accessories":"shop-drones-and-accessories", \
			"rc vehicles & batteries":"shop-remote-control-toys","baby & toddler toys":"shop-baby-toys", \
			"activity gym & playmats":"shop-activity-gym-playmats","early learning":"shop-early-learning-baby-toys", \
			"dolls & accessories":"shop-dolls-doll-houses","arts & crafts for kids":"shop-arts-craft", \
			"stuffed toys":"shop-stuffed-toys","blocks & building":"shop-blocks-building-toys"}}				
		elif c=="sportstravel":
			category = {"sports & travel":{"exercise & fitness":"shop-exercise-fitness","cardio equipment":"shop-cardio-training-equipment", \
			"strength equipment":"shop-strength-training-equipment","fitness accessories":"shop-fitness-accessories", \
			"weight":"shop-weight-training","yoga":"shop-yoga", \
			"pilates":"shop-pilates","boxing, martial arts & mma":"shop-boxing-martial-arts-mma", \
			"team sports":"shop-team-sports","football":"shop-football", \
			"basketball":"shop-basketball","volleyball":"shop-volleyball", \
			"outdoor recreation":"shop-outdoor-recreation","cycling":"shop-cycling", \
			"camping & hiking":"shop-camping-hiking","fishing":"shop-fishing", \
			"scooters":"shop-scooters-ride-ons","inline & roller skating":"shop-inline-roller skates", \
			"skateboards":"skateboards","swimming":"shop-swimming", \
			"diving & snorkeling":"shop-diving-snorkeling","racquets sports":"shop-racquet-sports", \
			"badminton":"shop-badminton","table tennis":"shop-table-tennis", \
			"tennis":"shop-tennis","men":"shop-shoes-clothing-men", \
			"sports shoes":"shop-sports-shoes-men","sports clothing":"shop-sports-clothing-men", \
			"sports bags":"shop-sports-bag","women":"shop-shoes-clothing-women", \
			"sports shoes":"shop-sports-shoes-women","sports clothing":"shop-sports-clothing-women", \
			"sports bags":"shop-sports-bag","accessories":"shop-sports-accessories", \
			"protective goggles":"shop-sports-protective-goggles","sports water bottles":"shop-sports-water-bottles", \
			"performance & gps trackers":"shop-performance-gps-trackers","luggage":"shop-luggage", \
			"suitcases":"shop-suitcases","luggage sets":"shop-luggage-sets", \
			"backpacks":"shop-bags-backpacks","laptop bags & cases":"shop-laptop-bags-cases", \
			"laptop backpacks":"shop-laptop-backpacks","shoulder bags":"shop-laptop-messenger-bags", \
			"laptop cases":"shop-laptop-cases","travel bags":"shop-bag", \
			"kids' bags & luggage":"shop-kids-luggage","travel accessories":"shop-travel-accessories"}}
		elif c=="motormusic":
			category = {"motors, music & more":{"automotive":"shop-automotive","motorcycle & atv":"shop-motorcycle-atv", \
			"auto electronics":"shop-auto-electronics","interior accessories":"shop-car-interior-accessories", \
			"exterior accessories":"shop-car-exterior-accessories","car care":"shop-car-care", \
			"oils & fluids":"shop-automotive-oil-fluids","paint, body, and trim":"shop-automotive-paint-body-trim", \
			"replacement parts":"shop-replacement-parts","performance parts":"shop-performance-parts-accessories", \
			"auto tires & wheels":"shop-automotive-wheels-tires","truck accessories":"shop-truck-acccessories", \
			"tools & equipment":"shop-automotive-tools-equipments","gps":"shop-gps-navigation", \
			"gadgets":"shop-gadgets-automotive","other electronic gadgets":"shop-other-electronic-gadgets", \
			"home gadgets":"shop-home-gadgets","drinking and smoking":"shop-drinking-smoking-accessories", \
			"motorcycle":"shop-motorcycle","moto tires and wheels":"shop-motorcycle-tires-wheels", \
			"musical instruments":"shop-musical-instruments","guitars":"shop-guitars", \
			"keyboards & pianos":"shop-keyboards-pianos","drums & percussion":"shop-drums-percussion", \
			"dj, karaoke, and electronic music":"shop-dj-karaoke-electronic-music","band & orchestra":"shop-band-orchestra", \
			"instrument accessories":"shop-instrument-accessories","books":"shop-books", \
			"magazines":"shop-media-games-music-magazines","music":"shop-music", \
			"movies":"shop-movies","tv series":"shop-tv-series", \
			"candy & chocolate":"shop-candy-chocolate","canned, dry & packaged foods":"shop-canned-dry-packaged-foods", \
			"beverages":"shop-beverages","breakfast":"shop-breakfast", \
			"baking & cooking":"shop-baking-cooking","wine & spirits":"shop-wines-spirits", \
			"dogs":"shop-dogs","food":"shop-dog-food", \
			"grooming supplies":"shop-dog-grooming-supplies","beds & accessories":"shop-beds-accessories-dogs", \
			"clean up & toilet":"shop-dog-clean-up-toilets","cats":"shop-cats", \
			"food":"shop-cat-food","foods & accessories":"shop-cat-beds-bowls", \
			"litter & toilet":"shop-cat-clean-up-toilets","grooming supplies":"shop-cat-grooming-supplies", \
			"bird, fish & small animals":"shop-birds-fish-small-animals","aquariums & accessories":"shop-aquariums-accessories", \
		    "beds & accessories":"shop-birds-fish-accessories-small-animals-beds","pet care":"shop-birds-fish-small-animals-pet-care"}}
				

		self.myfile = open(c + ".csv", 'w', newline='')
		writer = csv.DictWriter(self.myfile, fieldnames = ["url", "product_name", "product_header", "product_category", "product_price", "product_sale", "product_old", "installment", "rating", "product_image"], delimiter=',')
		writer.writeheader()
		for k,v in category.items():
			for key,val in v.items():
				self.lazada_scrape(k,key,val)

		print("Done Scraping")
