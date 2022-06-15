# -*- coding: utf-8 -*-
"""
Created on Mon May  9 16:37:07 2022

@author: Beautiful Mishika
"""

# -*- coding: utf-8 -*-
"""
Created on Mon May  9 16:08:02 2022

@author: Beautiful Mishika
"""

from tkinter import *
import random 

root=Tk()
root.title("Country and Capitals")
root.geometry("400x400")

enter_country = Entry(root)
enter_country.place(relx=0.5, rely=0.2, anchor=CENTER)

enter_capital = Entry(root)
enter_capital.place(relx=0.5, rely=0.3, anchor=CENTER)

country_list = Label(root)
capital_list = Label(root)

random_country_label = Label(root)
random_capital_label = Label(root)

country_list = []
capital_list = []

def countrylist():
    country = enter_country.get()
    country_list.append(country)
    country_list["text"] = "The Country Names : " + str(country_list)
    
    capital = enter_capital.get()
    capital_list.append(capital)
    capital_list["text"] = "The Capital Names : " + str(capital_list)
    
def random_country_capital():
    length1= len(country_list)
    length2= len(capital_list)
    
    random_no1 = random.randint(0, length1-1)
    random_no2 = random.randint(0, length2-1)
    
    random_country = country_list[random_no1]
    random_capital = capital_list[random_no2]
    
    random_country_label["text"] = "Random Country : " + str(random_country)
    random_capital_label["text"] = "Random Capital : " + str(random_capital)
    
btn = Button(root, text="Display Country and Capital name ", command=countrylist)
btn.place(relx=0.5, rely=0.4, anchor=CENTER)

country_list.place(relx=0.5, rely=0.5, anchor=CENTER)
capital_list.place(relx=0.5, rely=0.6, anchor=CENTER)

btn1=Button(root, text="Display Random Country and Capital name", command=random_country_capital)
btn1.place(relx=0.5, rely=0.7, anchor=CENTER)

random_country_label.place(relx=0.5, rely=0.8, anchor=CENTER)
random_capital_label.place(relx=0.5, rely=0.9, anchor=CENTER)

root.mainloop()