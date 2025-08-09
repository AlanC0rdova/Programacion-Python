#Alan Adrian Cordova 250199
#Programa que muestra el factorial de unn numero

acumulador = 1

num = int(input("de que numero quieres saber factorail:"))
for i in range(num):
    
    acumulador = acumulador * (i+1)
    
print(f"el factorial de {num} es {acumulador}")