from tkinter import *

menu = Tk()
menu.title("Fun Times Restaurant")
menu.geometry("1920x1080")
menu.configure(bg="pink")

def doDole(): #pack all assets of dole whip frame
    DWS.pack()
    DWSmall.pack(anchor = W, side= LEFT)
    DWMedium.pack(anchor = W, side= LEFT)
    DWLarge.pack(anchor = W, side= LEFT)
    DWAmnt.pack()

def doChurro(): #pack all assets of churro frame
    CAmnt.pack()

def doCott(): #pack all assets of cotton candy frame
    CCAmnt.pack()

def doHam():#pack all assets of hamburger frame
    HAmnt.pack()

def doPop(): #pack all assets of popcorn frame
    PWS.pack()
    PSmall.pack(anchor = W, side= LEFT)
    PMedium.pack(anchor = W, side= LEFT)
    PLarge.pack(anchor = W, side= LEFT)
    PAmnt.pack()

def doPretz():#pack all assets of pretzel frame
    SPAmnt.pack()

def placeOrder(): 
    dwamnt = int(DWAmnt.get()) #convert all spinbox amounts to integers
    camnt = int(CAmnt.get())
    ccamnt = int(CCAmnt.get())
    hamnt = int(HAmnt.get())
    pamnt = int(PAmnt.get())
    spamnt = int(SPAmnt.get())
    receipt= "" #create empty string to add receipt values to
    total = 0 #create total to add item totals to
    if dwamnt > 0: #runs code below if the amount of product is greater than 0
        if DWSize.get() == "S": #use radiobuttons to determine the size and price of selected item
            dwprice = 3.25
        elif DWSize.get() == "M":
            dwprice = 4.25
        elif DWSize.get() == "L":
            dwprice = 5.25
        dwtotal = round(dwprice * dwamnt, 2) #keep total in 2 places, calculate total price of items
        dwrcpt = str(dwamnt) + "x " + DWSize.get()+ " Dole Whip(s):   $" + str(dwtotal)#add all elements into a string that shows amount, size of product, and total price of product(s) bought
        receipt += (dwrcpt + "\n") #add string to receipt
        total += dwtotal
    if camnt > 0:    
        cprice = 3.25
        ctotal = round(cprice * camnt, 2)
        crcpt = str(camnt) + "x " + "Churro(s):   $" + str(ctotal)
        receipt += (crcpt + "\n")
        total += ctotal
    if ccamnt > 0:
        ccprice = 2.75
        cctotal = round(ccprice * ccamnt, 2)
        ccrcpt = str(ccamnt) + "x " + "Cotton Candy:   $" + str(cctotal)
        receipt += (ccrcpt + "\n")
        total += cctotal
    if hamnt > 0: 
        hprice = 9.25
        htotal = round(hprice * hamnt, 2)
        hrcpt = str(hamnt) + "x " + "Hamburger(s):   $" + str(htotal)
        receipt += hrcpt + "\n"
        total += htotal
    if pamnt > 0:
        if PSize.get() == "S":
            pprice = 2.75
        elif PSize.get() == "M":
            pprice = 3.75
        elif PSize.get() == "L":
            pprice = 4.75
        ptotal = round(pprice * pamnt, 2)
        prcpt = str(pamnt) + "x " + PSize.get()+ " Popcorn(s):   $" + str(ptotal)
        receipt += (prcpt + "\n")
        total += ptotal
    if spamnt > 0: 
        spprice = 3.25
        sptotal = round(spprice * spamnt, 2)
        sprcpt = str(spamnt) + "x " + "Soft Pretzel(s):   $" + str(sptotal)
        receipt += (sprcpt + "\n") 
        total += sptotal

    receipt += "Total:       $" + str(total)
    recpt.config(text= receipt)

def doButton1(): # when image is selected, show the picture and price of item
    #label_1.config(image=img01_size_2)
    label_1.config(image=img01)
    label_2.config(text="Churro:  $3.25")

def doButton2():
    label_1.config(image=img02)
    label_2.config(text="Pretzel:  $3.25")

def doButton3():
    label_1.config(image=img03)
    label_2.config(text="Hamburger:  $9.25")

def doButton4():
    label_1.config(image=img04)
    label_2.config(text="Cotton Candy:  $2.75")

def doButton5():
    label_1.config(image=img05)
    label_2.config(text="Popcorn:  Small-$2.75  Medium-$3.75  Large-$4.75")

def doButton6():
    label_1.config(image=img06)
    label_2.config(text="Dole Whip:  Small-$3.25  Medium-$4.25  Large-$5.25")

    
   

OrderMenu = Frame(menu, bg= "pink") #frame to hold the ordering part of the gui
OrderPics = Frame(menu, bg= "pink") #frame to hold the pictures and prices of the menu
DoleWhip  = Frame(OrderMenu, bg= "pink") #frame for dole whip ordering
DWS = Frame(DoleWhip, bg= "pink") #frame for dole whip sizes
Churro = Frame(OrderMenu, bg= "pink") 
Pretzel = Frame(OrderMenu, bg= "pink")
Hamburger = Frame(OrderMenu, bg= "pink")
Popcorn = Frame(OrderMenu, bg= "pink")
PWS = Frame(Popcorn, bg= "pink") #frame for popcorn sizes
CottCandy = Frame(OrderMenu, bg= "pink")

DWSize = StringVar() #var used for the dole whip sizes
DWSize.set(0) #keeps size unselected at start
PSize = StringVar() #var used for popcorn sizes
PSize.set(0)
recpt = Label(OrderMenu, bg= "pink") #label to display the receipt of the order

DWAmnt = Spinbox(DoleWhip, from_ = 0, to = 10) #spinboxes for amount of items user wishes to order
CAmnt = Spinbox(Churro, from_ = 0, to = 10 )
HAmnt = Spinbox(Hamburger, from_ = 0, to = 10 )
CCAmnt = Spinbox(CottCandy, from_ = 0, to = 10 )
PAmnt = Spinbox(Popcorn, from_ = 0, to = 10 )
SPAmnt = Spinbox(Pretzel, from_ = 0, to = 10 )

PSmall = Radiobutton(PWS, text= "Small", var= PSize, value= "S") #radiobuttons for size selection of DW and popcorn
PMedium = Radiobutton(PWS, text= "Medium", var= PSize, value= "M")
PLarge = Radiobutton(PWS, text= "Large", var= PSize, value= "L")
DWSmall = Radiobutton(DWS, text= "Small", var= DWSize, value= "S")
DWMedium = Radiobutton(DWS, text= "Medium", var= DWSize, value= "M")
DWLarge = Radiobutton(DWS, text= "Large", var= DWSize, value= "L")

dwbut = Button(DoleWhip, text= "Dole Whip", command= doDole) #buttons to display the rest of the frame and let user choose what they will order
cbut = Button(Churro, text= "Churro", command= doChurro)
pbut = Button(Popcorn, text= "Popcorn", command= doPop)
hbut = Button(Hamburger, text= "Hamburger", command= doHam)
spbut = Button(Pretzel, text= "Soft Pretzel", command= doPretz)
ccbut = Button(CottCandy, text= "Cotton Candy", command= doCott)
orderbut = Button(OrderMenu, text= "Place your Order", command= placeOrder)

img01 = PhotoImage(file="Churro.png") #images of food to be displayed on menu
img01_thumb = img01.subsample(4)

img02 = PhotoImage(file="Pretzel.png")
img02_thumb = img02.subsample(4)

img03 = PhotoImage(file="Hamburger.png")
img03_thumb = img03.subsample(4)

img04 = PhotoImage(file="CottonCandy.png")
img04_thumb = img04.subsample(4)

img05 = PhotoImage(file="Popcorn.png")
img05_thumb = img05.subsample(4)

img06 = PhotoImage(file="DoleWhip.png",)
img06_thumb = img06.subsample(4)

label_1 = Label(OrderPics, text="Food Items", bg= "pink")
label_1.grid(row=1, rowspan=6, column=1)

label_2 = Label(OrderPics, text="Select the Food Item You Would Like to See", bg= "pink")
label_2.grid(row=0, column=1)

MyButton1 = Button(OrderPics, image=img01_thumb, text="b1", width=100, height=100, command = lambda: doButton1())#buttons that will display the image of the food and the price
MyButton1.grid(row=1, column=0)

MyButton1 = Button(OrderPics, image=img02_thumb, text="b2", width=100, height=100, command = lambda: doButton2())
MyButton1.grid(row=2, column=0)

MyButton1 = Button(OrderPics, image=img03_thumb, text="b3", width=100, height=100, command = lambda: doButton3())
MyButton1.grid(row=3, column=0)

MyButton1 = Button(OrderPics, image=img04_thumb, text="b4", width=100, height=100, command = lambda: doButton4())
MyButton1.grid(row=4, column=0)

MyButton1 = Button(OrderPics, image=img05_thumb, text="b5", width=100, height=100, command = lambda: doButton5())
MyButton1.grid(row=5, column=0)

MyButton1 = Button(OrderPics, image=img06_thumb, text="b6", width=100, height=100, command = lambda: doButton6())
MyButton1.grid(row=6, column=0)

OrderPics.pack(side= LEFT) #packing each element of the GUI
OrderMenu.pack(side=RIGHT)
DoleWhip.pack()
dwbut.pack()
Churro.pack()
cbut.pack()
CottCandy.pack()
ccbut.pack()
Hamburger.pack()
hbut.pack()
Popcorn.pack()
pbut.pack()
Pretzel.pack()
spbut.pack()
orderbut.pack()
recpt.pack()
menu.mainloop()