#pegar despues del driver.quit 

año = []
km = []
for i in lista_año_km:
    lista = i.split('-')
    año.append(lista[0])
    km.append(lista[1])
#print(año, km)
#Agregamos al diccinonario las columnas año km
mi_diccionario={'Precio':lista_precios, 'Descripcion':lista_descripcion,'Año':año, 'Km':km}
