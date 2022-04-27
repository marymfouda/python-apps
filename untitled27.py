from tkinter import*
window = Tk ()
window.geometry('500x500+150+300')
window.title(" flowe store ")
b = Button(text=' colour ').grid(row=4,column=4)
l = Label(text='choose color ' , fg='blue' , bg='white').place(x=99,y=33)

window.mainloop()
