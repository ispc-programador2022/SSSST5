

separador=","
with open('escala_salarial.csv', encoding="utf-8") as archivo:
    next(archivo) #Omito el encabezado del archivo
    Salarios=[]
    for linea in archivo:
        linea=linea.rstrip("\n")  #quito el salto de línea
        columnas=linea.split(separador)
        cargo=columnas[0]
        liquidacion=float(columnas[1])
        
        
        Salarios.append({
            "cargo":cargo,
            "liquidacion":liquidacion,  
            
        })
   # print("\n\nArchivo CSV convertido a Diccionario:\n\n")
#print(Salarios) 
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
    if val_salario <= 150.000:
        suma1+=val_salario
        cant_menor_igual_150+=1
        
        
    elif val_salario > 150.000 and val_salario <= 300.000:
        cant_150_y_300+=1
        suma2+=val_salario
        

    elif val_salario > 300.000 and val_salario <= 500.000:
        cant_300_y_500+=1
        suma3+=val_salario
        
    else:
        cant_mayor_500+=1
        suma4+=val_salario
        



print ("\nLa cantidad de sueldos menores a 150000 son: ",cant_menor_igual_150)
print("\nEl sueldo promedio entres los sueldos menores o iguales a $150000 es: $",round(suma1/cant_menor_igual_150,3))
print("\nLa cantidad de sueldos mayores a 150000 y menores o iguales a 300000 son: ",cant_150_y_300)
print("\nEl sueldo promedio entres los sueldos entres $150000 y $300000 es: $",round(suma2/cant_150_y_300,3))
print("\nLa cantidad de sueldos mayores a 300000 y menores o iguales a 500000 son: ",cant_300_y_500)
print("\nEl sueldo promedio entres los sueldos mayores a $300000 y menores a 500000 es: $",round(suma3/cant_300_y_500,3))
print("\nLa cantidad de sueldos mayores a 500000 son: ",cant_mayor_500)   
print("\nEl sueldo promedio entre los sueldos mayores a $500000 es: $", suma4/cant_mayor_500)
print("\n La cantidad total salarios analizados es: ", cant_menor_igual_150+cant_150_y_300+cant_300_y_500+cant_mayor_500,"\n")


