import csv
import matplotlib.pyplot as plt

def promedios(suma, cantidad):
    promedios=suma//cantidad
    return promedios



separador=","
with open('salida_productos.csv', encoding="utf-8") as archivo:
    next(archivo) #Omito el encabezado del archivo
    Productos=[]
    for linea in archivo:
        linea=linea.rstrip("\n")  #quito el salto de línea
        columnas=linea.split(separador)
        precio=int(columnas[0])
        descripcion=columnas[1].lower() #pongo la descripción todo en minúsculas
        año=int(columnas[2])
        km=int(columnas[3])
        
        Productos.append({
            "precio":precio,
            "descripcion":descripcion,
            "año": año,
            "km":km,  
            
        })

#print(Productos)

suma1=0
suma2=0
suma3=0
suma4=0
suma5=0
suma6=0

autos_menor_15=0
autos_15_25=0
autos_25_35=0
autos_35_50=0
autos_50_65=0
autos_mayor_65=0


for producto in Productos:
    precio_auto = producto["precio"]
    if precio_auto>500000 and precio_auto<=1500000:
        suma1+=precio_auto
        autos_menor_15+=1
    elif precio_auto > 1500000 and precio_auto <= 2500000:
        suma2+=precio_auto
        autos_15_25+=1  
    elif precio_auto  > 2500000 and precio_auto <= 3500000:
        suma3+=precio_auto
        autos_25_35+=1
    elif precio_auto > 3500000 and  precio_auto <= 5000000:
        suma4+=precio_auto
        autos_35_50+=1
        
    elif precio_auto > 5000000 and precio_auto <= 6500000:
        suma5+=precio_auto
        autos_50_65+=1
        
    elif precio_auto>6500000 and precio_auto <=8000000:
        suma6+=precio_auto
        autos_mayor_65+=1
total_autos=autos_menor_15+autos_15_25+autos_25_35+autos_35_50+autos_50_65+autos_mayor_65


#Muestra cantidad de autos por rango de precio:
print("La cantidad de autos cuyo valor es menor a 1500000 son: ",autos_menor_15)
print("La cantidad de autos con precio entre 1500000 y 2500000 son: ",autos_15_25)
print("La cantidad de autos con precio entre 2500000 y 3500000 son: ",autos_25_35)
print("La cantidad de autos con precio entre 3500000 y 5000000 son: ",autos_35_50)
print("La cantidad de autos con precio entre 5000000 y 6500000 son: ",autos_50_65)
print("La cantidad de autos con precio mayor a 6500000 son: ",autos_mayor_65)
print("\nEl scrapping se realizo sobre 500 autos ")
print("Algunos datos no sirvieron ya que no reflejaban el precio que es un dato crucial para nuestro análisis")
print("La cantidad total de autos que sirvieron para el análisis son: ",total_autos)

#Valores promedios por rangos:

print("\nEl precio promedio de los autos menores o iguales a $1500000 es: $",promedios(suma1, autos_menor_15))
print("\nEl precio promedio de los autos entre $1500000 y $2500000 es: $",promedios(suma2, autos_15_25))
print("\nEl precio promedio de los autos entre $2500000 y $3500000 es: $",promedios(suma3, autos_25_35))
print("\nEl precio promedio de los autos entre $3500000 y $5000000 es: $",promedios(suma4, autos_35_50))
print("\nEl precio promedio de los autos entre $5000000 y $6500000 es: $",promedios(suma5, autos_50_65))
print("\nEl precio promedio de los autos mayores a $6500000 es: ",promedios(suma6,autos_mayor_65))


#Análisis en función del modelo:

modelo_99_05=0
modelo_06_10=0
modelo_11_15=0
modelo_16_22=0
modelo_xx_98=0

for producto in Productos:
    precio_auto = producto["precio"]
    año_auto=producto["año"]
    if (precio_auto>500000) and  (precio_auto<=8000000):
        if año_auto>=1999 and año_auto<2006:
            modelo_99_05+=1
        elif año_auto>=2006 and año_auto<2011:
            modelo_06_10+=1
        elif año_auto>=2011 and año_auto<2016:
            modelo_11_15+=1
        elif año_auto>=2016 and año_auto<=2022:
            modelo_16_22+=1
        else:
            modelo_xx_98+=1

#print("Cantidad de autos analizados: ",modelo_xx_98+modelo_99_05+modelo_06_10+modelo_11_15+modelo_16_22)
print("La cantidad de autos menores al año 99 son: ",modelo_xx_98)
print("La cantidad de autos modelo 99-05 son: ", modelo_99_05)
print("La cantidad de autos modelo 06-10 son: ", modelo_06_10)
print("La cantidad de autos modelo 11-15 son: ", modelo_11_15)
print("La cantidad de autos modelo 16-22 son: ", modelo_16_22)

#Gráfico porcentajes según los rangos precios de Autos
cantidad_autos_por_rango=[autos_menor_15,autos_15_25,autos_25_35,autos_35_50,autos_50_65,autos_mayor_65]
nombres=["<=1.5M",">1.5M-<=2.5M",">2.5M-<=3.5M",">3.5M-<=5M",">5M-<=6.5M",">6.5M"]
plt.pie(cantidad_autos_por_rango, labels=nombres,autopct="%0.1f%% ")
plt.title("Porcentajes cantidad de autos según los rangos de precios: \n Análisis con respecto a 417 autos ")
plt.axis("equal")
plt.savefig("Porcentajes autos.png") 
plt.show()

#Gráfico Capacidad de Ahorro
Modelo_año=[modelo_xx_98,modelo_99_05,modelo_06_10,modelo_11_15,modelo_16_22]
nombres=["-1998","1999-2005","2006-2010","2011-2015","2016-2022"]
fig, ax=plt.subplots()
#Etiqueta en eje Y
ax.set_ylabel("Cantidad")
#Etiqueta en eje X
ax.set_title("Autos por rango de modelo")
plt.bar(nombres, Modelo_año,color='turquoise')
plt.savefig("Autos_por_año.png")
plt.show()



dictPrecios_Año={'cantidad_autos':total_autos,
                 "precio_menor_1.5":autos_menor_15,
                 "precio_1.5-2.5":autos_15_25,
                 "precio_2.5-3.5":autos_25_35,
                 "precio_3.5-5":autos_35_50,
                 "precio_5-6.5":autos_50_65,
                 "precio_6.5":autos_mayor_65,
                 "prom_menor1.5":promedios(suma1, autos_menor_15),
                 "prom_1.5-2.5":promedios(suma2, autos_15_25),
                 "prom_2.5-3.5":promedios(suma3, autos_25_35),
                 "prom_5-6.5":promedios(suma5, autos_50_65),
                 "prom_mayor6.5":promedios(suma6,autos_mayor_65),
                 "mod_menor_99":modelo_xx_98,
                 "mod_99_05":modelo_99_05,
                 "mod_06_10":modelo_06_10,
                 "mod_11_15":modelo_11_15,
                 "mod_16_22":modelo_16_22,

            }           
    

#Creación del archivo CSV con los datos del análisis de los modelos de auto
with open('dictPrecios_año.csv','w')as f:
    writer=csv.writer(f)
    for k,v in dictPrecios_Año.items():
        writer.writerow([k,v])


       
       
        
   
