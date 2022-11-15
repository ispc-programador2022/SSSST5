import csv

with open('salida_productos.csv', newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row['Descripcion'],row['Año-Km'])
		     
