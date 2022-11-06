import mysql.connector
from mysql.connector import Error
import re
import csv

try:
	connection = mysql.connector.connect(host='localhost',
                                         database='proyecto',
                                         user='sssst4',
                                         password='contrasena')
	if connection.is_connected():
		db_Info = connection.get_server_info()
		print("Connected to MySQL Server version ", db_Info)
		cursor = connection.cursor()
		with open('salida_productos.csv', newline='') as csvfile:
			reader = csv.DictReader(csvfile)        
			for row in reader:
				rr=re.findall(r'\d+.\d+',row['Precio'])
				cant = len(rr)
				if cant:
					if "USD" in row['Precio'] :
						precio=int(rr[0].replace(".",""))*158 
					else: 
						precio=int(rr[0].replace(".",""))     	
				print(precio,row['Descripcion'],row['Año-Km'])
				mySql_insert_query = """INSERT INTO autos (precio, descripcion, aniokm) VALUES (%s, %s, %s) """
				record = (precio,row['Descripcion'], row['Año-Km'])
				cursor.execute(mySql_insert_query, record)
				connection.commit()                

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


