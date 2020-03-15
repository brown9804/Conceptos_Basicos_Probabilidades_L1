##Se muestran ejemplos de la definición clásica de la probabilidad de que 
##suceda un elemento cualquiera, uno en específico y un ejemplo de cartas.


###Forma de ejecutar
###python3 DefinicionClasicaProbabilidad.py

####Parte 1
#Se considera una muestra, el cual es un vector con n elementos
print("Se posee la siguiente muestra: 1,2,3,4,5,6   ")
espacio_muestras = [1,2,3,4,5,6]
#cuenta la cantidad de elementos que posee la muestra
n = len(espacio_muestras)
#saca la probabilidad es dividir 1/cantidad de elementos
probabilidad = 1.0/n
print("La proabilidad es de:   ", probabilidad)
#se busca por los numeros par en la muestra de arriba, lo que
#calcula es la razon entonces divide el numero entre dos y si da
#numero entero entonces es par 4/2 = 2 250 /2 =125
numeros_pares = [i for i in espacio_muestras if i % 2 is 0]
#cuenta la cantidad de numeros pares
h = len(numeros_pares)
#considera la probabilidad de numero pares, cantidad de numeros pares/numero total
probabilidadpares = float(h)/n
print("Probabilidad de que salga un número par:   ", probabilidadpares)
####Parte 2 ejemplo de naipe con 52 cartas probabilidad de sacar 6 con 4 palos 
# Crear espacio de muestras de palo, es decir un mazo de reinas,
#diamantes, etc en total son 4
palo = [i+1 for i in range(13)]
# Comprobar divisibilidad por 6
divisible_6 = [i for i in palo if i % 6 is 0]
print("Tomando en cuenta que hay cuatro palos, la frecuencia relativa de los números divisibles por 6 es:")
#Saca la probabilidad de que salga 6
probabilidad_6 = (4*float(len(divisible_6)))/(4*len(palo))
# Respuesta frecuencia relativa de los números divisibles por 6 es
print("{0:0.2f}".format(probabilidad_6))
