"""Ejercicio No. 2
Programa que permita realizar un préstamo bancario, teniendo en cuenta que el
préstamo será otorgado solamente a personas con ingresos superiores a $945200
y que no posea ninguna otra deuda."""

print("------------------------")
print("--------realizar un prestamo banacario--------")
print("--------------------")

INGRESOS =int(input("INGRESE el valor de suss ingresos "))

#processing 
if INGRESOS > 945200:
    deudas=int(input("ponga 0 si no tiene deudas o ponga 1 si tiene deudas "))
    if deudas==0:
        print("aprobado el prestamo ")
else:
    print(" no puede ser aprobado ")

    #output


deudas= int(input)
print("si es <  de 245200 prestamo DENEGADO")
print("si es > de 245200 prestamo   APROBADO ")

if((INGRESOS > 242500)):
  print("prestamo el aprobado:")