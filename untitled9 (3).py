# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 10:53:22 2021

@author: rewan
"""

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
        window.title("Restaurant")
        
    def header(self):
        self.header_frame=Button(text="Restaurant",width=520,bg=self.backgroundcolor,fg=self.fontcolor,font=("arial",15,"bold"),borderwidth=10,state=DISABLED).pack()
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
        self.nb = ttk.Notebook(window)
        self.f11= ttk.Frame(self.nb, width= 1010, height=518)
        self.nb.add(self.f11, text='\t\t\t Sandwitches\t\t\t')
        self.f22 = ttk.Frame(self.nb)
        self.nb.add(self.f22, text= "\t\t\tMain dishes\t\t\t")
        self.f23 = ttk.Frame(self.nb)
        self.nb.add(self.f23, text= "\t\t\tHot drinks\t\t\t\t")
        self.nb.place(x=0,y=60)


    def drink(self):
        self.frame_drink=Frame(self.f11,height=500,width=1000).place(x=0,y=0)
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
        self.dicti1={
       "Beefburger cheese       ":250,
       "chicken burger          ":250,
       "beefburger special      ":300,
       "chawarma pain           ":100,
       "chawarma raghif         ":100,
       "chawarma special        ":100,
       "chawarma garnie         ":200,
       "souffle poulet          ":100,
       "souffle viande          ":170,
       "souffle mixte           ":150,
       "souffle merguaz         ":170,
       "soiffle garnie         ":130,
       "malfouf special        ":200,
       "malfouf poulet         ":120,
       }
        self.dicti2={
      "crepe kebda      ":100,
       "crepe viande      ":150,
       "crepe chicken     ":130,
       "corn mayo         ":60,
       "corn cheese       ":40,
       "corn lays mayo    ":70,
       "corn lays cheese   ":60,
       "corn mayo tomato   ":60,
       "veg mayo crilled   ":70,
       "veg club cheese    ":50,
       "veg crilled sndwitch":70,
       "veg sandwitch       ":40,
       "Bhujia sandwitch grill":60,
       "Bhujia sandwitch cheese":60,
       }
        self.hot_drink_text=Label(self.f11,text="Sandwitches",font=("arail",15,"bold")).place(x=20,y=10)
        self.x=50
        self.y=50
        self.background="#fff"
      #row1
        for key,value in self.dicti1.items():
          text=Label(self.f11,text=key).place(x=self.x,y=self.y)
          text=Label(self.f11,text=value).place(x=self.x+(170),y=self.y)
          self.y=self.y+(30)
      #row2
        self.x2=480
        self.y2=50
        for key,value in self.dicti2.items():
          text=Label(self.f11,text=key).place(x=self.x2,y=self.y2)
          text=Label(self.f11,text=value).place(x=self.x2+(170),y=self.y2)
          self.y2=self.y2+(30)
        self.textinput1=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input1,justify='center').place(x=290,y=50)
        self.textinput2=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input2,justify='center').place(x=290,y=80)
        self.textinput3=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input3,justify='center').place(x=290,y=110)
        self.textinput4=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input4,justify='center').place(x=290,y=140)
        self.textinput5=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input5,justify='center').place(x=290,y=170)
        self.textinput6=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input6,justify='center').place(x=290,y=200)
        self.textinput7=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input7,justify='center').place(x=290,y=230)
        self.textinput8=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input8,justify='center').place(x=290,y=260)
        self.textinput9=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input9,justify='center').place(x=290,y=290)
        self.textinput10=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input10,justify='center').place(x=290,y=320)
        self.textinput11=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input11,justify='center').place(x=290,y=350)
        self.textinput12=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input12,justify='center').place(x=290,y=380)
        self.textinput13=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input13,justify='center').place(x=290,y=410)
        self.textinput14=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input14,justify='center').place(x=290,y=440)
        self.textinput15=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input15,justify='center').place(x=720,y=50)
        self.textinput16=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input16,justify='center').place(x=720,y=80)
        self.textinput17=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input17,justify='center').place(x=720,y=110)
        self.textinput18=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input18,justify='center').place(x=720,y=140)
        self.textinput19=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input19,justify='center').place(x=720,y=170)
        self.textinput20=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input20,justify='center').place(x=720,y=200)
        self.textinput21=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input21,justify='center').place(x=720,y=230)
        self.textinput22=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input22,justify='center').place(x=720,y=260)
        self.textinput23=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input23,justify='center').place(x=720,y=290)
        self.textinput24=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input24,justify='center').place(x=720,y=320)
        self.textinput25=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input25,justify='center').place(x=720,y=350)
        self.textinput26=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input26,justify='center').place(x=720,y=380)
        self.textinput27=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input27,justify='center').place(x=720,y=410)
        self.textinput28=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input28,justify='center').place(x=720,y=440)
    def calculate_drink(self):
        self.price1=self.value_input1.get()*250
        self.price2=self.value_input2.get()*250
        self.price3=self.value_input3.get()*300
        self.price4=self.value_input4.get()*100
        self.price5=self.value_input5.get()*100
        self.price6=self.value_input6.get()*100
        self.price7=self.value_input7.get()*200
        self.price8=self.value_input8.get()*100
        self.price9=self.value_input9.get()*170
        self.price10=self.value_input10.get()*150
        self.price11=self.value_input11.get()*170
        self.price12=self.value_input12.get()*130
        self.price13=self.value_input13.get()*200
        self.price14=self.value_input14.get()*120
        self.price15=self.value_input15.get()*100
        self.price16=self.value_input16.get()*150
        self.price17=self.value_input17.get()*130
        self.price18=self.value_input18.get()*60
        self.price19=self.value_input19.get()*40
        self.price20=self.value_input20.get()*40
        self.price21=self.value_input21.get()*60
        self.price22=self.value_input22.get()*60
        self.price23=self.value_input23.get()*70
        self.price24=self.value_input24.get()*50
        self.price25=self.value_input25.get()*70
        self.price26=self.value_input26.get()*40
        self.price27=self.value_input27.get()*60
        self.price28=self.value_input28.get()*60
        self.total=float(
                        self.price1+self.price2+self.price3+self.price4+self.price5+self.price6+self.price7+self.price8+self.price9+self.price10+self.price11+self.price12+self.price13+self.price14+self.price15+self.price16+self.price17+self.price18+self.price19+self.price20+self.price21+self.price22+self.price23+self.price24+self.price25+self.price26+self.price27+self.price28)
        self.sandwitch.set(str(self.total)+" $")
        #price main dishes
        self.price1a=self.value_input1a.get()*350
        self.price2a=self.value_input2a.get()*450
        self.price3a=self.value_input3a.get()*300
        self.price4a=self.value_input4a.get()*250
        self.price5a=self.value_input5a.get()*150
        self.price6a=self.value_input6a.get()*100
        self.price7a=self.value_input7a.get()*100
        self.price8a=self.value_input8a.get()*100
        self.price9a=self.value_input9a.get()*120
        self.price10a=self.value_input10a.get()*150
        self.price11a=self.value_input11a.get()*170
        self.price12a=self.value_input12a.get()*250
        self.price13a=self.value_input13a.get()*190
        self.price14a=self.value_input14a.get()*170
        self.price15a=self.value_input15a.get()*250
        self.price16a=self.value_input16a.get()*350
        self.price17a=self.value_input17a.get()*310
        self.price18a=self.value_input18a.get()*200
        self.price19a=self.value_input19a.get()*130
        self.price20a=self.value_input20a.get()*150
        self.price21a=self.value_input21a.get()*350
        self.price22a=self.value_input22a.get()*120
        self.price23a=self.value_input23a.get()*180
        self.price24a=self.value_input24a.get()*250
        self.price25a=self.value_input25a.get()*270
        self.price26a=self.value_input26a.get()*160
        self.price27a=self.value_input27a.get()*190
        self.price28a=self.value_input28a.get()*130
        self.total2=float(
                        self.price1a+self.price2a+self.price3a+self.price4a+self.price5a+self.price6a+self.price7a+self.price8a+self.price9a+self.price10a+self.price11a+self.price12a+self.price13a+self.price14a+self.price15a+self.price16a+self.price17a+self.price18a+self.price19a+self.price20a+self.price21a+self.price22a+self.price23a+self.price24a+self.price25a+self.price26a+self.price27a+self.price28a)
        self.dishes.set(str(self.total2)+" $")
        #hot drinks
        self.price1aa=self.value_input1aa.get()*15
        self.price2aa=self.value_input2aa.get()*25
        self.price3aa=self.value_input3aa.get()*30
        self.price4aa=self.value_input4aa.get()*25
        self.price5aa=self.value_input5aa.get()*10
        self.price6aa=self.value_input6aa.get()*10
        self.price7aa=self.value_input7aa.get()*10
        self.price8aa=self.value_input8aa.get()*15
        self.price9aa=self.value_input9aa.get()*17
        self.price10aa=self.value_input10aa.get()*30
        self.price11aa=self.value_input11aa.get()*10
        self.price12aa=self.value_input12aa.get()*12
        self.price13aa=self.value_input13aa.get()*10
        self.price14aa=self.value_input14aa.get()*12
        self.price15aa=self.value_input15aa.get()*20
        self.price16aa=self.value_input16aa.get()*25
        self.price17aa=self.value_input17aa.get()*32
        self.price18aa=self.value_input18aa.get()*35
        self.price19aa=self.value_input19aa.get()*27
        self.price20aa=self.value_input20aa.get()*37
        self.price21aa=self.value_input21aa.get()*40
        self.price22aa=self.value_input22aa.get()*30
        self.price23aa=self.value_input23aa.get()*28
        self.price24aa=self.value_input24aa.get()*34
        self.price25aa=self.value_input25aa.get()*17
        self.price26aa=self.value_input26aa.get()*14
        self.price27aa=self.value_input27aa.get()*20
        self.price28aa=self.value_input28aa.get()*36
        self.total3=float(
                        self.price1aa+self.price2aa+self.price3aa+self.price4aa+self.price5aa+self.price6aa+self.price7aa+self.price8aa+self.price9aa+self.price10aa+self.price11aa+self.price12aa+self.price13aa+self.price14aa+self.price15aa+self.price16aa+self.price17aa+self.price18aa+self.price19aa+self.price20aa+self.price21aa+self.price22aa+self.price23aa+self.price24aa+self.price25aa+self.price26aa+self.price27aa+self.price28aa)
        self.hotdrink.set(str(self.total3)+" $")        
    def drink2(self):
      self.frame_drink2=Frame(self.f22,height=500,width=1000).place(x=0,y=0)
      self.value_input1a=IntVar()
      self.value_input2a=IntVar()
      self.value_input3a=IntVar()
      self.value_input4a=IntVar()
      self.value_input5a=IntVar()
      self.value_input6a=IntVar()
      self.value_input7a=IntVar()
      self.value_input8a=IntVar()
      self.value_input9a=IntVar()
      self.value_input10a=IntVar()
      self.value_input11a=IntVar()
      self.value_input12a=IntVar()
      self.value_input13a=IntVar()
      self.value_input14a=IntVar()
      self.value_input15a=IntVar()
      self.value_input16a=IntVar()
      self.value_input17a=IntVar()
      self.value_input18a=IntVar()
      self.value_input19a=IntVar()
      self.value_input20a=IntVar()
      self.value_input21a=IntVar()
      self.value_input22a=IntVar()
      self.value_input23a=IntVar()
      self.value_input24a=IntVar()
      self.value_input25a=IntVar()
      self.value_input26a=IntVar()
      self.value_input27a=IntVar()
      self.value_input28a=IntVar()      
      self.dicti={
       "chawarema              ":350,
       "corden bleu            ":450,
       "scalpoe creme          ":300,
       "balles grille          ":250,
       "poulet marine          ":150,
       "fried wings            ":100,
       "lemon paper wings      ":100,
       "jerk wings             ":100,
       "creole wings           ":120,
       "fish filet             ":150,
       "Griot                 ":170,
       "Grilled chicken       ":250,
       "creole shrimp         ":190,
       "fried shrimp          ":170,
       }
      self.x=50
      self.y=50
      self.background="#fff"

      self.hot_drink_text=Label(self.f22,text="Main dishes",font=("arail",15,"bold")).place(x=20,y=10)
      for key,value in self.dicti.items():
          text=Label(self.f22,text=key).place(x=self.x,y=self.y)
          text=Label(self.f22,text=value).place(x=self.x+(170),y=self.y)
          self.y=self.y+(30)

      self.textinput1a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input1a,justify='center').place(x=290,y=50)
      self.textinput2a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input2a,justify='center').place(x=290,y=80)
      self.textinput3a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input3a,justify='center').place(x=290,y=110)
      self.textinput4a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input4a,justify='center').place(x=290,y=140)
      self.textinput5a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input5a,justify='center').place(x=290,y=170)
      self.textinput6a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input6a,justify='center').place(x=290,y=200)
      self.textinput7a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input7a,justify='center').place(x=290,y=230)
      self.textinput8a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input8a,justify='center').place(x=290,y=260)
      self.textinput9a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input9a,justify='center').place(x=290,y=290)
      self.textinput10a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input10a,justify='center').place(x=290,y=320)
      self.textinput11a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input11a,justify='center').place(x=290,y=350)
      self.textinput12a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input12a,justify='center').place(x=290,y=380)
      self.textinput13a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input13a,justify='center').place(x=290,y=410)
      self.textinput14a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input14a,justify='center').place(x=290,y=440)
      #row2
      self.dicti2={
       "steamed shrip           ":250,
       "oxtail                  ":350,
       "fried conch             ":310,
       "Grill conch             ":200,
       "slew conch             " :130,
       "fried fish              ":150,
       "lobster tail            ":140,
       "crabe creole (seasonal) ":120,
       "stew chicken           ":180,
       "Grilled chicken         ":250,
       "stew fish               ":270,
       "lobster tail            ":350,
       "fried pork              ":160,
       "steamed conch           ":190,
       "colombo                 ":130
       }
      self.x2=480
      self.y2=50
      for key,value in self.dicti2.items():
          text=Label(self.f22,text=key).place(x=self.x2,y=self.y2)
          text=Label(self.f22,text=value).place(x=self.x2+(170),y=self.y2)
          self.y2=self.y2+(30)
      self.textinput15a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input15a,justify='center').place(x=720,y=50)
      self.textinput16a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input16a,justify='center').place(x=720,y=80)
      self.textinput17a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input17a,justify='center').place(x=720,y=110)
      self.textinput18a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input18a,justify='center').place(x=720,y=140)
      self.textinput19a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input19a,justify='center').place(x=720,y=170)
      self.textinput20a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input20a,justify='center').place(x=720,y=200)
      self.textinput21a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input21a,justify='center').place(x=720,y=230)
      self.textinput22a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input22a,justify='center').place(x=720,y=260)
      self.textinput23a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input23a,justify='center').place(x=720,y=290)
      self.textinput24a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input24a,justify='center').place(x=720,y=320)
      self.textinput25a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input25a,justify='center').place(x=720,y=350)
      self.textinput26a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input26a,justify='center').place(x=720,y=380)
      self.textinput27a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input27a,justify='center').place(x=720,y=410)
      self.textinput28a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input28a,justify='center').place(x=720,y=440)
    

    def drink3(self):
      self.frame_drink3=Frame(self.f23,height=500,width=1000).place(x=0,y=0)
      self.value_input1aa=IntVar()
      self.value_input2aa=IntVar()
      self.value_input3aa=IntVar()
      self.value_input4aa=IntVar()
      self.value_input5aa=IntVar()
      self.value_input6aa=IntVar()
      self.value_input7aa=IntVar()
      self.value_input8aa=IntVar()
      self.value_input9aa=IntVar()
      self.value_input10aa=IntVar()
      self.value_input11aa=IntVar()
      self.value_input12aa=IntVar()
      self.value_input13aa=IntVar()
      self.value_input14aa=IntVar()
      self.value_input15aa=IntVar()
      self.value_input16aa=IntVar()
      self.value_input17aa=IntVar()
      self.value_input18aa=IntVar()
      self.value_input19aa=IntVar()
      self.value_input20aa=IntVar()
      self.value_input21aa=IntVar()
      self.value_input22aa=IntVar()
      self.value_input23aa=IntVar()
      self.value_input24aa=IntVar()
      self.value_input25aa=IntVar()
      self.value_input26aa=IntVar()
      self.value_input27aa=IntVar()
      self.value_input28aa=IntVar()      
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

      self.textinput1aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input1aa,justify='center').place(x=290,y=50)
      self.textinput2aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input2aa,justify='center').place(x=290,y=80)
      self.textinput3aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input3aa,justify='center').place(x=290,y=110)
      self.textinput4aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input4aa,justify='center').place(x=290,y=140)
      self.textinput5aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input5aa,justify='center').place(x=290,y=170)
      self.textinput6aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input6aa,justify='center').place(x=290,y=200)
      self.textinput7aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input7aa,justify='center').place(x=290,y=230)
      self.textinput8aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input8aa,justify='center').place(x=290,y=260)
      self.textinput9aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input9aa,justify='center').place(x=290,y=290)
      self.textinput10aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input10aa,justify='center').place(x=290,y=320)
      self.textinput11aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input11aa,justify='center').place(x=290,y=350)
      self.textinput12aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input12aa,justify='center').place(x=290,y=380)
      self.textinput13aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input13aa,justify='center').place(x=290,y=410)
      self.textinput14aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input14aa,justify='center').place(x=290,y=440)
      #row2
      self.dicit2={
       "Hot penicillin           ":20,
       "moneygun toddy           ":25,
       "Hot turmeric             ":32,
       "tahini Hot chocolate     ":35,
       "mexican Hot chocolate    ":27,
       "coffe                    ":37,
       "vintage coffe            ":40,
       "matcha latte             ":30,
       "hot toddy                ":28,
       "caramel latte            ":34,
       "hot cocoa                ":17,
       "warm hazelnut            ":14,
       "magic cocoa              ":20,
       "piccole latte            ":36 
          }
      self.x2=480
      self.y2=50
      for key,value in self.dicit2.items():
          text=Label(self.f23,text=key).place(x=self.x2,y=self.y2)
          text=Label(self.f23,text=value).place(x=self.x2+(170),y=self.y2)
          self.y2=self.y2+(30)
      self.textinput15aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input15aa,justify='center').place(x=720,y=50)
      self.textinput16aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input16aa,justify='center').place(x=720,y=80)
      self.textinput17aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input17aa,justify='center').place(x=720,y=110)
      self.textinput18aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input18aa,justify='center').place(x=720,y=140)
      self.textinput19aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input19aa,justify='center').place(x=720,y=170)
      self.textinput20aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input20aa,justify='center').place(x=720,y=200)
      self.textinput21aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input21aa,justify='center').place(x=720,y=230)
      self.textinput22aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input22aa,justify='center').place(x=720,y=260)
      self.textinput23aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input23aa,justify='center').place(x=720,y=290)
      self.textinput24aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input24aa,justify='center').place(x=720,y=320)
      self.textinput25aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input25aa,justify='center').place(x=720,y=350)
      self.textinput26aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input26aa,justify='center').place(x=720,y=380)
      self.textinput27aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input27aa,justify='center').place(x=720,y=410)
      self.textinput28aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input28aa,justify='center').place(x=720,y=440)
    def alfatora(self):
       self.textfatora=Label(self.f1,text="[الفواتير]",font=("arial",13,"bold"),fg="gold",bg=self.backgroundcolor).place(x=1157,y=200)
       self.F5 = Frame(self.window,bd=0,width=220,bg='white',height=200)
       self.F5.place(x=1016,y=220)
       scrol_y= Scrollbar(self.F5,orient=VERTICAL)
       self.txtarea=Text(self.F5,yscrollcommand=scrol_y.set)
       scrol_y.pack(side=LEFT,fill=Y)
       scrol_y.config(command=self.txtarea.yview)
       self.txtarea.pack(fill=BOTH,expand=1)
       self.txtarea.insert(END,"\tسوبر ماركت الخبير يرحب بكم")
       self.txtarea.insert(END,"\n  ====================================")
       self.txtarea.insert(END,f"\n\t B.NUM  : ")
       self.txtarea.insert(END,f"\n\t Name   : {self.name_store.get()}")
       self.txtarea.insert(END,f"\n\t Phone  : {self.phone_store.get()}")
       self.txtarea.insert(END,"\n======================================")
       self.txtarea.insert(END,f"\nالسعر\t      العدد\t       المشتريات ")
       self.txtarea.insert(END,"\n======================================")
       
    def billing(self):
        if self.name_store.get()=="" or self.phone_store.get()=="":
            messagebox.showerror("حدث خطأ","لا يجوز ترك حقل الاسم ورقم الهاتف فارغا")
        elif self.hotdrink.get()=="0.0 $" and self.sandwitch.get()=="0.0 $" and self.dishes.get()=="0.0 $":
            messagebox.showerror("حدث خطأ"," ليس هناك منتجات محددة ولم يتم اختيار احداها يجب اختيار عدد المنتجات")
        else:
            self.alfatora()
            if self.value_input1.get()!=0:
                 self.txtarea.insert(END,f"\n {self.price1}\t\t{self.value_input1.get()}\t\tbeefburger cheese")
            if self.value_input2.get()!=0:
                self.txtarea.insert(END,f"\n {self.price2}\t\t{self.value_input2.get()}\t\tchicken burger")
            if self.value_input3.get()!=0:
                self.txtarea.insert(END,f"\n {self.price3}\t\t{self.value_input3.get()}\t\tbeefburger special")
            if self.value_input4.get()!=0:
                self.txtarea.insert(END,f"\n {self.price4}\t\t{self.value_input4.get()}\t\tchawarma pain ")
            if self.value_input5.get()!=0:
                self.txtarea.insert(END,f"\n {self.price5}\t\t{self.value_input5.get()}\t\tchawarma raghif")
            if self.value_input6.get()!=0:
                self.txtarea.insert(END,f"\n {self.price6}\t\t{self.value_input6.get()}\t\tchawarma special")
            if self.value_input7.get()!=0:
                self.txtarea.insert(END,f"\n {self.price7}\t\t{self.value_input7.get()}\t\tchawarma garnie ")
            if self.value_input8.get()!=0:
                self.txtarea.insert(END,f"\n {self.price8}\t\t{self.value_input8.get()}\t\tsouffle poulet")
            if self.value_input9.get()!=0:
                self.txtarea.insert(END,f"\n {self.price9}\t\t{self.value_input9.get()}\t\tsouffle viande")
            if self.value_input10.get()!=0:
                self.txtarea.insert(END,f"\n {self.price10}\t\t{self.value_input10.get()}\t\tsouffle mixte")
            if self.value_input11.get()!=0:
                self.txtarea.insert(END,f"\n {self.price11}\t\t{self.value_input11.get()}\t\tsouffle merguaz")
            if self.value_input12.get()!=0:
                self.txtarea.insert(END,f"\n {self.price12}\t\t{self.value_input12.get()}\t\tsouffle garnie")
            if self.value_input13.get()!=0:
                self.txtarea.insert(END,f"\n {self.price13}\t\t{self.value_input13.get()}\t\tmalfouf special")
            if self.value_input14.get()!=0:
                self.txtarea.insert(END,f"\n {self.price14}\t\t{self.value_input14.get()}\t\tmalfouf poulet")
            if self.value_input15.get()!=0:
                self.txtarea.insert(END,f"\n {self.price15}\t\t{self.value_input15.get()}\t\tcrepe kepda")
            if self.value_input16.get()!=0:
                self.txtarea.insert(END,f"\n {self.price16}\t\t{self.value_input16.get()}\t\tcerpe viande")
            if self.value_input17.get()!=0:
                self.txtarea.insert(END,f"\n {self.price17}\t\t{self.value_input17.get()}\t\tcrepe chicken")
            if self.value_input18.get()!=0:
                self.txtarea.insert(END,f"\n {self.price18}\t\t{self.value_input18.get()}\t\tcorn mayo")
            if self.value_input19.get()!=0:
                self.txtarea.insert(END,f"\n {self.price19}\t\t{self.value_input19.get()}\t\tcorn cheese")
            if self.value_input20.get()!=0:
                self.txtarea.insert(END,f"\n {self.price20}\t\t{self.value_input20.get()}\t\tcorn lays mayo")
            if self.value_input21.get()!=0:
                self.txtarea.insert(END,f"\n {self.price21}\t\t{self.value_input21.get()}\t\tcorn lays cheese")
            if self.value_input22.get()!=0:
                self.txtarea.insert(END,f"\n {self.price22}\t\t{self.value_input22.get()}\t\tcorn mayp tomato")
            if self.value_input23.get()!=0:
                self.txtarea.insert(END,f"\n {self.price23}\t\t{self.value_input23.get()}\t\tveg mayo crilled")
            if self.value_input24.get()!=0:
                self.txtarea.insert(END,f"\n {self.price24}\t\t{self.value_input24.get()}\t\tveg club cheese")
            if self.value_input25.get()!=0:
                self.txtarea.insert(END,f"\n {self.price25}\t\t{self.value_input25.get()}\t\tveg crilled sandwitch")
            if self.value_input26.get()!=0:
                self.txtarea.insert(END,f"\n {self.price26}\t\t{self.value_input26.get()}\t\tveg sandwitch")
            if self.value_input27.get()!=0:
                self.txtarea.insert(END,f"\n {self.price27}\t\t{self.value_input27.get()}\t\tbhujia sandwitch crill")
            if self.value_input28.get()!=0:
                self.txtarea.insert(END,f"\n {self.price28}\t\t{self.value_input28.get()}\t\tbhujia sandwitch cheese")
                
            if self.value_input1a.get()!=0:
                 self.txtarea.insert(END,f"\n {self.price1a}\t\t{self.value_input1a.get()}\t\tchawarema")
            if self.value_input2a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price2a}\t\t{self.value_input2a.get()}\t\tcorden bleu")
            if self.value_input3a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price3a}\t\t{self.value_input3a.get()}\t\tscalope creme")
            if self.value_input4a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price4a}\t\t{self.value_input4a.get()}\t\tballes grill ")
            if self.value_input5a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price5a}\t\t{self.value_input5a.get()}\t\tpoulet marine")
            if self.value_input6a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price6a}\t\t{self.value_input6a.get()}\t\tfried wings")
            if self.value_input7a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price7a}\t\t{self.value_input7a.get()}\t\tlemon paper wings")
            if self.value_input8a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price8a}\t\t{self.value_input8a.get()}\t\tjerk wings")
            if self.value_input9a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price9a}\t\t{self.value_input9a.get()}\t\tcreole wings")
            if self.value_input10a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price10a}\t\t{self.value_input10a.get()}\t\tfish filet")
            if self.value_input11a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price11a}\t\t{self.value_input11a.get()}\t\tGriot")
            if self.value_input12a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price12a}\t\t{self.value_input12a.get()}\t\tGrilled chicken")
            if self.value_input13a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price13a}\t\t{self.value_input13a.get()}\t\tcreole shrimp")
            if self.value_input14a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price14a}\t\t{self.value_input14a.get()}\t\tfried shrimp")
            if self.value_input15a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price15a}\t\t{self.value_input15a.get()}\t\tsteamed shrip")
            if self.value_input16a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price16a}\t\t{self.value_input16a.get()}\t\toxtail")
            if self.value_input17a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price17a}\t\t{self.value_input17a.get()}\t\tfried conch")
            if self.value_input18a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price18a}\t\t{self.value_input18a.get()}\t\tGrill conch")
            if self.value_input19a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price19a}\t\t{self.value_input19a.get()}\t\tslew conch")
            if self.value_input20a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price20a}\t\t{self.value_input20a.get()}\t\tfried fish")
            if self.value_input21a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price21a}\t\t{self.value_input21a.get()}\t\tlobster tail")
            if self.value_input22a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price22a}\t\t{self.value_input22a.get()}\t\tcrabe creole")
            if self.value_input23a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price23a}\t\t{self.value_input23a.get()}\t\tstew chicken")
            if self.value_input24a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price24a}\t\t{self.value_input24a.get()}\t\tGrilled chicken")
            if self.value_input25a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price25a}\t\t{self.value_input25a.get()}\t\tstew fish")
            if self.value_input26a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price26a}\t\t{self.value_input26a.get()}\t\tfried pork")
            if self.value_input27a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price27a}\t\t{self.value_input27a.get()}\t\tsteamed conch")
            if self.value_input28a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price28a}\t\t{self.value_input28a.get()}\t\tcolombo")
                
            self.txtarea.insert(END,"\n......................................")
            self.txtarea.insert(END,f"\n\t{self.sandwitch+self.dishes+self.hotdrink} $\t     المجموع الكلي")
            self.txtarea.insert(END,"\n......................................")
            
    
    
    def calculate_price(self):
        self.sandwitch=StringVar()
        self.sandwitch.set("00")
        self.dishes=StringVar()
        self.dishes.set("00")
        self.hotdrink=StringVar()
        self.hotdrink.set("00")
        f3=Frame(width=1360,height=100,bg=self.backgroundcolor).place(x=0,y=600)
        self.button_1=Button(text="الحساب",bg=self.color_button,width=10,borderwidth=2,cursor="hand2",font=("arial",13,"bold"),command=self.calculate_drink).place(x=1225,y=620)
        self.button_2=Button(text="افراغ الحقول",bg=self.color_button,width=10,borderwidth=2,cursor="hand2",font=("arial",13,"bold")).place(x=1110,y=620)
        self.button_3=Button(text="تصدير الفاتوره",bg=self.color_button,width=10,borderwidth=2,cursor="hand2",font=("arial",13,"bold"),command=self.billing).place(x=1225,y=660)
        self.button_4=Button(text="اغلاق البرنامج",bg=self.color_button,width=10,borderwidth=2,cursor="hand2",font=("arial",13,"bold")).place(x=1110,y=660)
        self.text_price1=Label(text="حساب الكلي مشروبات",bg=self.backgroundcolor,fg=self.fontcolor,font=("arial",13,"bold")).place(x=880,y=630)
        self.input_price1=Entry(textvariable=self.hotdrink,bg=self.fontcolor,font=("arial",13,"bold"),width=12).place(x=750,y=630)
        self.text_price2=Label(text="حساب الكلي أطباق رئيسية",bg=self.backgroundcolor,fg=self.fontcolor,font=("arial",13,"bold")).place(x=550,y=630)
        self.input_price2=Entry(textvariable=self.dishes,bg=self.fontcolor,font=("arial",13,"bold"),width=12).place(x=420,y=630)
        self.text_price3=Label(text="حساب الكلي الستدويتشات",bg=self.backgroundcolor,fg=self.fontcolor,font=("arial",13,"bold")).place(x=220,y=630)
        self.input_price3=Entry(textvariable=self.sandwitch,bg=self.fontcolor,font=("arial",13,"bold"),width=12).place(x=90,y=630)
    
       
window=Tk()
my_class=super(window)
my_class.header()

my_class.calculate_price() 
my_class.choice()
my_class.drink()
my_class.drink2()
my_class.drink3()
#my_class.calculate_drink2()

#my_class.calculate_drink3()

my_class.data_customer("reham",18)

my_class.alfatora()

window.mainloop()