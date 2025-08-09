#Alan Cordova
#calcula la suma de n numero ingresados 

#asfsdadgansj ha

c=0 #acumulador para suma
print(" UPBC ")

for i in range(2):#damos rango dependiendo de la variable
  nombre = (input(f"{i+1}.- Ingrese nombre del alumno : "))
  c1 = float(input("Ingrese la calificacion de la U1: "))
  c2 = float(input("Ingrese la calificacion de la U2: "))
  c3 = float(input("Ingrese la calificacion de la U3: "))
  c = c+c1+c2+c3 #suma del acumulador mas la cantidad de numero ingresados
  


print(f"alumno: {nombre}")
print(f"promedio es: {c/3}")


