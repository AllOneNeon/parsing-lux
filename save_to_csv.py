import pymssql
import csv

conn = pymssql.connect(server='103.24.99.76', 
                        user='testUser', 
                        password='Abcd.1234', 
                        database='Portal_Data')

cursor = conn.cursor()
cursor.execute("""SELECT *
                FROM sys.databases 
                WHERE name = 'Portal_Data'
                """)
                
rows = cursor.fetchall()
with open('data.csv', 'w', newline='\r\n') as csvfile:
    csvfile.seek(0)
    a = csv.writer(csvfile)
    a.writerows(rows)
