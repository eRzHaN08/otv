from tkinter import *



ok=Tk()
ok.title('СЧИТАЕМ')
ok.geometry('700x500')
ok['bg']='white'



txt1=Label(text='0', font=('Comic',100), fg='white', bg='black')
txt1.place(x=300,y=150)


def plus():
    x=int(txt1['text'])
    txt1['text']=x+1


def minus():
    y=int(txt1['text'])
    txt1['text']=y-1




pl=Button(text='+', font=('Comic',100), fg='#08D9D6',bg='pink', command=plus)
pl.place(x=450,y=80)

p2=Button(text='-', font=('Comic',100), fg='#08D9D6',bg='pink', command=minus)
p2.place(x=100,y=80)



























mainloop()

