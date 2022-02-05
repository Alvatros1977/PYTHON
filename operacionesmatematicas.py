# Ejemplo de opraciones matematicas.

#Importando la libreria de funciones matematicas
import math

#entradas(entrada de datos)

#variables
#sintaxis para declarar (crear) una variable



numero1=10
numero2=2

numero_1=float (input("introdusca el numero:")) #convierte un string a un int
numero_2=float (input("Introdusca el segundo numero")) # convierte un string a un int


#procesos.(Calculos u Operaciones matematicas y/o logicas)

suma= numero1+numero2
resta=numero1-numero2
div =numero1/numero2
multiplicacion=numero1*numero2

potencia1=numero1**numero2
potencia2=pow(numero1,numero2)
cuadrado=pow(numero1,2)
cubo=pow(numero1,3)

raiz_cuadrada= math.sqrt(numero1)
raiz_cuadrada2=pow(numero1,1/2)
raiz_cubica=pow(numero1,1/3)


#input
suma= numero_1+numero_2
resta=numero_1-numero_2
div =numero1/numero2
multiplicacion=numero_1*numero_2

potencia1=numero_1**numero_2
potencia2=pow(numero_1,numero_2)
cuadrado=pow(numero_1,2)
cubo=pow(numero_1,3)

raiz_cuadrada= math.sqrt(numero_1)
raiz_cuadrada2=pow(numero_1,1/2)
raiz_cubica=pow(numero_1,1/3)


#Salidas  (mostrar los resultador.)

print("estos son los resultados de los numeros ya fijos")
print("la suma es igual a " + str(suma)) #concatenacion o union
print ("este es el resultado de la resta", str(resta))
print(f"el resultado de la division es:{div}")
print (f"el resultado de esta multiplicacion es {multiplicacion}") #interpolacion
print (f"el resultado de potencia1 es {potencia1}")
print (f"el resulatado de la potencia2 es {potencia2}")
print (f"el resultado del cuadrado es {cuadrado}")
print (f"el resulatdo del cubo es {cuadrado}")

print (f"el resultado de la raiz cuadrada de 1 es igual a {raiz_cuadrada}")
print (f"el resultado de la raiz cuadrada2 de 1 es igual a {raiz_cuadrada2}")
print (f"el resultado de la raiz cubica de 1 es igual a {raiz_cubica}")


#input

print("estos son los resultados de los numeros con Input")

print("la suma es igual a " + str(suma)) #concatenacion o union
print ("este es el resultado de la resta", str(resta))
print(f"el resultado de la division es:{div}")
print (f"el resultado de esta multiplicacion es {multiplicacion}") #interpolacion
print (f"el resultado de potencia1 es {potencia1}")
print (f"el resulatado de la potencia2 es {potencia2}")
print (f"el resultado del cuadrado es {cuadrado}")
print (f"el resulatdo del cubo es {cuadrado}")

print (f"el resultado de la raiz cuadrada de 1 es igual a {raiz_cuadrada}")
print (f"el resultado de la raiz cuadrada2 de 1 es igual a {raiz_cuadrada2}")
print (f"el resultado de la raiz cubica de 1 es igual a {raiz_cubica}")


