from tkinter import *


ok=Tk()
ok.title('Задание 2')
ok.geometry('700x700')



pol=Scale (orient='horizontal', from_=1, to=4, width=15, length=400)
pol.place(x=150,y=150)




lbl=Label(text='Меняю цвет', font=('Arial', 40))
lbl.place(x=160,y=400)



def polus():
    if (pol.get()) == 1:
        lbl['bg']='blue'
    elif (pol.get()) == 2:
        lbl['bg']='red'
    elif (pol.get()) == 3:
        lbl['bg']='green'
    elif (pol.get()) == 4:
        lbl['bg'] = 'pink'



but=Button(text='Click', font=('Arial',40), command=polus)
but.place(x=220,y=250)












mainloop()
