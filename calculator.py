from tkinter import*
import math as m
from PIL import Image, ImageTk

root = Tk()
root.title("Calculator")
root.geometry("291x490")
root.resizable(0,0)
root.config(bg = "#000000")

def num(dig):
    old = dis.get()
    dis.delete(0,END)
    dis.insert(0,old+dig)
    return

def clear():
    dis.delete(0,END)
    return

def back():
    current = dis.get()
    length = len(current)-1
    dis.delete(length,END)

def equ():
    ans = dis.get()
    ans=eval(ans)
    dis.delete(0,END)
    dis.insert(0, ans)
def show_msg(event):
    ans = dis.get()
    ans=eval(ans)
    dis.delete(0,END)
    dis.insert(0, ans)  

def click(val):
    e = dis.get()
    if val == "√":
        ab = m.sqrt(eval(e))
        dis.delete(0,END)
        dis.insert(0, ab)
    elif val == "∛":
        ab = m.cbrt(eval(e))
        dis.delete(0,END)
        dis.insert(0, ab)
    elif val == "cos":
        ab = m.cos(m.radians(eval(e)))
        dis.delete(0,END)
        dis.insert(0, ab)
    elif val == "sin":
        ab = m.sin(m.radians(eval(e)))
        dis.delete(0,END)
        dis.insert(0, ab)
    elif val == "tan":
        ab = m.tan(m.radians(eval(e)))
        dis.delete(0,END)
        dis.insert(0, ab)
    elif val == "sec":
        ab = m.acos(m.radians(eval(e)))
        dis.delete(0,END)
        dis.insert(0, ab)
    elif val == "cosec":
        ab = m.asin(m.radians(eval(e)))
        dis.delete(0,END)
        dis.insert(0, ab)
    elif val == "cot":
        ab = m.atan(m.radians(eval(e)))
        dis.delete(0,END)
        dis.insert(0, ab)
    elif val == "fac":
        ab = m.factorial(eval(e))
        dis.delete(0,END)
        dis.insert(0, ab)

    elif val == 'x\u00B2':
        ab = eval(e) **2
        dis.delete(0,END)
        dis.insert(0, ab) 
    elif val == 'x\u00B3':
        ab = eval(e) **3
        dis.delete(0,END)
        dis.insert(0, ab) 
    elif val == 'x\u00B4':
        ab = eval(e) **4
        dis.delete(0,END)
        dis.insert(0, ab) 
    elif val == 'x\u00B4':
        ab = eval(e) **4
        dis.delete(0,END)
        dis.insert(0, ab) 
    elif val == "π":
        ab = 3.14159
        ab = str(ab)
        dis.delete(0,END)
        dis.insert(0, ab)
    elif val == "2π":
        ab = 2 * 3.14159
        ab = str(ab)
        dis.delete(0,END)
        dis.insert(0, ab)
    




    
    

dis = Entry(root  , font = ("verdana 24 "),borderwidth=5,width=14,bg= "#3d3d3d",fg = "#0000ff")
dis.grid(row = 0,column=0,columnspan=80)

btn1 = Button(root,text=1,bg="#6b6b6b",fg="#7eb7ff",width =4,height=2,font = ("verdana 16 bold"),activebackground="gray",command=lambda: num("1"))
btn1.grid(row = 1,column = 0)
btn1.config(font=("verdana" , 14))

btn2 = Button(root,text=2,bg="#6b6b6b",fg="#7eb7ff",width =4,height=2,font = ("verdana 16 bold"),activebackground="gray",command=lambda: num("2"))
btn2.grid(row = 1,column = 1)
btn2.config(font=("verdana" , 14))

btn3 = Button(root,text=3,bg="#6b6b6b",fg="#7eb7ff",width =4,height=2,font = ("verdana 16 bold"),activebackground="gray",command=lambda: num("3"))
btn3.grid(row = 1,column = 2)
btn3.config(font=("verdana" , 14))

btnpl = Button(root,text="+",bg="#602000",fg="#7eb7ff",width =4,height=2,font = ("verdana 16 bold"),activebackground="gray",command=lambda: num("+"))
btnpl.grid(row = 1,column = 3)
btnpl.config(font=("verdana" , 14))

btn4 = Button(root,text=4,bg="#6b6b6b",fg="#7eb7ff",width =4,height=2,font = ("verdana 16 bold"),activebackground="gray",command=lambda: num("4"))
btn4.grid(row = 2,column = 0)
btn4.config(font=("verdana" , 14))

btn5 = Button(root,text=5,bg="#6b6b6b",fg="#7eb7ff",width =4,height=2,font = ("verdana 16 bold"),activebackground="gray",command=lambda: num("5"))
btn5.grid(row = 2,column = 1)
btn5.config(font=("verdana" , 14))

btn6 = Button(root,text=6,bg="#6b6b6b",fg="#7eb7ff",width =4,height=2,font = ("verdana 16 bold"),activebackground="gray",command=lambda: num("6"))
btn6.grid(row = 2,column = 2)
btn6.config(font=("verdana" , 14))

btnmin = Button(root,text="-",bg="#602000",fg="#7eb7ff",width =4,height=2,font = ("verdana 16 bold"),activebackground="gray",command=lambda: num("-"))
btnmin.grid(row = 2,column = 3)
btnmin.config(font=("verdana" , 14))

btn7 = Button(root,text=7,bg="#6b6b6b",fg="#7eb7ff",width =4,height=2,font = ("verdana 16 bold"),activebackground="gray",command=lambda: num("7"))
btn7.grid(row = 3,column = 0)
btn7.config(font=("verdana" , 14))

btn8 = Button(root,text=8,bg="#6b6b6b",fg="#7eb7ff",width =4,height=2,font = ("verdana 16 bold"),activebackground="gray",command=lambda: num("8"))
btn8.grid(row = 3,column = 1)
btn8.config(font=("verdana" , 14))

btn9 = Button(root,text=9,bg="#6b6b6b",fg="#7eb7ff",width =4,height=2,font = ("verdana 16 bold"),activebackground="gray",command=lambda: num("9"))
btn9.grid(row = 3,column = 2)
btn9.config(font=("verdana" , 14))

btndiv = Button(root,text="÷",bg="#602000",fg="#7eb7ff",width =4,height=2,font = ("verdana 16 bold"),activebackground="gray",command=lambda: num("/"))
btndiv.grid(row = 3,column = 3)
btndiv.config(font=("verdana" , 14))

btnp4 = Button(root,text="x⁴",bg="#287d00",fg="#7eb7ff",width =4,height=2,font = ("verdana 16 bold"),activebackground="gray",command=lambda:click("x\u00B4"))
btnp4.grid(row = 5,column = 4)
btnp4.config(font=("verdana" , 14))

btn0 = Button(root,text=0,bg="#6b6b6b",fg="#7eb7ff",width =4,height=2,font = ("verdana 16 bold"),activebackground="gray",command=lambda: num("0"))
btn0.grid(row = 4,column = 1)
btn0.config(font=("verdana" , 14))

btnpoi = Button(root,text=".",bg="#7b0000",fg="#7eb7ff",width =4,height=2,font = ("verdana 16 bold"),activebackground="gray",command=lambda: num("."))
btnpoi.grid(row = 4,column = 2)
btnpoi.config(font=("verdana" , 14))

btnmul = Button(root,text="X",bg="#602000",fg="#7eb7ff",width =4,height=2,font = ("verdana 16 bold"),activebackground="gray",command=lambda: num("*"))
btnmul.grid(row = 4,column = 3)
btnmul.config(font=("verdana" , 14))

btnp2 = Button(root,text="x²",bg="#287d00",fg="#7eb7ff",width =4,height=2,font = ("verdana 16 bold"),activebackground="gray",command=lambda:click("x\u00B2"))
btnp2.grid(row = 5,column = 0)
btnp2.config(font=("verdana" , 14))

btnp3 = Button(root,text="x³",bg="#287d00",fg="#7eb7ff",width =4,height=2,font = ("verdana 16 bold"),activebackground="gray",command=lambda:click("x\u00B3"))
btnp3.grid(row = 5,column = 1)
btnp3.config(font=("verdana" , 14))

btnr2 = Button(root,text="√",bg="#287d00",fg="#7eb7ff",width =4,height=2,font = ("verdana 16 bold"),activebackground="gray",command=lambda:click("√"))
btnr2.grid(row = 5,column = 2)
btnr2.config(font=("verdana" , 14))

btnr3 = Button(root,text="∛",bg="#287d00",fg="#7eb7ff",width =4,height=2,font = ("verdana 16 bold"),activebackground="gray",command=lambda:click("∛"))
btnr3.grid(row = 5,column = 3)
btnr3.config(font=("verdana" , 14))

btnfactorial = Button(root,text="!",bg="#7b0000",fg="#7eb7ff",width =4,height=2,font = ("verdana 16 bold"),activebackground="gray",command=lambda:click("fac"))
btnfactorial.grid(row = 4,column = 0)
btnfactorial.config(font=("verdana" , 14))

btnsi = Button(root,text="sin\n(x)",bg="#770079",fg="#7eb7ff",width =4,height=2,font = ("verdana 4 bold"),activebackground="gray",command=lambda:click("sin"))
btnsi.grid(row = 6,column = 0)
btnsi.config(font=("verdana" , 14))

btnco = Button(root,text="cos\n(x)",bg="#770079",fg="#7eb7ff",width =4,height=2,font = ("verdana 4 bold"),activebackground="gray",command=lambda:click("cos"))
btnco.grid(row = 6,column = 1)
btnco.config(font=("verdana" , 14))

btnta = Button(root,text="tan\n(x)",bg="#770079",fg="#7eb7ff",width =4,height=2,font = ("verdana 4 "),activebackground="gray",command=lambda:click("tan"))
btnta.grid(row = 6,column = 2)
btnta.config(font=("verdana" , 14))

btnps = Button(root,text="(",bg="#00164d",fg="#7eb7ff",width =4,height=2,font = ("verdana 1 "),activebackground="gray",command=lambda: num("("))
btnps.grid(row = 6,column = 3)
btnps.config(font=("verdana" , 14))

btnpc = Button(root,text=")",bg="#00164d",fg="#7eb7ff",width =4,height=2,font = ("verdana 1"),activebackground="gray",command=lambda: num(")"))
btnpc.grid(row = 6,column = 4)
btnpc.config(font=("verdana" , 14))

btnC = Button(root,text="C",bg="#00967f",fg="red",width =4,height=2,font = ("verdana 1 "),activebackground="gray",command=clear)
btnC.grid(row = 1,column = 4)
btnC.config(font=("verdana" , 14))

btnX = Button(root,text="X",bg="#00967f",fg="red",width =4,height=2,font = ("verdana 1"),activebackground="gray",command=back)
btnX.grid(row = 2,column = 4)
btnX.config(font=("verdana" , 14))

btneq = Button(root,text="=",bg="#b80000",fg="#0000ff",width =4,height=5,font = ("verdana 70 bold"),activebackground="gray",command = equ)
btneq.place(x = 232,y = 171)
btneq.config(font=("verdana" , 14))

btncosec = Button(root,text="cosec\n(x)",bg="#770079",fg="#7eb7ff",width =4,height=2,font = ("verdana 1 "),activebackground="gray",command=lambda:click("cosec"))
btncosec.grid(row = 7,column = 0)
btncosec.config(font=("verdana" , 14))

btnsec = Button(root,text="sec\n(x)",bg="#770079",fg="#7eb7ff",width =4,height=2,font = ("verdana 4 bold"),activebackground="gray",command=lambda:click("sec"))
btnsec.grid(row = 7,column = 1)
btnsec.config(font=("verdana" , 14))

btncot = Button(root,text="cot\n(x)",bg="#770079",fg="#7eb7ff",width =4,height=2,font = ("verdana 4 "),activebackground="gray",command=lambda:click("cot"))
btncot.grid(row = 7,column = 2)
btncot.config(font=("verdana" , 14))

btnpi = Button(root,text="π",bg="#00651c",fg="#7eb7ff",width =4,height=2,font = ("verdana 1 "),activebackground="gray",command=lambda:click("π"))
btnpi.grid(row = 7,column = 3)
btnpi.config(font=("verdana" , 14))

btnper = Button(root,text="2π",bg="#00651c",fg="#7eb7ff",width =4,height=2,font = ("verdana 1"),activebackground="gray",command=lambda:click("2π"))
btnper.grid(row = 7,column = 4)
btnper.config(font=("verdana" , 14))

root.bind('<Return>', show_msg) 
root.mainloop()
