from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=20a01944eda34a13f4a4dcecfff77197").json()
    w_label1.config(text=data["weather"][0]["main"]) #the main is to be selected from the weather dictionary 
    wb_label1.config(text=data["weather"][0]["description"]) #changes are to be made in text
    temp_label1.config(text=str(data["main"]["temp"]-273.15))
    per_label1.config(text=data["main"]["pressure"])

win = Tk() #a class
win.title("Weather App")
win.config(bg="light blue")
win.geometry("500x570")

name_label=Label(win,text="Simple Weather App",
                 font=("Arial",25,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

city_name = StringVar()
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

com = ttk.Combobox(win,text="Simple Weather App",values=list_name,
                 font=("Arial",20,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)

w_label=Label(win,text="Weather Climate",
                 font=("Arial",10))
w_label.place(x=25,y=260,height=50,width=100)

w_label1=Label(win,text="",
                 font=("Arial",12))
w_label1.place(x=135,y=260,height=50,width=165)

wb_label=Label(win,text="Weather Description",
                 font=("Arial",8))
wb_label.place(x=25,y=330,height=50,width=100)

wb_label1=Label(win,text="",
                 font=("Arial",12))
wb_label1.place(x=135,y=330,height=50,width=165)

temp_label=Label(win,text="Temperature",
                 font=("Arial",12))
temp_label.place(x=25,y=400,height=50,width=100)

temp_label1=Label(win,text="",
                 font=("Arial",12))
temp_label1.place(x=135,y=400,height=50,width=165)

per_label=Label(win,text="Pressure",
                 font=("Arial",12))
per_label.place(x=25,y=470,height=50,width=100)

per_label1=Label(win,text="",
                 font=("Arial",12))
per_label1.place(x=135,y=470,height=50,width=165)

done_button=Button(win,text="Done",
                 font=("Arial",20,"bold"),command=data_get)

done_button.place(y=190,height=50,width=100,x=200)

win.mainloop() #continuously running the win 