"""EJERCICIO 4: Prprograma que calcule el índice de masa corporal de una persona
(IMC = peso[kg] / altura2 [m]) e indique el estado en el que se encuentra esa
persona en función del valor del IMC:"""

print("----------")
print("-------INDICE DE MASA CORPORAL------")
print("-----------")

#Input 
peso=int(input("ingresa tu peso: "))
alt=float(input("ingrese su altura: "))

#Proccesing
imc=peso/(alt**2)
if imc<=16:
    print("teneis un criterio de visita el hospital")
else:
    if imc<=17:
        print("Usted tiene infrapeso")
    else:
        if imc<=18:
           print("Usted tiene un pseo bajo ")
        else:
            if imc<=25:
                print("Usted tiene un peso normal. estais saludable de peso")
            else:
                if imc<=30:
                   print("Usted tiene sobre peso (obesidad de grado 1 )")
                else:
                  if imc<=35:
                     print("Usted tiene sobre peso (obesidad grado II )")
                  else:
                    if imc<=40:
                     print("Usted tiene sobre peso (obesidad grado III)")
                    else:
                        if imc<=40:
                         print("Usted tiene sobre peso (obesidad grado IV)")
                      
                   

                   


                   
