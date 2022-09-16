###GUI
###pack, grid, place
import tkinter as tkr
##app = tkr.Tk(__name__)
##app.title('My App')
##app.geometry('300x250')
##
###Pack
####tkr.Label(app, text = 'Welcome').pack(anchor='nw')
####tkr.Label(app, text = 'To').pack()
####tkr.Label(app, text = 'Upflairs').pack(anchor='ne')
##
###grid
####tkr.Label(app, text = 'Welcome').grid(row=0,column=1)
####tkr.Label(app, text = 'To').grid(row=1,column=0)
####tkr.Label(app, text = 'Upflairs').grid(row=0, column = 2)
##
###place
##tkr.Label(app, text = 'Welcome').place(x=15,y=15)
##tkr.Label(app, text = 'To').place(x=130,y=100)
##tkr.Label(app, text = 'Upflairs').place(x=230,y=220)
##
##app.mainloop()

#CALCULATOR
app=tkr.Tk(__name__)
app.title('My Calculator')
app.geometry('300x400')

tkr.Label(app, text='CALCULATOR', font=('Arial',20), fg='blue').place(x=75,y=7)
tkr.Label(app, text='First Value', font=(20)).place(x=35,y=60)
tkr.Label(app, text='Second Value', font=(20)).place(x=150,y=60)

fv = tkr.Variable(app)
sv = tkr.Variable(app)

tkr.Entry(app, width= 15, font=('Arial', 10), textvariable=fv).place(x=35,y=80)
tkr.Entry(app, width= 15, font=('Arial', 10), textvariable=sv).place(x=150,y=80)

def myadd():
   res.set(eval(fv.get()+'+'+sv.get()))
def mysub():
   res.set(eval(fv.get()+'-'+sv.get()))
def mymul():
   res.set(eval(fv.get()+'*'+sv.get()))
def mydiv():
   res.set(eval(fv.get()+'/'+sv.get()))

tkr.Button(app, text='+', width =3, bg='red', fg='white', font=(10), command = myadd).place(x=35, y = 130)
tkr.Button(app, text='-', width =3, bg='red', fg='white', font=(10),command = mysub).place(x=95, y = 130)
tkr.Button(app, text='*', width =3, bg='red', fg='white', font=(10),command = mymul).place(x=155, y = 130)
tkr.Button(app, text='/', width =3, bg='red', fg='white', font=(10), command = mydiv).place(x=210, y = 130)

#Result
tkr.Label(app, text='Your Result :', font=('Arial',15)).place(x=35, y=200)
res = tkr.Variable(app)
res.set('0')
tkr.Label(app, font=('Arial',10),textvariable=res ).place(x=150, y=205)


app.mainloop()

#Spinbox
#radiobox
#Combox
#Listbox
























