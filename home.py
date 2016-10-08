from tkinter import *
from webscrape.webscrape import WebScrape

def selectItem():
	categ = var.get()
	print(categ)

def callback():
	print(var.get())
	webscrape.run_lazada_scrape(var.get())

webscrape = WebScrape()
root = Tk()
root.title("Lazada WebScrape")
var = StringVar()

R1 = Radiobutton(root, text="electronics", variable=var, value="electronics", command=selectItem)
R1.pack( anchor = W )
R2 = Radiobutton(root, text="woman fashion", variable=var, value="wfashion", command=selectItem)
R2.pack( anchor = W )
R3 = Radiobutton(root, text="men fashion", variable=var, value="mfashion", command=selectItem)
R3.pack( anchor = W )
R4 = Radiobutton(root, text="home and living", variable=var, value="homeliving", command=selectItem)
R4.pack( anchor = W )
R5 = Radiobutton(root, text="health and beauty", variable=var, value="healthbeauty", command=selectItem)
R5.pack( anchor = W )
R6 = Radiobutton(root, text="baby and toys", variable=var, value="babytoys", command=selectItem)
R6.pack( anchor = W )
R7 = Radiobutton(root, text="sports and travel", variable=var, value="sportstravel", command=selectItem)
R7.pack( anchor = W )
R8 = Radiobutton(root, text="motor and music and more", variable=var, value="motormusic", command=selectItem)
R8.pack( anchor = W )

root.resizable(width=False, height=False)
root.geometry('{}x{}'.format(300, 300))

B = Button(root, text ="Scrape", command=callback)
B.pack()

R1.select()
root.mainloop()