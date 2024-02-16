import tkinter
from tkinter import *

window = Tk()
window.title("BMI Calculater")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width / 2) - 200
y = (screen_height / 2) - 200
window.geometry('%dx%d+%d+%d' % (200, 200, x, y))
# window.geometry('400x100+960+540')
# window.minsize(width=200, height=200)
window.columnconfigure(0, minsize=200)
window.rowconfigure([1, 1], minsize=30)

window.resizable(0,0)
window.attributes('-toolwindow', 1)
window.attributes('-')
window.focus()
window.attributes("-topmost", 1)


def Calculated(event=None):
    kg = my_entry_kg.get()
    cm = my_entry_cm.get()
    if (kg.isdecimal() and cm.isdecimal()):
        result = int(kg) / ((int(cm)/100) ** 2)
        if result < 18.5:
            my_result.config(text=f"{result:.1f} => (Zayıf)", fg='red', font=('Arial', 12, 'bold'))
        elif 18.5 < result <= 24.9:
            my_result.config(text=f"{result:.1f} => (Normal Kilo)", fg='red', font=('Arial', 12, 'bold'))
        elif 25.0 < result <= 29.9:
            my_result.config(text=f"{result:.1f} => (Fazla Kilo)", fg='red', font=('Arial', 12, 'bold'))
        elif 30.0 < result <= 34.9:
            my_result.config(text=f"{result:.1f} => (1. Derece Obez)", fg='red', font=('Arial', 12, 'bold'))
        elif 35.0 < result <= 39.9:
            my_result.config(text=f"{result:.1f} => (2. Derece Obez)", fg='red', font=('Arial', 12, 'bold'))
        elif result >= 40:
            my_result.config(text=f"{result:.1f} => (Morbid Obez)", fg='red', font=('Arial', 12, 'bold'))
        else:
            my_result.config(text="Değer Dışında", fg='red', font=('Arial', 12, 'bold'))
    else:
        my_result.config(text="Yanlış Değer girdiniz.", fg='red', font=('Arial', 9, 'bold'))

def kg():
    pass

def boy():
    pass

my_label_kg = Label(text="Vücut Ağırlığınızı Giriniz (kg)")
#my_label_kg.config(padx=10, pady=10)
#my_label_kg.pack()
my_label_kg.grid(row = 0, column = 0, sticky = 'n', pady=5)
# my_label_kg.place(x=25, y=10)

my_entry_kg = Entry(width=20)
#my_entry_kg.pack()
my_entry_kg.grid(row = 1, column = 0, sticky = 'n')
# my_entry_kg.place(x=35, y=35)

my_label_cm = Label(text="Boyunuzu Giriniz (cm)")
# my_label_cm.config(padx=10, pady=10)
#my_label_cm.pack()
my_label_cm.grid(row = 2, column = 0, sticky = 'n', pady=5)
# my_label_cm.place(x=35, y=70)

my_entry_cm = Entry(width=20)
#my_entry_cm.pack()
my_entry_cm.grid(row = 3, column = 0, sticky = 'n')
# my_entry_cm.place(x=35, y=95)

window.bind('<Return>', Calculated)

my_button_calc = Button(text="Hesapla", command=Calculated)
#my_button_calc.pack()
my_button_calc.grid(row = 4, column = 0, sticky = 'n', pady=10)
# my_button_calc.place(x=65, y=130)

my_result = Label()
my_result.grid(row = 5, column = 0, sticky = 'n', pady=10)

window.mainloop()