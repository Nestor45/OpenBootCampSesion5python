from cmath import exp, pi
import math

def calcular_area_triangulo(altura, base):
    area = (base * altura)/2
    print("El area del triangulo es:",area)

calcular_area_triangulo(5,10)

def calcular_area_circulo(radio):
    area = pi*pow(radio,2)
    print("el area del circulo es: ",area)

calcular_area_circulo(5)

def es_primo(numero):
    contador=2
    primo=True
    if type(numero) == int:
        if (numero > 1):
            while (contador!=numero):
                if (numero % contador == 0):
                    primo=False
                contador += 1
            if primo:
                print("Es primo")
            else:
                print("No es primo")
        else:
            print("El numero es menor que 1")
    else:
        print("El valor que se introdujo no es un numero")
es_primo(5)


def es_bisiesto(anio):
    # podemos saber si un año es bisiesto si este es múltiplo de 4. Si además es múltiplo de 100 no será bisiesto a no ser que sea múltiplo de 400, que sí será bisiesto.
    if anio%4==0 and (anio%100!=0 or anio%400==0):
        print("Es año bisiesto")
    else:
        print("No es año bisiesto")
es_bisiesto(2000)

