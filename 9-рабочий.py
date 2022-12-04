from tkinter import *
from math import sqrt

okno=Tk()
okno.title('квадратичный калькулятор')
okno.minsize(325,230)
okno.resizable(width=False, height=False)

obl=Frame(okno)
obl.grid()


a=Entry(obl, width=3)
a.grid(row=1, column=1, padx=(10,0))

a_txt = Label(obl,text='x**2+').grid(row=1,column=2)


b=Entry(obl,width=3)
b.grid(row=1,column=3)

b_txt=Label(obl, text='x+').grid(row=1,column=4)


c=Entry(obl, width=3)
c.grid(row=1,column=5)

c_txt=Label(obl,text='=0').grid(row=1,column=6)


resh=Text(obl,bg='lightblue', font=('Arial', 12),width=35,height=10)
resh.grid(row=2,columnspan=8)

def formul(a,b,c):
    D = b*b - 4*a*c
    if D >=0:
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)
        text = 'The discriminant is: %s \n X1 is: %s \n X2 is: %s \n' % (D, x1, x2)
    else:
        text='The discriminant is: %s \n This equation has no solutions' % D
    return text


def vstavka(value):
    resh.delete('0.0','end')
    resh.insert('0.0',value)

def obrabot():
    try:
        a_val = float(a.get())
        b_val = float(b.get())
        c_val = float(c.get())
        vstavka(formul(a_val, b_val, c_val))
    except ValueError:
        vstavka('Make sure you entered 3 numbers')

knop=Button(obl, text='Solve', command=obrabot).grid(row=1,column=7, padx=(10,0))




mainloop()