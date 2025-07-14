#Alan Cordova 250199
#Invierte un numero de 2 digitos 

num1 = float(input("Ingresa un numero de 2 digitos: "))

u = (num1//10)
d = (num1%10)
inv = ((d*10)+u)

print(f"el numero era {num1} invertido es {inv}")