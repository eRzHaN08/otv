from tkinter import *
from random import randint


ok=Tk()
ok.title('Кутакбас')
ok.geometry('500x500')


txt=Label(text='',font=('Comic Sans MS', 20, 'bold'), fg='white', bg='green')
txt.place(x=220,y=280)


def kubas():
    g=int (randint(1,6))
    txt['text']=g



kn=Button(text='Бросить', font=('Comic Sans MS', 20, 'bold'), bg='pink',command=kubas)
kn.place(x=160,y=210)





mainloop()
