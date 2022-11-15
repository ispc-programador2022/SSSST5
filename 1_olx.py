
import random
from time import sleep
from selenium import webdriver 


driver = webdriver.Chrome('./chromedriver.exe') #  NOMBRE DE TU CHROME DRIVER

driver.get('https://www.olx.com.ar/autos_c378')
driver.maximize_window()
sleep(3)
driver.refresh() # Solucion  donde los anuncios solo cargan al hacerle refresh o al darle click a algun elemento
sleep(5) # Esperamos que cargue el boton
# Busco el boton para cargar mas informacion
boton = driver.find_element("xpath",'//button[@data-aut-id="btnLoadMore"]')
for i in range(20): 
    try:
        # le doy click
        boton.click()
        # espero que cargue la informacion dinamica lo hago random para que no crea q es un robot
        sleep(random.uniform(8.0, 10.0))
        # busco el boton nuevamente para darle click en la siguiente iteracion
        boton = driver.find_element("xpath",'//button[@data-aut-id="btnLoadMore"]')
    except:
        # si hay algun error, rompo el lazo. 
        break

# Encuentro cual es el XPATH de cada elemento donde esta la informacion que quiero extraer
# Esto es una LISTA. Por eso el metodo esta en plural
lista_precios=[]
lista_descripcion=[]

lista_año_km=[]

autos = driver.find_elements("xpath",'//li[@data-aut-id="itemBox"]')


# Recorro cada uno de los anuncios 
for auto in autos:
    # Precio por cada anuncio
    precio = auto.find_element("xpath",'.//span[@data-aut-id="itemPrice"]').text
    lista_precios.append(precio)
    #print (precio)
    # Descripción de cada anuncio
    descripcion = auto.find_element("xpath",'.//span[@data-aut-id="itemTitle"]').text
    lista_descripcion.append(descripcion)
    #print (descripcion)
    año_km=auto.find_element("xpath",'.//span[@data-aut-id="itemDetails"]').text
    lista_año_km.append(año_km)
driver.quit()
año=[]
km=[]
for i in lista_año_km:
    lista=i.split('-')
    año.append(lista[0])
    km.append(lista[1])
#print(lista_precios)
#print(lista_descripcion)
mi_diccionario={'Precio':lista_precios, 'Descripcion':lista_descripcion,'Año':año,'Km':km}
#print(mi_diccionario)


import pandas as pd
df=pd.DataFrame(mi_diccionario,columns=['Precio','Descripcion','Año','Km'])
print(df)
df.to_csv('salida_productos.csv',index=False)
