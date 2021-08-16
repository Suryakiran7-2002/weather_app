import socket
import sqlite3 as sq
def add_data(add_city,add_temp):
    conn = sq.connect("weather_app_data.db")
    c = conn.cursor()

    c.execute("INSERT INTO WEATHER_DATA_final VALUES (:city,:temp)",
              {
                  'city' : add_city,
                  'temp' : add_temp
              }
              )

    conn.commit()
    conn.close()



def update_data(up_city,up_temp):

    conn = sq.connect("weather_app_data.db")
    c = conn.cursor()
    c.execute("UPDATE WEATHER_DATA_final SET temperature = ? where city = ?",(up_temp,up_city))

    conn.commit()
    conn.close()

def show_weather(city):

    conn = sq.connect("weather_app_data.db")
    c = conn.cursor()

    c.execute("SELECT * FROM WEATHER_DATA_final")

    full_data = c.fetchall()

    for i in range(len(full_data)):
        if full_data[i][0] == city:
            temp = str(full_data[i][1])
            break
    else:
        temp = "NO DATA FOUND"


    return temp



s = socket.socket()

s.bind(('192.168.1.13',7777))

s.listen(10)

while True:
    conn,addr = s.accept()
    print("connected to ",addr)
    if addr[0] == '192.168.1.2':
            option = conn.recv(3).decode()
            print(option)
            if option == 'add':
                city_len = conn.recv(1).decode()
                add_city = conn.recv(int(city_len)).decode()

                add_temp = conn.recv(2).decode()

                add_data(add_city,add_temp)
            elif option == 'upd':
                up_city_len = conn.recv(1).decode()

                up_city = conn.recv(int(up_city_len)).decode()

                up_temp = conn.recv(2).decode()

                print(up_city,up_temp)
                update_data(up_city,up_temp)
    else:
        city=conn.recv(1024).decode()
        temp = show_weather(city)
        conn.send(bytes(temp,"utf-8"))
        print(city,temp)
