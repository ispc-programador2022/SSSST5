
import csv
import matplotlib.pyplot as plt

def promedios(suma, cantidad):
    promedios=suma//cantidad
    return promedios

def ahorro (promedio):
    canasta=128214
    return (promedio - canasta)


separador=","
with open('escala_salarial.csv', encoding="utf-8") as archivo:
    next(archivo) #Omito el encabezado del archivo
    Salarios=[]
    for linea in archivo:
        linea=linea.rstrip("\n")  #quito el salto de línea
        columnas=linea.split(separador)
        cargo=columnas[0]


        liquidacion=int(columnas[1])
        
        Salarios.append({
            "cargo":cargo,
            "liquidacion":liquidacion,  
            
        })
   
#Análisis de intervalos de los sueldos:
cant_menor_igual_150=0
cant_150_y_300=0
cant_300_y_500=0
cant_mayor_500=0
suma1=0
suma2=0
suma3=0
suma4=0

for salario in Salarios:
    val_salario = salario["liquidacion"]

    if val_salario <= 150000:
        suma1+=val_salario
        cant_menor_igual_150+=1
        
        
    elif val_salario > 150000 and val_salario <= 300000:
        cant_150_y_300+=1
        suma2+=val_salario
        

    elif val_salario > 300000 and val_salario <= 500000:
        cant_300_y_500+=1
        suma3+=val_salario
        
    else:
        cant_mayor_500+=1
        suma4+=val_salario
        
total_sueldos=cant_menor_igual_150+cant_150_y_300+cant_300_y_500+cant_mayor_500
print("\n LA CANTIDAD TOTAL DE SALARIOS ANALIZADOS ES: ", total_sueldos,"\n")


#Intervalos sueldos menores a $150000
print ("\nLa cantidad de sueldos menores a 150000 son: ",cant_menor_igual_150)

print("\nEl sueldo promedio entres los sueldos menores o iguales a $150000 es: $",promedios(suma1, cant_menor_igual_150), "por lo que su capacidad de ahorro es nula \n, ya que no cubre el monto de la canasta básica ($128.214)")

#Intervalos sueldos comprendidos entre 150000 y 300000
print("\nLa cantidad de sueldos mayores a 150000 y menores o iguales a 300000 son: ",cant_150_y_300)

prom_150_300=promedios(suma2, cant_150_y_300)
print("\nEl sueldo promedio entres los sueldos entres $150000 y $300000 es: $",prom_150_300)
print("\nLa capacidad de ahorro mensual de este grupo es: $",ahorro(prom_150_300))

#Intervalos sueldos comprendidos entre 300000 y 500000
print("\nLa cantidad de sueldos mayores a 300000 y menores o iguales a 500000 son: ",cant_300_y_500)

prom_300_500=promedios(suma3,cant_300_y_500)
print("\nEl sueldo promedio entres los sueldos mayores a $300000 y menores a 500000 es: $",prom_300_500)
print("\nLa capacidad de ahorro mensual de este grupo es: $",ahorro(prom_300_500))

#Intervalos sueldos mayores a 500000
print("\nLa cantidad de sueldos mayores a 500000 son: ",cant_mayor_500)   
prom_500=promedios(suma4, cant_mayor_500) 
print("\nEl sueldo promedio entre los sueldos mayores a $500000 es: $", prom_500)
print("\nLa capacidad de ahorro de este grupo es: $",ahorro(prom_500))

#Gráfico porcentajes según los rangos de sueldos
cantidad_sueldos_por_rango=[cant_menor_igual_150,cant_150_y_300,cant_300_y_500,cant_mayor_500]
nombres=["<=150000",">150000-<=300000",">300000-<=500000",">500000"]
plt.pie(cantidad_sueldos_por_rango, labels=nombres,autopct="%0.1f%% ")
plt.title("Porcentajes según los rangos de sueldos: \n Análisis con respecto a 273 salarios ")
plt.axis("equal")
plt.savefig("Porcentajes sueldos.png") 
plt.show()


#Gráfico Capacidad de Ahorro

capacidad_ahorro=[ahorro(prom_150_300),ahorro(prom_300_500),ahorro(prom_500)]
nombres=["150000-300000","300000-500000",">500000"]
fig, ax=plt.subplots()
#Etiqueta en eje Y
ax.set_ylabel("Ahorro Mensual")
#Etiqueta en eje X
ax.set_title("Rangos sueldos")
plt.bar(nombres, capacidad_ahorro)
plt.savefig("Capacidad ahorro.png")
plt.show()



dictSalarios={'sueldos':total_sueldos,
                 "sueldos_menores_150000":cant_menor_igual_150,
                 "sueldo_promedio_150000":promedios(suma1, cant_menor_igual_150),
                 "sueldos_150_300":cant_150_y_300,
                 "sueldos_promedio_150_300":prom_150_300,
                 "ahorros_150_300":ahorro(prom_150_300),
                 "sueldos_300_500":cant_300_y_500,
                 "sueldos_promedio_300_500":prom_300_500,
                 "ahorros_300_500":ahorro(prom_300_500),
                 "sueldos_500":cant_mayor_500,
                 "sueldos_promedio_500":prom_500,
                 "ahorros_500":ahorro(prom_500)
                 }


#print(dictSalarios) 

#Creación del archivo CSV con los datos del análisis de los sueldos 
with open('dictSalarios.csv','w')as f:
    writer=csv.writer(f)
    for k,v in dictSalarios.items():
        writer.writerow([k,v])


