from tkinter import Tk,Button,Label
root=Tk()
root.title("calculator")
var=""
def cal(data):
    global var
    var=var+data
    l.config(text=var[-29:])
def sqrt():
    global var
    try:
        var=str((float(var)**0.5))
        l.config(text=var[-29:])
    except:
        l.config(text="INVALID")
def solution():
    global var
    try:
        var=str(eval(var))
        l.config(text=var[-29:])
    except:
        l.config(text="INVALID")
def back():  
    global var
    var=var[:-1]
    l.config(text=var[-29:])
def clear():
    global var
    var=""
    l.config(text="enter your expression")
l=Label(root,text="enter your expression",font=("algerian",20),fg="red")
b0=Button(root,text="0",width=10,height=2,command=lambda:cal("0"),bg="black",fg="red",
font=('algerian',20))
b1=Button(root,text="1",width=10,height=2,command=lambda:cal("1"),bg="black",fg="red",
font=('algerian',20))
b2=Button(root,text="2",width=10,height=2,command=lambda:cal("2"),bg="black",fg="red",
font=('algerian',20))
b3=Button(root,text="3",width=10,height=2,command=lambda:cal("3"),bg="black",fg="red",
font=('algerian',20))
b4=Button(root,text="4",width=10,height=2,command=lambda:cal("4"),bg="black",fg="red",
font=('algerian',20))
b5=Button(root,text="5",width=10,height=2,command=lambda:cal("5"),bg="black",fg="red",
font=('algerian',20))
b6=Button(root,text="6",width=10,height=2,command=lambda:cal("6"),bg="black",fg="red",
font=('algerian',20))
b7=Button(root,text="7",width=10,height=2,command=lambda:cal("7"),bg="black",fg="red",
font=('algerian',20))
b8=Button(root,text="8",width=10,height=2,command=lambda:cal("8"),bg="black",fg="red",
font=('algerian',20))
b9=Button(root,text="9",width=10,height=2,command=lambda:cal("9"),bg="black",fg="red",
font=('algerian',20))
bDot=Button(root,text=".",width=10,height=2,command=lambda:cal("."),bg="black",fg="red",
font=('algerian',20))
bAdd=Button(root,text="+",width=10,height=2,command=lambda:cal("+"),bg="black",fg="red",
font=('algerian',20))
bSub=Button(root,text="-",width=10,height=2,command=lambda:cal("-"),bg="black",fg="red",
font=('algerian',20))
bMul=Button(root,text="*",width=10,height=2,command=lambda:cal("*"),bg="black",fg="red",
font=('algerian',20))
bDiv=Button(root,text="/",width=10,height=2,command=lambda:cal("/"),bg="black",fg="red",
font=('algerian',20))
bMod=Button(root,text="%",width=10,height=2,command=lambda:cal("%"),bg="black",fg="red",
font=('algerian',20))
bSqrt=Button(root,text="Sqrt",width=10,height=2,command=sqrt,bg="black",fg="red",
font=('algerian',20))
bEqual=Button(root,text="=",width=10,height=2,command=solution,bg="orange",fg="black",
font=('algerian',20))
bClear=Button(root,text="Clear",width=10,height=2,command=clear,bg="black",fg="red",
font=('algerian',20))
bBack=Button(root,text="Back",width=10,height=2,command=back,bg="black",fg="red",
font=('algerian',20))
l.grid(row=0,column=0,columnspan=4)
b1.grid(row=1,column=1)
b2.grid(row=1,column=2)
b3.grid(row=1,column=3)
bAdd.grid(row=1,column=4)
b4.grid(row=2,column=1)
b5.grid(row=2,column=2)
b6.grid(row=2,column=3)
bSub.grid(row=2,column=4)
b7.grid(row=3,column=1)
b8.grid(row=3,column=2)
b9.grid(row=3,column=3)
bMul.grid(row=3,column=4)
bClear.grid(row=5,column=2)
b0.grid(row=4,column=2)
bDot.grid(row=4,column=3)
bDiv.grid(row=4,column=4)
bBack.grid(row=5,column=1)
bSqrt.grid(row=4,column=1)
bEqual.grid(row=5,column=3)
bMod.grid(row=5,column=4)
root.mainloop()