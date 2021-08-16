from tkinter import *
import sqlite3 as sq

root = Tk()

def add_data():
    conn = sq.connect("weather_app_data.db")
    c = conn.cursor()

    c.execute("INSERT INTO WEATHER_DATA_final VALUES (:city,:temp)",
              {
                  'city' : add_city_e.get(),
                  'temp' : add_temp_e.get()
              }
              )

    conn.commit()
    conn.close()

    add_city_e.delete(0, END)
    add_temp_e.delete(0, END)

def update_data():
    up_city = up_city_e.get()
    up_temp = up_temp_e.get()
    conn = sq.connect("weather_app_data.db")
    c = conn.cursor()
    c.execute("UPDATE WEATHER_DATA_final SET temperature = ? where city = ?",(up_temp,up_city))

    conn.commit()
    conn.close()


    up_city_e.delete(0,END)
    up_temp_e.delete(0,END)





add_data_frame = Frame(root,width = 100,height = 100)
add_data_frame.grid(row = 0,column=0)


add_city_l = Label(add_data_frame,text = 'City').pack()
add_city_e = Entry(add_data_frame)
add_city_e.pack()

add_temp_l = Label(add_data_frame,text = "Temperature").pack()
add_temp_e = Entry(add_data_frame)
add_temp_e.pack()
add_data_button = Button(add_data_frame,text = "ADD DATA",command = add_data).pack()

update_data_frame = Frame(root,width = 100,height = 100)
update_data_frame.grid(row = 0,column = 1,padx = 50)

up_city_l = Label(update_data_frame,text = 'City').pack()
up_city_e = Entry(update_data_frame)
up_city_e.pack()

up_temp_l = Label(update_data_frame,text = "Temperature").pack()
up_temp_e = Entry(update_data_frame)
up_temp_e.pack()

update_data_button = Button(update_data_frame,text = "UPDATE DATA",command = update_data).pack()


root.mainloop()
