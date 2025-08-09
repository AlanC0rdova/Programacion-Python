#Alan Adrian Cordova 250199
#Programa que compara 2 valores

#inicializar la variable para el numero mayor con un valor pequeño
mayor = float('-inf')

#leer 5 numeros usando bucle "for"
for i in range(5):
    num = float(input(f"ingresa el numero {i + 1}:"))
    #comprar el numero actual con el mayor encontrado hasta ahora
    if num > mayor:
        mayor = num

#imprimir
print(f"el numero mayor es: {mayor}")