from tkinter import *
from tkinter import ttk
 
def print():
    tott = float(totText.get())
    bal=float(balText.get())
    top = Toplevel()
    top.geometry("500x500")
    top.config(bg="white")
    l = Label(top, text='---------RECIEPT----------')
    l.pack()
    l.config(bg="white")
    heading = Label(top, text="ITEM         PRICE         QUANTITY         TOTAL")
    heading.pack()
    heading.config(bg="white")
    l = Label(top, text='----------------------------------------------------------------------------------------------------------------------')
    l.pack()
    l.config(bg="white")
    for child in listBox.get_children():
        item  = (listBox.item(child, 'values')[0])
        price = float(listBox.item(child, 'values')[1])
        qty   = float(listBox.item(child, 'values')[2])
        tot   = float(listBox.item(child, 'values')[3])
        item1 = Label(top, text=f'{item}\t\t{price}\t\t{qty}\t\t{tot}')
        item1.config(bg="white")
        item1.pack()


    l = Label(top, text='----------------------------------------------------------------------------------------------------------------------')
    l.pack()
    l.config(bg="white")    
 
    tot = Label(top, text=f'Total\t{tott}')
    tot.config(bg="white")
    tot.pack()

    tot = Label(top, text=f'Balance\t{bal}')
    tot.config(bg="white")
    tot.pack()


def pay():
    totall=float(tot.cget("text"))
    pay=float(e11.get())
    bal=pay-totall
    balText.set(bal)
 
 
def show():
    tot = 0
    if (var1.get()):
        price = int(e1.get())
        qty = int(e6.get())
        tot = int(price * qty)
        tempList = [['STEAM MOMOS', e1.get(), e6.get(), tot]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        for i, (item, price, qty, tot) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(item, price, qty, tot))
 
    if (var2.get()):
        price = int(e2.get())
        qty = int(e7.get())
        tot = int(price * qty)
        tempList = [['CHOWMEIN', e2.get(), e7.get(), tot]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        for i, (item, price, qty, tot) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(item, price, qty, tot))
 
    if (var3.get()):
        price = int(e3.get())
        qty = int(e8.get())
        tot = int(price * qty)
        tempList = [['MANCHURIAN', e3.get(), e8.get(), tot]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        for i, (item, price, qty, tot) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(item, price, qty, tot))
 
    if (var4.get()):
        price = int(e4.get())
        qty = int(e9.get())
        tot = int(price * qty)
        tempList = [['VEG BURGER', e4.get(), e9.get(), tot]]
        tempList.sort(key=lambda e: e[1], reverse=True)
 
        for i, (item, price, qty, tot) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(item, price, qty, tot))
 
    if (var5.get()):
        price = int(e5.get())
        qty = int(e10.get())
        tot = int(price * qty)
        tempList = [['SPRING ROLL', e5.get(), e10.get(), tot]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        for i, (item, price, qty, tot) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(item, price, qty, tot))
 
    sum1 = 0.0
    for child in listBox.get_children():
        sum1 += float(listBox.item(child, 'values')[3])
    totText.set(sum1)
 
 
root = Tk()
   
    
root.title("Inventory System")
root.geometry("1000x600")
global e1
global e2
global e3
global e4
global totText
global balText
 
totText = StringVar()
balText = IntVar()
 
Label(root, text="BILLING SYSTEM", font="Georgia 22 bold" ,bg="green").place(x=100, y=10) 
Label(root, text="ITEM",font="Georgia").place(x=20, y=70)
Label(root, text="PRICE",font="Georgia").place(x=170, y=70)
Label(root, text="QUANTITY",font="Georgia").place(x=330, y=70)
  
var1 = IntVar()
Checkbutton(root, text="STEAM MOMOS", variable=var1).place(x=10, y=100)
 
var2 = IntVar()
Checkbutton(root, text="CHOWMEIN", variable=var2).place(x=10, y=130)
 
var3 = IntVar()
Checkbutton(root, text="MANCHURIAN", variable=var3).place(x=10, y=160)
 
var4 = IntVar()
Checkbutton(root, text="VEG BURGER", variable=var4).place(x=10, y=190)
 
var5 = IntVar()
Checkbutton(root, text="SPRING ROLL", variable=var5).place(x=10, y=220)

Label(root, text="Total", font="Garamond 18").place(x=600, y=10)
Label(root, text="Pay", font="Garamond 18").place(x=600, y=40)
Label(root, text="Balance", font="Garamond 18").place(x=600, y=70)

e1 = Entry(root)
e1.place(x=160, y=100)
 
e2 = Entry(root)
e2.place(x=160, y=130)
 
e3 = Entry(root)
e3.place(x=160, y=160)
 
e4 = Entry(root)
e4.place(x=160, y=190)
 
e5 = Entry(root)
e5.place(x=160, y=220)
 
e6 = Entry(root)
e6.place(x=320, y=100)
 
e7 = Entry(root)
e7.place(x=320, y=130)
 
e8 = Entry(root)
e8.place(x=320, y=160)
 
e9 = Entry(root)
e9.place(x=320, y=190)
 
e10 = Entry(root)
e10.place(x=320, y=220)
 
tot = Label(root, text="", font="arial 22 bold", textvariable=totText)
tot.place(x=700, y=10)

e11= Entry(root)
e11.place(x=700,y=50)

balance = Label(root, text="", font="arial 22 bold", textvariable=balText).place(x=700, y=70)

Button(root, text="Add", font="Calibri 11 bold", bg="red", command=show, height=3, width=13).place(x=10, y=250)
Button(root, text="PayNow", font="Calibri 11 bold", bg="red", command=pay, height=3, width=13).place(x=850, y=140)
Button(root, text="Print",font="Calibri 11 bold", bg="red", command=print, height=3, width=13).place(x=850, y=250)

cols = ('Item', 'Price', 'Quantity', 'Total')
listBox = ttk.Treeview(root, columns=cols, show='headings')
 
for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=330)
 
 
root.mainloop()
