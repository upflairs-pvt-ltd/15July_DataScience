import sqlite3 
conn = sqlite3.connect("bikedata.db") 

cur = conn.cursor() 
query = "select * from BikeDetails"

cur.execute(query) 
for record in cur.fetchall():
    print(record) 

cur.close()
conn.close() 