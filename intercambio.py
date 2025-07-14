#Alan Adrian Cordova Vazquez 250199
#Programa que intercambia valores  

#variables
a = float(input("Ingresa el primer numero: "))
b = float(input("Ingresa el segundo dato: "))

b = a*b

a = b//a #division entera, solo se queda el cociente sin decimales 
b = b//a
print(f"ahora a es {a} y b es {b}")