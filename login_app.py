from tkinter import*
from tkinter import messagebox
import webbrowser
#=========== code start ====================  
tk2=Tk()
tk2.geometry('1366x750')
tk2.resizable(False,False)
tk2.title("restaurant")
#============== the program icon ===============
tk2.iconbitmap('D:\\icon.ico')
title= Label(tk2 , text="Restaurant System ",fg='#0B2F3A',bg='gray',font=('tajawal',18,'bold'))
title.pack(fill=X)
#============= our acc =======================
u1='http://www.facebook.com/username'
u2='url-telegram'
u3='url-youtube'
#============= function ======================
def Open1 () :
    webbrowser.open_new(u1)
def Open2 () :
    webbrowser.open_new(u2)    
def Open3 () :
    webbrowser.open_new(u3)
def about1 () :
    messagebox.showinfo('developer','mrteam in fci tanta universty')
def about2 () :
     messagebox.showinfo('about program','system restaurant')
def log() :
    user =En1.get()
    passw =En2.get()
    if user=='mrteam' and passw=='123456' :
       tk2.destroy() 
       import menue_app
       menue_app.mainloop()
    else:
        messagebox.showerror('error','sory,your information is not true ')
F1= Frame(tk2 , width=380 , height=740, bg='#0B2F3A')
F1.place(x=1016,y=28)
b1= Button ( F1 , text='Facebook acc' , width=26,height=2,bg='gray',fg='black',relief=SUNKEN,font=('tajawal',12 ,'bold'),command=Open1)
b1.place(x=50,y=200)
b2= Button ( F1 , text='Telegram acc' , width=26,height=2,bg='gray',fg='black',relief=SUNKEN,font=('tajawal',12 ,'bold'),command=Open2)
b2.place(x=50,y=270)
b3= Button ( F1 , text='Youtube acc' , width=26,height=2,bg='gray',fg='black',relief=SUNKEN,font=('tajawal',12 ,'bold'),command=Open3)
b3.place(x=50,y=340)
b4= Button ( F1 , text='Developer info' , width=26,height=2,bg='gray',fg='black',relief=SUNKEN,font=('tajawal',12 ,'bold'),command=about1)
b4.place(x=50,y=410)
b5= Button ( F1 , text='Project info' , width=26,height=2,bg='gray',fg='black',relief=SUNKEN,font=('tajawal',12 ,'bold'),command=about2)
b5.place(x=50,y=480)
b6= Button ( F1 , text='Exit' , width=16,bg='white',height=2,fg='#0B2F3A',relief=SUNKEN,font=('tajawal',18 ,'bold'),command=quit)
b6.place(x=45,y=600)
#================ program photo ==================
photo=PhotoImage( file='D://restu.png')
imo= Label (tk2 ,image=photo ) 
imo.place(x=180,y=36,width=600,height=672)
F2=Frame (tk2 , width=1070 , height=220,bg='#0B2F3A')
F2.place(x=0,y=560)
photo1= PhotoImage( file ='D:\\img8.png')
imo1 = Label (F2 , image=photo1)
imo1.place(x=1050,y=935 , width=510,height=510)
L1= Label(F2 , text='user name : ', fg='white' ,bg='#0B2F3A', font= ('tajawal',12 ,'bold') )
L1.place(x=30 ,y= 25)
L2= Label(F2 , text='password : ', fg='white' ,bg='#0B2F3A', font= ('tajawal',12 ,'bold') )
L2.place(x=30 ,y= 70)
L3=Label(F2 , text='Welcome to our restaurant  , choose what you like! ', fg='gray' ,bg='#0B2F3A', font= ('tajawal',18 ,'bold') )
L3.place(x=390 ,y= 60)
En1=Entry( F2 , font=('tajawal',12) , justify='center')
En1.place(x=130,y=26)
En2=Entry( F2 , font=('tajawal',12) , justify='center')
En2.place(x=130,y=71)
b= Button (F2 , text =' Login' , bg='gray' , fg='black' , font=('tajawal',12,'bold'),command=log)
b.place(x=200,y=105)
tk2.mainloop()