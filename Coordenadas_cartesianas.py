"""Ejercicio No.1: 
programa para ubicar la coordenadas en un plano"""

print("---------------")
print("-------------ubicar las coordenadas en un plano")
print("---------------")

#input 

X = int(input("ingrese  coordenadda en x:"))
y = int(input("ingrese coordenada en y:"))
O = int(input("numero"))
#proccesing 

if((X > 0) and (y > O)):
    print("Punto en el primer cuadrante");

    if((X > O)) and (y < 0):
        print("punto en el primer cuadrante");

    if((X < O)) and (y < 0):
        print("punto en el segundo cuadrante");
     
if((X < O)) and (y > 0):
        print("punto en el tercer cuadrante");

else:
    print("punto de origin");
