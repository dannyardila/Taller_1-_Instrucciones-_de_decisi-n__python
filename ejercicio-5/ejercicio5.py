"""Ejercicio 5:
Programa para calcular el gasto de agua de una vivienda dado el número de m2 de agua
gastados,"""

print("-----------------------------------------------")
print("----------Gasto del Agua-----------")
print("-----------------------------------------------")

# input
M= input("Digite la cantidad en metros cuadrados que ha gastado:")
M= int(M)

C=10000

# processing

if M<=50:
    input("Su cuota de agua es: "+ str(C))

else:
    if M==50 or M<=200:
        Cf=((M-50)*2000)+C
        print("Su cuota final es: " + str(Cf))
  #ouput  
    else:
        Cf=((M-50)*3000)+C
        print("Su cuota final es: " + str(Cf))
    
      