'''
By Dev/AbdElrahman Youssef 
Phone : 01141870926
country : Egypt
'''
import tkinter as tk
from tkinter import messagebox

###################################################
app = tk.Tk()
app.title('Smart Calc')
app.resizable(False,False)
app.config(bg='black')
app.geometry('1000x390+150+100')
#=====================================================
#=====================================================
lbl = tk.Label(app,text='Smart Calc',bg='black',fg='gold',font=('tajawal',30,'bold')).grid(row=0,column=2)
sulbl= tk.Label(app,text='SUM +',bg='black',fg='green',font=('tajawal',20,'bold'))
sulbl.grid(row=1,column=0)
sum_lbl= tk.Label(app,text='0',bg='black',fg='white',font=('tajawal',20,'bold'))
sum_lbl.grid(row=1,column=1)
minbl= tk.Label(app,text='minus -',bg='black',fg='green',font=('tajawal',20,'bold'))
minbl.grid(row=2,column=0)
min_lbl= tk.Label(app,text='0',bg='black',fg='white',font=('tajawal',20,'bold'))
min_lbl.grid(row=2,column=1)
multlbl= tk.Label(app,text='multiple *',bg='black',fg='green',font=('tajawal',20,'bold'))
multlbl.grid(row=3,column=0)
multi_lbl= tk.Label(app,text='0',bg='black',fg='white',font=('tajawal',20,'bold'))
multi_lbl.grid(row=3,column=1)
div_lbl= tk.Label(app,text='Divide /',bg='black',fg='green',font=('tajawal',20,'bold'))
div_lbl.grid(row=4,column=0)
div_lbl= tk.Label(app,text='0',bg='black',fg='white',font=('tajawal',20,'bold'))
div_lbl.grid(row=4,column=1)
squarelbl= tk.Label(app,text='square root **',bg='black',fg='green',font=('tajawal',20,'bold'))
squarelbl.grid(row=5,column=0)
square_lbl= tk.Label(app,text='0',bg='black',fg='white',font=('tajawal',20,'bold'))
square_lbl.grid(row=5,column=1)
ent1 = tk.Entry(app,font=('tajawal',20,'bold'))
ent1.grid(row=6,column=0)
ent2 = tk.Entry(app,font=('tajawal',20,'bold'))
ent2.grid(row=7,column=0)


#================================================
def calc():	
	x = int(ent1.get())
	y = int(ent2.get())
	su = x+y
	mi = x-y
	multi = x*y
	div = x/y
	square = x**y
	sum_lbl['text'] = str(su)
	min_lbl['text'] = str(mi)
	multi_lbl['text'] = str(multi)
	div_lbl['text'] = str(div)
	square_lbl['text'] = str(square)


#==============================================
btn = tk.Button(app,text='DO Calc',command=calc,bg='black',fg='red',font=('tajawal',20,'bold'),height=2,width=19).grid(row=8,column=0)

##########################################################

app.mainloop()
