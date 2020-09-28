from Tkinter import * 
import math
def solveEquation():
	a=float(stringHSA.get())
	b=float(stringHSB.get())
	c=float(stringHSC.get())
	if a==0:
		if b==0 and c==0:
			stringKQ.set("Vo so nghiem")
		elif b==0 and c!=0:
			stringKQ.set("Vo nghiem")
		else:
			x=round((-c/b),2)
			stringKQ.set("x = "+str(x))
	else:
		delta=b**2-4*a*c
		if delta<0:
			stringKQ.set("Vo nghiem")
		elif delta==0:
			stringKQ.set("Nghiem kep: x1 = x2 = "+str((-b/(2*a))))
		else:
			x1=round((-b-math.sqrt(delta))/(2*a),2)
			x2=round((-b+math.sqrt(delta))/(2*a),2)
			stringKQ.set("x1 = "+str(x1)+"; x2 = "+str(x2))

def continueSolve():
	stringHSA.set("")
	stringHSB.set("")
	stringHSC.set("")
	stringKQ.set("")

root=Tk()

stringHSA=StringVar()
stringHSB=StringVar()
stringHSC=StringVar()
stringKQ=StringVar()


root.title("Giai Phuong Trinh Bac 2")
root.resizable(height=True,width=True)
root.minsize(height=220,width=470)

Label(root,text="Phuong Trinh Bac Hai",fg="blue",font=("tahoma",20),justify=CENTER).grid(row=0,columnspan=2)

Label(root,text="He so a:",font=("tahoma",16)).grid(row=1,column=0)
Entry(root,width=40,font=("tahoma",12),textvariable=stringHSA).grid(row=1,column=1)

Label(root,text="He so b:",font=("tahoma",16)).grid(row=2,column=0)
Entry(root,width=40,font=("tahoma",12),textvariable=stringHSB).grid(row=2,column=1)

Label(root,text="He so c:",font=("tahoma",16)).grid(row=3,column=0)
Entry(root,width=40,font=("tahoma",12),textvariable=stringHSC).grid(row=3,column=1)

frameButton=Frame()
Button(frameButton,text="Giai",font=("tahoma",12),command=solveEquation).pack(side=LEFT)
Button(frameButton,text="Tiep",font=("tahoma",12),command=continueSolve).pack(side=LEFT)
Button(frameButton,text="Thoat",font=("tahoma",12),command=root.quit).pack(side=LEFT)
frameButton.grid(row=4,columnspan=2,)

Label(root,text="Ket qua:",font=("tahoma",16)).grid(row=5,column=0)
Entry(root,width=40,font=("tahoma",12),textvariable=stringKQ).grid(row=5,column=1)

def makecenter(root):
	root.update_idletasks()
	width = root.winfo_width()
	height = root.winfo_height()
	x = (root.winfo_screenwidth() // 2) - (width // 2)
	y = (root.winfo_screenheight() // 2) - (height // 2)
	root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
makecenter(root)

root.mainloop()