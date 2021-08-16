from tkinter import *
from PIL import ImageTk, Image
import socket

root = Tk()

root.title("Weather app")
root.geometry("471x750")

def show_weather():
    city = searchbar.get()
    s = socket.socket()
    s.connect(('192.168.1.13',7777))
    s.send(bytes(searchbar.get(),'utf-8'))
    temp = s.recv(1024).decode()
    s.close()

    info_frame = Frame(root,width = 300, height = 100,bg = "White")
    info_frame.place(relx = 0.2, rely = 0.5)
    city = city.capitalize()


    city_lable = Label(info_frame,text = city,bg = "White",font = ("bold",20)).place(x = 10, y = 10)
    temp_lable = Label(info_frame,text = temp+"°C",bg = "White",font = ("bold",20)).place(x = 180, y = 10)








bk = ImageTk.PhotoImage(Image.open("bk.jpg"))
bkl = Label(root,image = bk)
bkl.place(x = 0, y=0)



sf = Frame(root,bg = '#D0F3A1',height = 90, width = 300,bd = 1000)
#sf.place(x = 100, y = 100)

search_mir = Image.open("search_image.jpg")
resized = search_mir.resize((280,100),Image.ANTIALIAS)
search_image = ImageTk.PhotoImage(resized)

search_image_l = Label(root,image = search_image)

search_image_l.place(x = 100, y = 100)





search_l = Label(root,text =  "Enter city:",bg = '#ffffff')
search_l.place(x = 125, y = 125)

searchbar = Entry(root,bg = '#A1F3C9')
searchbar.place(x = 125, y = 150,)

searchb = Button(root,text = 'search',command = show_weather)
searchb.place(x = 280,y = 145)



root.mainloop()