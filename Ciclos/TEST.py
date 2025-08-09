#Alan Adrian Cordova 250199
#Programa que compara 2 valores

#inicializar la variable para el numero mayor con un valor pequeño
mayor = float('-inf')
#contabiliza
cont = 0 
acumulador = 0 

#leer 5 numeros usando bucle "for"
for i in range(5):
    num = float(input(f"ingresa el numero {i + 1}:"))
    #comprar el numero actual con el mayor encontrado hasta ahora
   
   
    acumulador = acumulador + num #Suma todos los datos que ingrese el
    if num > mayor:
        mayor = num
        cont = cont+1

#imprimir
print(f"el numero mayor es: {mayor}")
print(f"el numero de veces que cambio el numero mayor: {cont}")
print(f"la suma de los numeros ingresados es: {acumulador}")