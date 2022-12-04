from tkinter import *
from tkinter import messagebox


ok=Tk()
ok.title('Вход')
ok.geometry('700x700')


txt1 = Label(text='Login',font=('Comic Sans MS', 20, 'bold'))
txt1.place(x=150,y=250)

txt2 = Label(text='Password',font=('Comic Sans MS', 20, 'bold'))
txt2.place(x=150,y=350)



vod1=Entry(font=('Comic Sans MS', 20, 'bold'), width='15')
vod1.place(x=300,y=250)

vod2=Entry(font=('Comic Sans MS', 20, 'bold'), width='15')
vod2.place(x=300,y=350)


def focus():
    if vod1.get()=='Admin' and vod2.get()=='Qwerty123':
        messagebox.showinfo(title='Vhod', message='Authorization completed')
    else:
        messagebox.showinfo(title='Mistake',message='invalid login or password')



poc=Button(text='Authorization',font=('Comic Sans MS', 30, 'bold'), bg='#aaffff', command=focus)
poc.place(x=200,y=500)




def photka(k):
    pho = PhotoImage(file = 'log.png')
    pho_lbl = Label(k)
    pho_lbl.photka = pho
    pho_lbl['image'] = pho_lbl.photka
    pho_lbl.place(x=320, y=100)

photka(ok)




mainloop()
