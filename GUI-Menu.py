from tkinter import *

menu = Tk()
menu.title("Fun Times Restaurant")
def doDole():
    DWS.pack()
    DWSmall.pack(anchor = W, side= LEFT)
    DWMedium.pack(anchor = W, side= LEFT)
    DWLarge.pack(anchor = W, side= LEFT)
    DWAmnt.pack()

def doChurro():
    CHAmnt.pack()

def placeOrder():
    dwamnt = int(DWAmnt.get())
    camnt = int(CHAmnt.get())
    receipt= ""
    if dwamnt > 1:
        if DWSize.get() == "S":
            dwprice = 3.25
        elif DWSize.get() == "M":
            dwprice = 4.25
        elif DWSize.get() == "L":
            dwprice = 5.25
        dwtotal = round(dwprice * dwamnt, 2)
        DWrcpt = str(dwamnt) + "x " + DWSize.get()+ " Dole Whip(s):   $" + str(dwtotal)
        receipt += DWrcpt
    if camnt > 1:    
        cprice = 3.25
        ctotal = round(cprice * camnt, 2)
        crcpt = str(camnt) + "x " + " Churro(s):   $" + str(ctotal)
        receipt += "\n" + crcpt
    total = dwtotal + ctotal
    receipt += "\nTotal:       $" + str(total)
    lab1.config(text= receipt)
        
    
   


DoleWhip  = Frame(menu)
DWS = Frame(DoleWhip)
Churro = Frame(menu)

DWSize = StringVar()
DWSize.set(0)
lab1 = Label(menu, text= "Receipt goes here:")
DWSmall = Radiobutton(DWS, text= "Small", var= DWSize, value= "S")
DWMedium = Radiobutton(DWS, text= "Medium", var= DWSize, value= "M")
DWLarge = Radiobutton(DWS, text= "Large", var= DWSize, value= "L")
DWAmnt = Spinbox(DoleWhip, from_ = 0, to = 10)
CHAmnt = Spinbox(Churro, from_ = 0, to = 10 )
but1 = Button(DoleWhip, text= "Dole Whip", command= doDole)
but2 = Button(Churro, text= "Churro", command= doChurro)
but3 = Button(menu, text= "Place your Order", command= placeOrder)

DoleWhip.pack()
but1.pack()
Churro.pack()
but2.pack()
but3.pack()
lab1.pack()
menu.mainloop()