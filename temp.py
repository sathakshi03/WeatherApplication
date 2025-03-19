from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    try:
        response = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=b31c90c035ef5819e0ebc3aaff634ec1")
        data = response.json()

        # Check for errors in the response
        if response.status_code != 200 or 'weather' not in data:
            w_label1.config(text="Error: " + data.get("message", "Invalid response"))
            wd_label1.config(text="")
            temp_label1.config(text="")
            per_label1.config(text="")
            return

        # Update the labels with the data from the API
        w_label1.config(text=data["weather"][0]["main"])
        wd_label1.config(text=data["weather"][0]["description"])    
        temp_label1.config(text=str(int(data["main"]["temp"]-273.15))) 
        per_label1.config(text=data["main"]["pressure"])
    except Exception as e:
        # Handle any unexpected errors
        w_label1.config(text="Error: " + str(e))




win = Tk()    #for window
win.title("WEATHER") #window title
win.config(bg = "LightCyan") #background color for window
win.geometry("500x570") # for window(box) width and height

name_label = Label(win,text = "Weather App",
                   font = ("Time New Roman",40,"bold"))
name_label.place(x=25 , y=50 , height=50, width=450)


city_name = StringVar()
list_name = ["Srikakulam","Vizianagaram	","Visakhapatnam","Kakinada","Eluru","Guntur","Bapatla","Kurnool","Nandyal","Tirupati","Chittoor","Hindupur","Proddatur","Tenali","Adoni","Machilipatnam","Ongole","Anantapur","Kadapa","Nellore"]
com = ttk.Combobox(win,text = "Weather App",values = list_name,
                   font = ("Time New Roman",25,"bold"),textvariable = city_name)  #for getting the options to select the places what ever we want
com.place(x=20 , y=120 , height=50, width=450)



w_label = Label(win,text = "Weather Climate",
                   font = ("Time New Roman",20))
w_label.place(x=25 , y=260 , height=50, width=210)
w_label1 = Label(win,text = "",
                   font = ("Time New Roman",20))
w_label1.place(x=250 , y=260 , height=50, width=210)



wd_label = Label(win,text = "Weather Description",
                   font = ("Time New Roman",17))
wd_label.place(x=25 , y=330 , height=50, width=210)
wd_label1 = Label(win,text = "",
                   font = ("Time New Roman",17))
wd_label1.place(x=250 , y=330 , height=50, width=210)



temp_label = Label(win,text = "Temperature",
                   font = ("Time New Roman",20))
temp_label.place(x=25 , y=400 , height=50, width=210)
temp_label1 = Label(win,text = "",
                   font = ("Time New Roman",20))
temp_label1.place(x=250 , y=400 , height=50, width=210)



per_label = Label(win,text = "Pressure",
                   font = ("Time New Roman",20))
per_label.place(x=25 , y=470 , height=50, width=210)
per_label1 = Label(win,text = "",
                   font = ("Time New Roman",20))
per_label1.place(x=250 , y=470 , height=50, width=210)



done_button = Button(win,text = "DONE",
                   font = ("Time New Roman",20,"bold"),command=data_get)
done_button.place(y=190, height=50, width=100, x=200) 

win.mainloop()