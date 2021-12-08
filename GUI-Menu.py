from tkinter import *

menu = Tk()
menu.title("Fun Times Restaurant")
menu.geometry("1920x1080")
def doDole():
    DWS.pack()
    DWSmall.pack(anchor = W, side= LEFT)
    DWMedium.pack(anchor = W, side= LEFT)
    DWLarge.pack(anchor = W, side= LEFT)
    DWAmnt.pack()

def doChurro():
    CAmnt.pack()

def doCott():
    CCAmnt.pack()

def doHam():
    HAmnt.pack()

def doPop():
    PWS.pack()
    PSmall.pack(anchor = W, side= LEFT)
    PMedium.pack(anchor = W, side= LEFT)
    PLarge.pack(anchor = W, side= LEFT)
    PAmnt.pack()

def doPretz():
    SPAmnt.pack()

def placeOrder():
    dwamnt = int(DWAmnt.get())
    camnt = int(CAmnt.get())
    ccamnt = int(CCAmnt.get())
    hamnt = int(HAmnt.get())
    pamnt = int(PAmnt.get())
    spamnt = int(SPAmnt.get())
    receipt= ""
    total = 0
    if dwamnt >= 1:
        if DWSize.get() == "S":
            dwprice = 3.25
        elif DWSize.get() == "M":
            dwprice = 4.25
        elif DWSize.get() == "L":
            dwprice = 5.25
        dwtotal = round(dwprice * dwamnt, 2)
        dwrcpt = str(dwamnt) + "x" + DWSize.get()+ " Dole Whip(s):   $" + str(dwtotal)
        receipt += (dwrcpt + "\n")
        total += dwtotal
    if camnt >= 1:    
        cprice = 3.25
        ctotal = round(cprice * camnt, 2)
        crcpt = str(camnt) + "x" + " Churro(s):   $" + str(ctotal)
        receipt += (crcpt + "\n")
        total += ctotal
    if ccamnt >= 1:
        ccprice = 2.75
        cctotal = round(ccprice * camnt, 2)
        ccrcpt = str(ccamnt) + "x" + "Cotton Candy:   $" + str(cctotal)
        receipt += (ccrcpt + "\n")
        total += cctotal
    if hamnt >= 1: 
        hprice = 9.25
        htotal = round(hprice * hamnt, 2)
        hrcpt = str(hamnt) + "x" + "Hamburger(s):   $" + str(htotal)
        receipt += hrcpt + "\n"
        total += htotal
    if pamnt >= 1:
        if PSize.get() == "S":
            pprice = 2.75
        elif PSize.get() == "M":
            pprice = 3.75
        elif PSize.get() == "L":
            pprice = 4.75
        ptotal = round(pprice * pamnt, 2)
        prcpt = str(pamnt) + "x" + PSize.get()+ " Popcorn(s):   $" + str(ptotal)
        receipt += (prcpt + "\n")
        total += ptotal
    if spamnt >= 1: 
        spprice = 3.25
        sptotal = round(spprice * spamnt, 2)
        sprcpt = str(spamnt) + "x" + "Soft Pretzel(s):   $" + str(sptotal)
        receipt += (sprcpt + "\n") 
        total += sptotal

    receipt += "Total:       $" + str(total)
    recpt.config(text= receipt)
        
    
   


DoleWhip  = Frame(menu)
DWS = Frame(DoleWhip)
Churro = Frame(menu)
Pretzel = Frame(menu)
Hamburger = Frame(menu)
Popcorn = Frame(menu)
PWS = Frame(Popcorn)
CottCandy = Frame(menu)

DWSize = StringVar()
DWSize.set(0)
PSize = StringVar()
PSize.set(0)
recpt = Label(menu, text= "Receipt goes here:")

DWAmnt = Spinbox(DoleWhip, from_ = 0, to = 10)
CAmnt = Spinbox(Churro, from_ = 0, to = 10 )
HAmnt = Spinbox(Hamburger, from_ = 0, to = 10 )
CCAmnt = Spinbox(CottCandy, from_ = 0, to = 10 )
PAmnt = Spinbox(Popcorn, from_ = 0, to = 10 )
SPAmnt = Spinbox(Pretzel, from_ = 0, to = 10 )

PSmall = Radiobutton(PWS, text= "Small", var= PSize, value= "S")
PMedium = Radiobutton(PWS, text= "Medium", var= PSize, value= "M")
PLarge = Radiobutton(PWS, text= "Large", var= PSize, value= "L")
DWSmall = Radiobutton(DWS, text= "Small", var= DWSize, value= "S")
DWMedium = Radiobutton(DWS, text= "Medium", var= DWSize, value= "M")
DWLarge = Radiobutton(DWS, text= "Large", var= DWSize, value= "L")

dwbut = Button(DoleWhip, text= "Dole Whip", command= doDole)
cbut = Button(Churro, text= "Churro", command= doChurro)
pbut = Button(Popcorn, text= "Popcorn", command= doPop)
hbut = Button(Hamburger, text= "Hamburger", command= doHam)
spbut = Button(Pretzel, text= "Soft Pretzel", command= doPretz)
ccbut = Button(CottCandy, text= "Cotton Candy", command= doCott)
orderbut = Button(menu, text= "Place your Order", command= placeOrder)

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