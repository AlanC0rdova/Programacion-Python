#Alan Cordova
#calcula la suma de 4 numero ingresados 



c=0 #acumulador 
for i in range(4):#damos rango de 4 
  x = int(input("mete un numero: "))
  c = c+x #suma del acumulador mas la cantidad de numero ingresados
print(f"la suma de todos los numeros es: {c}")

