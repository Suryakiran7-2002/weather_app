import sqlite3 as sq

conn = sq.connect("weather_app_data.db")
c = conn.cursor()

c.execute("""CREATE TABLE WEATHER_DATA_final
        (city text,
        temperature int);
""")

conn.commit()
conn.close()
