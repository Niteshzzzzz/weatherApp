from tkinter import *
from tkinter import messagebox
root=Tk()
root.title('Weather App')
root.geometry("350x350")
def weatherinfo():
    import requests
    city_name=e1.get()
    API_key="9b23d34fbc390b814ff6ae89d1651899"
    ws=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}")
    if ws.json()['cod']=='404':
        msg()
    else:
        n1.config(text=f"Weather is: {ws.json()['weather'][0]['main']}")
        n2.config(text=f"Temp is: {ws.json()['main']['temp']}k")
        n3.config(text=f"Pressure is: {ws.json()['main']['pressure']} atm")
        n4.config(text=f"Humidity is: {ws.json()['main']['humidity']}%")
        n5.config(text=f"Wind speed is: {ws.json()['wind']['speed']} mph")
def msg():
    messagebox.showinfo("Weather Status","City name is not found")
l1=Label(root,text='Enter City Name: ')
l1.grid(row=0,column=0)
e1=Entry(root)
e1.grid(row=0,column=2)
b1=Button(root,text='Get Weather',command=weatherinfo)
b1.grid(row=0,column=3)
n1=Label(root)
n1.grid(row=1,column=2)
n2=Label(root)
n2.grid(row=2,column=2)
n3=Label(root)
n3.grid(row=3,column=2)
n4=Label(root)
n4.grid(row=4,column=2)
n5=Label(root)
n5.grid(row=5,column=2)
root.mainloop()