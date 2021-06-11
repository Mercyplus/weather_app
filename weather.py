import requests
from tkinter import *
from tkinter import messagebox


font_style = ('Montserrat Alternates Regular', 10)
font_hel = 'Helvetica 12 bold'


api_key = "b6ed6621a1ca74982e51281fd1b33f00"


def Author():
    created = Toplevel()
    created.geometry('300x200')
    created.title('Автор')
    Label(created, text='Версия: 1.0', font=font_style).grid(row=1, column=3)
    Label(created, text='Разработчик: Mercyplus', font=font_hel).grid(row=2, column=2)


def proceed():
    city = cit.get()
    if not city or is_int(city) or city == '':
        return messagebox.showerror('Ошибка', 'Введите город')
    elif api_key == 'your api key':
        return messagebox.showerror('Ошибка', 'Введите свой api-ключ')

    else:
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        cityname = city
        complete_url = base_url + "appid=" + api_key + "&q=" + cityname
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":

            y = x["main"]
            current_temp = y["temp"]
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            Label(home, text='Температура: ' + str(round(current_temp - 272.15)) + ' °C').place(x=5, y=130)
            Label(home, text='Атмосферное давление: ' + str(int(current_pressure / 1.33)) + ' мм рт.ст.').place(x=5, y=170)
            Label(home, text='Влажность: ' + str(current_humidity) + ' %').place(x=5, y=210)
        else:
            return messagebox.showerror('Ошибка', 'Город не найден')


def is_int(value):
    try:
        int(value)
        return True
    except:
        return False


home = Tk()
home.geometry('400x400')
home.title('Weather App')
home.resizable(False, False)
cit = StringVar()

Label(home, text='Погодное приложение', font='Helvetica 12 bold').place(x=100, y=6)
Button(home, text='Автор', font=font_style, command=Author, background="#555", foreground="#fff").place(x=320, y=6)
Label(home, text='Введите город:', font=font_style).place(x=5, y=70)
Entry(home, width=20, textvariable=cit).place(x=150, y=70)
Button(home, text='Узнать', font=font_style, command=proceed, background="#555", foreground="#fff").place(x=320, y=70)


home.mainloop()
