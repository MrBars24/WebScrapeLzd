import tkinter as tk
from webscrape.webscrape import WebScrape

class MainFrame:
    def __init__(self, master):
    	self.master = master
    	self.frame = tk.Frame(self.master)
    	self.btn1 = tk.Button(self.frame, text="Electronics", 
                                command= lambda: self.new_window("electronics"))
    	self.btn2 = tk.Button(self.frame, text="woman fashion", 
                                command= lambda: self.new_window("wfashion"))
    	self.btn3 = tk.Button(self.frame, text="men fashion", 
                                command= lambda: self.new_window("mfashion"))
    	self.btn4 = tk.Button(self.frame, text="home & living", 
                                command= lambda: self.new_window("homeliving"))
    	self.btn5 = tk.Button(self.frame, text="health & beauty", 
                                command= lambda: self.new_window("healthbeauty"))
    	self.btn6 = tk.Button(self.frame, text="baby & toys", 
                                command= lambda: self.new_window("babytoys"))
    	self.btn7 = tk.Button(self.frame, text="sports & travel", 
                                command= lambda: self.new_window("sportstravel"))
    	self.btn8 = tk.Button(self.frame, text="motor,music,more", 
                                command= lambda: self.new_window("motormusic"))
    	self.btn1.pack(side="top", pady=5)
    	self.btn2.pack(side="top", pady=5)
    	self.btn3.pack(side="top", pady=5)
    	self.btn4.pack(side="top", pady=5)
    	self.btn5.pack(side="top", pady=5)
    	self.btn6.pack(side="top", pady=5)
    	self.btn7.pack(side="top", pady=5)
    	self.btn8.pack(side="top", pady=5)
    	self.frame.pack()
    def new_window(self,category):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.resizable(width=False, height=False)
        if category=="electronics":
            self.app = ListFrame(self.newWindow, "electronics", ["mobiles","tablets","accessories","power banks","phone cases", \
            	"tablet accessories","screen protectors","batteries & chargers","cables & docks","mobile accessories","parts & tools","selfie sticks","laptops", \
				"2-in-1s","gaming","netbooks","ultrabooks","macbooks","computers","storage","computer components","computer accessories", \
				"printers & accessories","network components","sports & action cameras","point & shoot cameras","dslrs","mirrorless cameras", \
				"drones","security & gadget cameras","instant cameras","camera accessories","memory cards","monopods & tripods","camera bags & cases", \
				"action camera accessories","televisions","headphones & headsets","portable speakers","home & audio theater","audio players", \
				"video","projectors","streaming media players","gaming","playstation","xbox","nintendo","wearable tech","smartwatches","activity & fitness trackers","vr headsets","smart trackers"])
        if category == "wfashion":
        	self.app = ListFrame(self.newWindow, "women's fashion", ["clothing","dresses","t-shirts & tops","jackets & coats","blouses & shirts","pants & shorts", \
				"skirts","jeans","lingerie & nightwear","muslim wear","swim wear","accessories","bags","tote bags","shoulder bags","top handle bags", \
				"cross body bags","satchels","sling bags","backpacks","clutches","wallets","eyewear","sunglasses","eyeglasses","shoes","sneakers","flat shoes", \
				"heels","boots","sandals","flip flops","jewellery","bracelets & bangles","necklaces & pendants","rings", \
				"earrings","jewellery sets","watches","fashion","business","casual","sports","buying guide", \
				"shoes","bags","watches","accessories"])
        if category == "mfashion":
        	self.app = ListFrame(self.newWindow, "men's fashion", ["clothing","jacket & coats","t-shirts","pants & shorts","jeans","shirts", \
				"sweaters & cardigans","suits","uderwear & socks","swim wear","accessories","bags",
				"shoulder bags","sling bags","messenger bags","satchels","backpacks","wallets", \
				"eyewear","sunglasses","eyeglasses","shoes","sneakers","flat shoes","formal shoes","sandals", \
				"boots","jewellery","bracelets","necklaces & pendants","rings","earrings","shirt accessories","watches", \
				"business","casual","fashion","sports","boys fashion","clothing","shoes","bags","watches","accessories"])
        if category == "homeliving":
        	self.app = ListFrame(self.newWindow, "home & living", ["small kitchen appliances","food preparation","juicers","electric grills","rice cookers & steamers","coffee machines & accessories","water dispensers","kettles & thermopots","garment care","irons", \
				"sewing machines","garment steamers","large appliances","refrigerators","washers & dryers","microwave & ovens", \
				"cooktops","freezers","ice makers","cooling & heating","air conditioners","air coolers", \
				"fans","air purifiers & dehumidifiers","water heaters","kitchen & dining", "cookware","bakeware", \
				"cooking knives","kitchen tools","tableware","kitchen storage","house keeping","vacuum cleaners","steam mops","laundry accessories","cleaning products","furniture", \
				"bedroom","living room","home office","dining","hallway & entry","outdoor & garden", \
				"lawn & garden","grills & entertaining","outdoor decor","outdoor furniture","home improvement","power tools", \
				"hand tools","flashlights","electrical","safety & security","lighting","home decor","bedding","bath", \
				"storage & organisation","pet supplies","stationery"])
        if category == "healthbeauty":
        	self.app = ListFrame(self.newWindow, "health & beauty", ["skin care","treatments & serum","moisturisers & cream","toners","face cleansers","face masks","sun protection","personal care", \
				"hair care","bath & body","hand & foot care","makeup","face","eyes","lips","sets & palettes","brushes & accessories", \
				"nail care","fragrances","women","men","beauty tools","hair styling","skin care & tools","slimmers & massagers", \
				"hair removal","men's care","shaving","body & skin care","hair care","food supplements","well being","weight management", \
				"beauty supplements","whitening supplements","sports nutrition","medical supplies","health monitors","scales & body fat analysers","personal pleasures"])
        if category == "babytoys":
        	self.app = ListFrame(self.newWindow, "baby & toys", ["diapering & potty","disposable diapers","diaper bags","cloth diapers","baby gear","strollers","car seats","carriers", \
				"nursery","health & safety","feeding","milk formula","bottle-feeding","breastfeeding","baby & toddler food","clothing & accessories","baby girls","baby boys","new born","maternity care","pacifiers & accessories","sports & outdoor play", \
				"outdoor toys","play tents & tunnels","learning & education","basic & life skills toys","musical instruments","action figures & collectibles", \
				"pretend play","puzzle","remote control & play vehicles","drones & accessories","rc vehicles & batteries","baby & toddler toys", \
				"activity gym & playmats","early learning","dolls & accessories","arts & crafts for kids","stuffed toys","blocks & building"])
        if category == "sportstravel":
        	self.app = ListFrame(self.newWindow, "sports & travel", ["exercise & fitness","cardio equipment","strength equipment","fitness accessories","weight","yoga", \
				"pilates","boxing, martial arts & mma","team sports","football","basketball","volleyball", \
				"outdoor recreation","cycling","camping & hiking","fishing","scooters","inline & roller skating", \
				"skateboards","swimming","diving & snorkeling","racquets sports","badminton","table tennis", \
				"tennis","men","sports shoes","sports clothing","sports bags","women","sports shoes","sports clothing", \
				"sports bags","accessories","protective goggles","sports water bottles","performance & gps trackers","luggage", \
				"suitcases","luggage sets","backpacks","laptop bags & cases","laptop backpacks","shoulder bags", \
				"laptop cases","travel bags","kids' bags & luggage","travel accessories"])
        if category == "motormusic":
        	self.app = ListFrame(self.newWindow, "motors, music & more", ["automotive","motorcycle & atv","auto electronics","interior accessories","exterior accessories","car care", \
				"oils & fluids","paint, body, and trim","replacement parts","performance parts","auto tires & wheels","truck accessories", \
				"tools & equipment","gps","gadgets","other electronic gadgets","home gadgets","drinking and smoking", \
				"motorcycle","moto tires and wheels","musical instruments","guitars","keyboards & pianos","drums & percussion", \
				"dj, karaoke, and electronic music","band & orchestra","instrument accessories","books","magazines","music", \
				"movies","tv series","candy & chocolate","canned, dry & packaged foods","beverages","breakfast", \
				"baking & cooking","wine & spirits","dogs","food","grooming supplies","beds & accessories","clean up & toilet","cats", \
				"food","foods & accessories","litter & toilet","grooming supplies","bird, fish & small animals","aquariums & accessories", \
				"beds & accessories","pet care"])
class ListFrame:
    def __init__(self, master, categ, picks=[]):
        self.wscrape = webscrape = WebScrape()
        self.vars = []
        self.master = master
        self.frame = tk.Frame(self.master)
        row = 0
        col = 0
        count = 0
        for pick in picks:
            var = tk.StringVar()
            var.set(0)
            if(count%10==0):
            	row = 0
            	tk.Checkbutton(self.frame, text=pick, onvalue=pick, offvalue = 0, variable=var,width=20).grid(row=0, column=col, sticky="NW")
            	col+=1
            else:
                tk.Checkbutton(self.frame, text=pick, onvalue=pick, offvalue = 0, variable=var,width=20).grid(row=row+1, column=col-1, sticky="NW")
                row+=1
            self.vars.append(var)
            count+=1
        self.btnScr = tk.Button(self.master, text="Scrape", 
                                command=lambda:self.scrape_web(categ,self.vars))
        self.btnScr.pack(side="bottom",pady=5)
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()

    def find_val(self,key):
        keys = {"mobiles":"shop-mobiles","tablets":"shop-tablets", \
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
            "televisions":"shop-televisions", \
            "headphones & headsets":"shop-audio-headphones","portable speakers":"shop-portable-speakers-for-tv", \
            "home & audio theater":"shop-home-audio-theater","audio players":"shop-mp3-player-ipods", \
            "video":"shop-video","projectors":"shop-projectors-2", \
            "streaming media players":"shop-video-media-players","gaming":"shop-gaming", \
            "playstation":"shop-gaming/sony/","xbox":"shop-gaming/microsoft/", \
            "nintendo":"nintendo","wearable tech":"shop-wearable-technology", \
            "smartwatches":"shop-gadgets-smart-watches","activity & fitness trackers":"shop-fitness-trackers", \
            "vr headsets":"shop-vr","smart trackers":"shop-smart-tracking","clothing":"shop-womens-clothing","dresses":"shop-womens-dresses", \
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
            "watches":"shop-watches-girls","accessories":"shop-accessories-girls","clothing":"shop-mens-clothing","jacket & coats":"shop-mens-jackets & coats", \
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
            "accessories":"shop-accessories-boys","small kitchen appliances":"shop-small-kitchen-appliances","food preparation":"shop-food-preparation", \
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
            "stationery":"shop-stationery","skin care":"shop-face","treatments & serum":"shop-skincare-face-treatments-serums", \
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
            "personal pleasures":"shop-sexual-wellness","diapering & potty":"shop-diapers-potties","disposable diapers":"shop-disposable-diapers", \
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
            "stuffed toys":"shop-stuffed-toys","blocks & building":"shop-blocks-building-toys","exercise & fitness":"shop-exercise-fitness","cardio equipment":"shop-cardio-training-equipment", \
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
            "kids' bags & luggage":"shop-kids-luggage","travel accessories":"shop-travel-accessories","automotive":"shop-automotive","motorcycle & atv":"shop-motorcycle-atv", \
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
            "beds & accessories":"shop-birds-fish-accessories-small-animals-beds","pet care":"shop-birds-fish-small-animals-pet-care"}

        return keys[key];

    def scrape_web(self, categ, picks=[]):
    	prod_dictionary = {}
    	for pick in picks:
            if(pick.get()!="0"):
                prod_dictionary[pick.get()] = self.find_val(pick.get())
    	self.wscrape.run_lazada_scrape(categ,prod_dictionary)


def main(): 
    root = tk.Tk()
    root.title("Lazada WebScrape")
    root.resizable(width=False, height=False)
    root.geometry('{}x{}'.format(200, 300))
    app = MainFrame(root)
    root.mainloop()

if __name__ == '__main__':
    main()
