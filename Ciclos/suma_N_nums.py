#Alan Cordova
#calcula la suma de n numero ingresados 



c=0 #acumulador 
alan = int(input("Ingresa cuantos numeros quieres sumar: "))

for i in range(alan):#damos rango dependiendo de la variable
  x = int(input("mete un numero: "))
  c = c+x #suma del acumulador mas la cantidad de numero ingresados
print(f"la suma de todos los numeros es: {c}")
