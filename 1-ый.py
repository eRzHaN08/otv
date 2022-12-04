from tkinter import *
from tkinter import messagebox


ok=Tk()
ok.title('Задание 1')
ok.geometry('700x700')
ok['bg']='#FFC0CB'




txt1=Label(text='Фамилия', font=('Arial', 40), fg='#008080')
txt1.place(x=90,y=150)

txt2=Label(text='Имя', font=('Arial', 40), fg='#008080')
txt2.place(x=90,y=220)

txt3=Label(text='Отчество', font=('Arial', 40), fg='#008080')
txt3.place(x=90,y=290)


pl=Entry (font=('Arial', 40), width='12', fg='#008080')
pl.place(x=330,y=150)

pl1=Entry (font=('Arial', 40), width='12', fg='#008080')
pl1.place(x=330,y=220)

pl2=Entry (font=('Arial', 40), width='12', fg='#008080')
pl2.place(x=330,y=290)


def texx():
    messagebox.showinfo(title='Информация',message=f'Ваше ФИО:{pl.get()} {pl1.get()} {pl2.get()}')
    



kn=Button(text='Вывести сообщение', font=('Arial', 30), fg='#008080', bg='#00FF7F', command=texx)
kn.place(x=200,y=400)





mainloop()
