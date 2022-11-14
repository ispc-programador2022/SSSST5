

import matplotlib.pyplot as plt


print("\nConclusiones de nuestro análisis:")
print("\n Capacidad de ahorro de $85717, sueldos entre 150000y 300000")
tiempo_primer_intervalo1 = round(1113762/85171)
print("Para adquirir un auto de valor menor a 1.5M se demorará:  ", tiempo_primer_intervalo1, " meses")
tiempo_primer_intervalo2= round(1998217/85171)
print("Para adquirir un auto de valor comprendido entre 1.5M y 2.5M se demorará:  ", tiempo_primer_intervalo2, " meses")
tiempo_primer_intervalo3= round(3008308/85171)
print("Para adquirir un auto de valor comprendido entre 2.5M y 3.5M se demorará:  ", tiempo_primer_intervalo3, " meses")
tiempo_primer_intervalo4= round(4228707/85171)
print("Para adquirir un auto de valor comprendido entre 3.5M y 5M se demorará:  ", tiempo_primer_intervalo4, " meses")
tiempo_primer_intervalo5= round(5809771/85171)
print("Para adquirir un auto de valor comprendido entre 5My 6.5M se demorará:  ", tiempo_primer_intervalo5, " meses")
tiempo_primer_intervalo6= round(7232857/85171)
print("Para adquirir un auto de valor mayor 6.5M se demorará:  ", tiempo_primer_intervalo6, " meses")

print("\n Capacidad de ahorro de $253467, sueldos entre 300000 y 500000 ")
tiempo_segundo_intervalo1 = round(1113762/253467)
print("Para adquirir un auto de valor menor a 1.5M se demorará:  ", tiempo_segundo_intervalo1, " meses")
tiempo_segundo_intervalo2= round(1998217/253467)
print("Para adquirir un auto de valor comprendido entre 1.5M y 2.5M se demorará:  ", tiempo_segundo_intervalo2, " meses")
tiempo_segundo_intervalo3= round(3008308/253467)
print("Para adquirir un auto de valor comprendido entre 2.5M y 3.5M se demorará:  ", tiempo_segundo_intervalo3, " meses")
tiempo_segundo_intervalo4= round(4228707/253467)
print("Para adquirir un auto de valor comprendido entre 3.5M y 5M se demorará:  ", tiempo_segundo_intervalo4, " meses")
tiempo_segundo_intervalo5= round(5809771/253467)
print("Para adquirir un auto de valor comprendido entre 5My 6.5M se demorará:  ", tiempo_segundo_intervalo5, " meses")
tiempo_segundo_intervalo6= round(7232857/253467)
print("Para adquirir un auto de valor mayor 6.5M se demorará:  ", tiempo_segundo_intervalo6, " meses")


print("\n Capacidad de ahorro de $718947 , sueldos mayores a 500000")
tiempo_tercer_intervalo1 = round(1113762/718947)
print("Para adquirir un auto de valor menor a 1.5M se demorará:  ", tiempo_tercer_intervalo1, " meses")
tiempo_tercer_intervalo2= round(1998217/718947)
print("Para adquirir un auto de valor comprendido entre 1.5M y 2.5M se demorará:  ", tiempo_tercer_intervalo2, " meses")
tiempo_tercer_intervalo3= round(3008308/718947)
print("Para adquirir un auto de valor comprendido entre 2.5M y 3.5M se demorará:  ", tiempo_tercer_intervalo3, " meses")
tiempo_tercer_intervalo4= round(4228707/718947)
print("Para adquirir un auto de valor comprendido entre 3.5M y 5M se demorará:  ", tiempo_tercer_intervalo4, " meses")
tiempo_tercer_intervalo5= round(5809771/718947)
print("Para adquirir un auto de valor comprendido entre 5My 6.5M se demorará:  ", tiempo_tercer_intervalo5, " meses")
tiempo_tercer_intervalo6= round(7232857/718947)
print("Para adquirir un auto de valor mayor 6.5M se demorará:  ", tiempo_tercer_intervalo6, " meses")



#Gráficos:

intervalo1=[tiempo_primer_intervalo1,tiempo_primer_intervalo2,tiempo_primer_intervalo3,tiempo_primer_intervalo4,tiempo_primer_intervalo5,tiempo_primer_intervalo6]
nombres=[">1.5M","1.5M-2.5M","2.5M-3.5M","3.5M-5M","5M-6.5M",">6.5M"]
fig, ax=plt.subplots()
#Etiqueta en eje Y
ax.set_ylabel("meses")
#Etiqueta en eje X
ax.set_title("Cantidad de meses según precio auto \n Capacidad de ahorro de $85717\n en base al sueldo promedio (150000 y 300000) ")
plt.bar(nombres, intervalo1, color='magenta')
plt.savefig("Meses_capacid1.png")
plt.show()


intervalo2=[tiempo_segundo_intervalo1,tiempo_segundo_intervalo2,tiempo_segundo_intervalo3,tiempo_segundo_intervalo4,tiempo_segundo_intervalo5,tiempo_segundo_intervalo6]
nombres=[">1.5M","1.5M-2.5M","2.5M-3.5M","3.5M-5M","5M-6.5M",">6.5M"]
fig, ax=plt.subplots()
#Etiqueta en eje Y
ax.set_ylabel("meses")
#Etiqueta en eje X
ax.set_title("Cantidad de meses según precio auto \n Capacidad de ahorro de $253467 \n en base al sueldo promedio (300000 y 500000) ")
plt.bar(nombres, intervalo2, color='cyan')
plt.savefig("Meses_capacid2.png")
plt.show()

intervalo3=[tiempo_tercer_intervalo1,tiempo_tercer_intervalo2,tiempo_tercer_intervalo3,tiempo_tercer_intervalo4,tiempo_tercer_intervalo5,tiempo_tercer_intervalo6]
nombres=[">1.5M","1.5M-2.5M","2.5M-3.5M","3.5M-5M","5M-6.5M",">6.5M"]
fig, ax=plt.subplots()
#Etiqueta en eje Y
ax.set_ylabel("meses")
#Etiqueta en eje X
ax.set_title("Cantidad de meses según precio auto \n Capacidad de ahorro de $ 718947\n en base al sueldo promedio (>500000) ")
plt.bar(nombres, intervalo2, color='salmon')
plt.savefig("Meses_capacid3.png")
plt.show()



  
   