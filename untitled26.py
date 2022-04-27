from tkinter import *
from tkinter import ttk
from tkinter import messagebox
class super:
    def __init__(self,window):
        self.backgroundcolor="#253C43"
        self.fontcolor="#fff"
        self.color_button="#D6E4B1"
        self.window=window
        window.geometry("1366x750")
        window.title("super market")
        
    def header(self):
        self.header_frame=Button(text="online super market",width=520,bg=self.backgroundcolor,fg=self.fontcolor,font=("arial",15,"bold"),borderwidth=10,state=DISABLED).pack()
    def data_customer(self,name,phone):
        self.f1=Frame(width=350,height=200,bg=self.backgroundcolor).place(x=1016,y=60)
        self.text=Label(self.f1,text="بيانات المشتري",bg=self.backgroundcolor,fg=self.fontcolor,font=("arial",15,"bold")).place(x=1240,y=70)
        #store value_input
        self.name_store=StringVar()
        self.phone_store=StringVar()
        self.nameuser=Label(self.f1,text="اسم المشتري",bg=self.backgroundcolor,fg=self.fontcolor,font=("arial",13,"bold")).place(x=1220,y=120)
        self.name_input=Entry(self.f1,width=20,textvariable=self.name_store).place(x=1080,y=125)
        self.phoneuser=Label(self.f1,text="رقم المشتري",bg=self.backgroundcolor,fg=self.fontcolor,font=("arial",13,"bold")).place(x=1220,y=160)
        self.phone_input=Entry(self.f1,width=20,textvariable=self.phone_store).place(x=1080,y=165)
    def choice(self):
        self.s = ttk.Style()
        self.s.theme_use('default')
        self.s.configure('TNotebook.Tab', background="#aaa")
        self.s.map("TNotebook", background= [("selected", "#000")])
# Create a Notebook widget
        self.nb = ttk.Notebook(window)
# Add a frame for adding a new tab
        self.f11= ttk.Frame(self.nb, width= 1010, height=518)
# Adding the Tab Name
        self.nb.add(self.f11, text= '\t\t\tالادوات الكهربيه\t\t\t')
        self.f22 = ttk.Frame(self.nb)
        self.nb.add(self.f22, text= "\t\t\tالبقوليات\t\t\t")
        self.f23 = ttk.Frame(self.nb)
        self.nb.add(self.f23, text= "\t\t\tالالعاب\t\t\t\t")
        self.nb.place(x=0,y=60)
    def calculate_drink(self):
        self.value_input1=IntVar()
        self.value_input2=IntVar()
        self.value_input3=IntVar()
        self.value_input4=IntVar()
        self.value_input5=IntVar()
        self.value_input6=IntVar()
        self.value_input7=IntVar()
        self.value_input8=IntVar()
        self.value_input9=IntVar()
        self.value_input10=IntVar()
        self.value_input11=IntVar()
        self.value_input12=IntVar()
        self.value_input13=IntVar()
        self.value_input14=IntVar()
        self.value_input15=IntVar()
        self.value_input16=IntVar()
        self.value_input17=IntVar()
        self.value_input18=IntVar()
        self.value_input19=IntVar()
        self.value_input20=IntVar()
        self.value_input21=IntVar()
        self.value_input22=IntVar()
        self.value_input23=IntVar()
        self.value_input24=IntVar()
        self.value_input25=IntVar()
        self.value_input26=IntVar()
        self.value_input27=IntVar()
        self.value_input28=IntVar()
    def drink(self):
      self.frame_drink=Frame(self.f11,height=500,width=1000).place(x=0,y=0)
      self.dicti={
       "Hot oats                 ":15,
       "Hot lotus                ":25,
       "Hot chocolate marshmallow":30,
       "Hot chocolate            ":25,
       "lipton tea               ":10,
       "green tea                ":10,
       "Taylors tea              ":10,
       "Ahmed tea                ":15,
       "Sahlab                   ":17,
       "Ahmed tea                ":15,
       "Sahlab                   ":17,
       "sahlab special Al Dawood ":30,
       "herbs                    ":10,
       "Lemon with boney         ":12,
       "herb                     ":10,
       "Lemo  with boney         ":12 
       }
      self.x=50
      self.y=50
      self.background="#fff"

      self.hot_drink_text=Label(self.f11,text="Hot Drinks",font=("arail",15,"bold")).place(x=20,y=10)
      for key,value in self.dicti.items():
          text=Label(self.f11,text=key).place(x=self.x,y=self.y)
          text=Label(self.f11,text=value).place(x=self.x+(170),y=self.y)
          self.y=self.y+(30)

      self.textinput1=Entry(self.f11,width=20,bg=self.background,textvariable=self.value_input1,justify='center').place(x=290,y=50)
      self.textinput2=Entry(self.f11,width=20,bg=self.background,textvariable=self.value_input2,justify='center').place(x=290,y=80)
      self.textinput3=Entry(self.f11,width=20,bg=self.background,textvariable=self.value_input3,justify='center').place(x=290,y=110)
      self.textinput4=Entry(self.f11,width=20,bg=self.background,textvariable=self.value_input4,justify='center').place(x=290,y=140)
      self.textinput5=Entry(self.f11,width=20,bg=self.background,textvariable=self.value_input5,justify='center').place(x=290,y=170)
      self.textinput6=Entry(self.f11,width=20,bg=self.background,textvariable=self.value_input6,justify='center').place(x=290,y=200)
      self.textinput7=Entry(self.f11,width=20,bg=self.background,textvariable=self.value_input7,justify='center').place(x=290,y=230)
      self.textinput8=Entry(self.f11,width=20,bg=self.background,textvariable=self.value_input8,justify='center').place(x=290,y=260)
      self.textinput9=Entry(self.f11,width=20,bg=self.background,textvariable=self.value_input9,justify='center').place(x=290,y=290)
      self.textinput10=Entry(self.f11,width=20,bg=self.background,textvariable=self.value_input10,justify='center').place(x=290,y=320)
      self.textinput11=Entry(self.f11,width=20,bg=self.background,textvariable=self.value_input11,justify='center').place(x=290,y=350)
      self.textinput12=Entry(self.f11,width=20,bg=self.background,textvariable=self.value_input12,justify='center').place(x=290,y=380)
      self.textinput13=Entry(self.f11,width=20,bg=self.background,textvariable=self.value_input13,justify='center').place(x=290,y=410)
      self.textinput14=Entry(self.f11,width=20,bg=self.background,textvariable=self.value_input14,justify='center').place(x=290,y=440)
      #row2
      self.x2=480
      self.y2=50
      for key,value in self.dicti.items():
          text=Label(self.f11,text=key).place(x=self.x2,y=self.y2)
          text=Label(self.f11,text=value).place(x=self.x2+(170),y=self.y2)
          self.y2=self.y2+(30)
      self.textinput15=Entry(self.f11,width=20,bg=self.background,textvariable=self.value_input15,justify='center').place(x=720,y=50)
      self.textinput16=Entry(self.f11,width=20,bg=self.background,textvariable=self.value_input16,justify='center').place(x=720,y=80)
      self.textinput17=Entry(self.f11,width=20,bg=self.background,textvariable=self.value_input17,justify='center').place(x=720,y=110)
      self.textinput18=Entry(self.f11,width=20,bg=self.background,textvariable=self.value_input18,justify='center').place(x=720,y=140)
      self.textinput19=Entry(self.f11,width=20,bg=self.background,textvariable=self.value_input19,justify='center').place(x=720,y=170)
      self.textinput20=Entry(self.f11,width=20,bg=self.background,textvariable=self.value_input20,justify='center').place(x=720,y=200)
      self.textinput21=Entry(self.f11,width=20,bg=self.background,textvariable=self.value_input21,justify='center').place(x=720,y=230)
      self.textinput22=Entry(self.f11,width=20,bg=self.background,textvariable=self.value_input22,justify='center').place(x=720,y=260)
      self.textinput23=Entry(self.f11,width=20,bg=self.background,textvariable=self.value_input23,justify='center').place(x=720,y=290)
      self.textinput24=Entry(self.f11,width=20,bg=self.background,textvariable=self.value_input24,justify='center').place(x=720,y=320)
      self.textinput25=Entry(self.f11,width=20,bg=self.background,textvariable=self.value_input25,justify='center').place(x=720,y=350)
      self.textinput26=Entry(self.f11,width=20,bg=self.background,textvariable=self.value_input26,justify='center').place(x=720,y=380)
      self.textinput27=Entry(self.f11,width=20,bg=self.background,textvariable=self.value_input27,justify='center').place(x=720,y=410)
      self.textinput28=Entry(self.f11,width=20,bg=self.background,textvariable=self.value_input28,justify='center').place(x=720,y=440)
    def calculate_drink2(self):
        self.value_input1=IntVar()
        self.value_input2=IntVar()
        self.value_input3=IntVar()
        self.value_input4=IntVar()
        self.value_input5=IntVar()
        self.value_input6=IntVar()
        self.value_input7=IntVar()
        self.value_input8=IntVar()
        self.value_input9=IntVar()
        self.value_input10=IntVar()
        self.value_input11=IntVar()
        self.value_input12=IntVar()
        self.value_input13=IntVar()
        self.value_input14=IntVar()
        self.value_input15=IntVar()
        self.value_input16=IntVar()
        self.value_input17=IntVar()
        self.value_input18=IntVar()
        self.value_input19=IntVar()
        self.value_input20=IntVar()
        self.value_input21=IntVar()
        self.value_input22=IntVar()
        self.value_input23=IntVar()
        self.value_input24=IntVar()
        self.value_input25=IntVar()
        self.value_input26=IntVar()
        self.value_input27=IntVar()
        self.value_input28=IntVar()
        
    def drink2(self):
      self.frame_drink2=Frame(self.f22,height=500,width=1000).place(x=0,y=0)
      self.dicti={
       "Hot oats                 ":15,
       "Hot lotus                ":25,
       "Hot chocolate marshmallow":30,
       "Hot chocolate            ":25,
       "lipton tea               ":10,
       "green tea                ":10,
       "Taylors tea              ":10,
       "Ahmed tea                ":15,
       "Sahlab                   ":17,
       "Ahmed tea                ":15,
       "Sahlab                   ":17,
       "sahlab special Al Dawood ":30,
       "herbs                    ":10,
       "Lemon with boney         ":12,
       "herb                     ":10,
       "Lemo  with boney         ":12 
       }
      self.x=50
      self.y=50
      self.background="#fff"

      self.hot_drink_text=Label(self.f22,text="Hot Drinks",font=("arail",15,"bold")).place(x=20,y=10)
      for key,value in self.dicti.items():
          text=Label(self.f22,text=key).place(x=self.x,y=self.y)
          text=Label(self.f22,text=value).place(x=self.x+(170),y=self.y)
          self.y=self.y+(30)

      self.textinput1=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input1,justify='center').place(x=290,y=50)
      self.textinput2=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input2,justify='center').place(x=290,y=80)
      self.textinput3=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input3,justify='center').place(x=290,y=110)
      self.textinput4=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input4,justify='center').place(x=290,y=140)
      self.textinput5=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input5,justify='center').place(x=290,y=170)
      self.textinput6=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input6,justify='center').place(x=290,y=200)
      self.textinput7=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input7,justify='center').place(x=290,y=230)
      self.textinput8=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input8,justify='center').place(x=290,y=260)
      self.textinput9=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input9,justify='center').place(x=290,y=290)
      self.textinput10=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input10,justify='center').place(x=290,y=320)
      self.textinput11=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input11,justify='center').place(x=290,y=350)
      self.textinput12=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input12,justify='center').place(x=290,y=380)
      self.textinput13=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input13,justify='center').place(x=290,y=410)
      self.textinput14=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input14,justify='center').place(x=290,y=440)
      #row2
      self.x2=480
      self.y2=50
      for key,value in self.dicti.items():
          text=Label(self.f22,text=key).place(x=self.x2,y=self.y2)
          text=Label(self.f22,text=value).place(x=self.x2+(170),y=self.y2)
          self.y2=self.y2+(30)
      self.textinput15=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input15,justify='center').place(x=720,y=50)
      self.textinput16=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input16,justify='center').place(x=720,y=80)
      self.textinput17=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input17,justify='center').place(x=720,y=110)
      self.textinput18=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input18,justify='center').place(x=720,y=140)
      self.textinput19=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input19,justify='center').place(x=720,y=170)
      self.textinput20=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input20,justify='center').place(x=720,y=200)
      self.textinput21=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input21,justify='center').place(x=720,y=230)
      self.textinput22=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input22,justify='center').place(x=720,y=260)
      self.textinput23=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input23,justify='center').place(x=720,y=290)
      self.textinput24=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input24,justify='center').place(x=720,y=320)
      self.textinput25=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input25,justify='center').place(x=720,y=350)
      self.textinput26=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input26,justify='center').place(x=720,y=380)
      self.textinput27=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input27,justify='center').place(x=720,y=410)
      self.textinput28=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input28,justify='center').place(x=720,y=440)
    
    def calculate_drink3(self):
        self.value_input1=IntVar()
        self.value_input2=IntVar()
        self.value_input3=IntVar()
        self.value_input4=IntVar()
        self.value_input5=IntVar()
        self.value_input6=IntVar()
        self.value_input7=IntVar()
        self.value_input8=IntVar()
        self.value_input9=IntVar()
        self.value_input10=IntVar()
        self.value_input11=IntVar()
        self.value_input12=IntVar()
        self.value_input13=IntVar()
        self.value_input14=IntVar()
        self.value_input15=IntVar()
        self.value_input16=IntVar()
        self.value_input17=IntVar()
        self.value_input18=IntVar()
        self.value_input19=IntVar()
        self.value_input20=IntVar()
        self.value_input21=IntVar()
        self.value_input22=IntVar()
        self.value_input23=IntVar()
        self.value_input24=IntVar()
        self.value_input25=IntVar()
        self.value_input26=IntVar()
        self.value_input27=IntVar()
        self.value_input28=IntVar()
    def drink3(self):
      self.frame_drink3=Frame(self.f23,height=500,width=1000).place(x=0,y=0)
      self.dicti={
       "Hot oats                 ":15,
       "Hot lotus                ":25,
       "Hot chocolate marshmallow":30,
       "Hot chocolate            ":25,
       "lipton tea               ":10,
       "green tea                ":10,
       "Taylors tea              ":10,
       "Ahmed tea                ":15,
       "Sahlab                   ":17,
       "Ahmed tea                ":15,
       "Sahlab                   ":17,
       "sahlab special Al Dawood ":30,
       "herbs                    ":10,
       "Lemon with boney         ":12,
       "herb                     ":10,
       "Lemo  with boney         ":12 
       }
      self.x=50
      self.y=50
      self.background="#fff"

      self.hot_drink_text=Label(self.f23,text="Hot Drinks",font=("arail",15,"bold")).place(x=20,y=10)
      for key,value in self.dicti.items():
          text=Label(self.f23,text=key).place(x=self.x,y=self.y)
          text=Label(self.f23,text=value).place(x=self.x+(170),y=self.y)
          self.y=self.y+(30)

      self.textinput1=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input1,justify='center').place(x=290,y=50)
      self.textinput2=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input2,justify='center').place(x=290,y=80)
      self.textinput3=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input3,justify='center').place(x=290,y=110)
      self.textinput4=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input4,justify='center').place(x=290,y=140)
      self.textinput5=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input5,justify='center').place(x=290,y=170)
      self.textinput6=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input6,justify='center').place(x=290,y=200)
      self.textinput7=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input7,justify='center').place(x=290,y=230)
      self.textinput8=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input8,justify='center').place(x=290,y=260)
      self.textinput9=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input9,justify='center').place(x=290,y=290)
      self.textinput10=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input10,justify='center').place(x=290,y=320)
      self.textinput11=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input11,justify='center').place(x=290,y=350)
      self.textinput12=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input12,justify='center').place(x=290,y=380)
      self.textinput13=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input13,justify='center').place(x=290,y=410)
      self.textinput14=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input14,justify='center').place(x=290,y=440)
      #row2
      self.x2=480
      self.y2=50
      for key,value in self.dicti.items():
          text=Label(self.f23,text=key).place(x=self.x2,y=self.y2)
          text=Label(self.f23,text=value).place(x=self.x2+(170),y=self.y2)
          self.y2=self.y2+(30)
      self.textinput15=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input15,justify='center').place(x=720,y=50)
      self.textinput16=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input16,justify='center').place(x=720,y=80)
      self.textinput17=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input17,justify='center').place(x=720,y=110)
      self.textinput18=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input18,justify='center').place(x=720,y=140)
      self.textinput19=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input19,justify='center').place(x=720,y=170)
      self.textinput20=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input20,justify='center').place(x=720,y=200)
      self.textinput21=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input21,justify='center').place(x=720,y=230)
      self.textinput22=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input22,justify='center').place(x=720,y=260)
      self.textinput23=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input23,justify='center').place(x=720,y=290)
      self.textinput24=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input24,justify='center').place(x=720,y=320)
      self.textinput25=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input25,justify='center').place(x=720,y=350)
      self.textinput26=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input26,justify='center').place(x=720,y=380)
      self.textinput27=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input27,justify='center').place(x=720,y=410)
      self.textinput28=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input28,justify='center').place(x=720,y=440)
    def alfatora(self):
       self.textfatora=Label(self.f1,text="[الفواتير]",font=("arial",13,"bold"),fg="gold",bg=self.backgroundcolor).place(x=1157,y=200)
       self.F5 = Frame(self.window,bd=0,width=220,bg='white',height=200)
       self.F5.place(x=1016,y=220)
       scrol_y= Scrollbar(self.F5,orient=VERTICAL)
       self.txtarea=Text(self.F5,yscrollcommand=scrol_y.set)
       scrol_y.pack(side=LEFT,fill=Y)
       scrol_y.config(command=self.txtarea.yview)
       self.txtarea.pack(fill=BOTH,expand=1)
    def calculate_price(self):
        f3=Frame(width=1360,height=100,bg=self.backgroundcolor).place(x=0,y=600)
        self.button_1=Button(text="الحساب",bg=self.color_button,width=10,borderwidth=2,cursor="hand2",font=("arial",13,"bold")).place(x=1225,y=620)
        self.button_2=Button(text="افراغ الحقول",bg=self.color_button,width=10,borderwidth=2,cursor="hand2",font=("arial",13,"bold")).place(x=1110,y=620)
        self.button_3=Button(text="تصدير الفاتوره",bg=self.color_button,width=10,borderwidth=2,cursor="hand2",font=("arial",13,"bold")).place(x=1225,y=660)
        self.button_4=Button(text="اغلاق البرنامج",bg=self.color_button,width=10,borderwidth=2,cursor="hand2",font=("arial",13,"bold")).place(x=1110,y=660)
        self.text_price1=Label(text="حساب الكلي البقوليات",bg=self.backgroundcolor,fg=self.fontcolor,font=("arial",13,"bold")).place(x=880,y=630)
        self.input_price1=Label(text="",bg=self.fontcolor,fg=self.fontcolor,font=("arial",13,"bold"),width=12).place(x=750,y=630)
        self.text_price2=Label(text="حساب الكلي البقوليات",bg=self.backgroundcolor,fg=self.fontcolor,font=("arial",13,"bold")).place(x=550,y=630)
        self.input_price2=Label(text="",bg=self.fontcolor,fg=self.fontcolor,font=("arial",13,"bold"),width=12).place(x=420,y=630)
        self.text_price3=Label(text="حساب الكلي البقوليات",bg=self.backgroundcolor,fg=self.fontcolor,font=("arial",13,"bold")).place(x=220,y=630)
        self.input_price3=Label(text="",bg=self.fontcolor,fg=self.fontcolor,font=("arial",13,"bold"),width=12).place(x=90,y=630)
window=Tk()
my_class=super(window)
my_class.header()
my_class.calculate_drink2()
my_class.calculate_price() 
my_class.choice()
my_class.calculate_drink()
my_class.drink()
my_class.drink3()
my_class.calculate_drink3()
my_class.drink2()
my_class.data_customer("reham",18)
my_class.alfatora()

window.mainloop()