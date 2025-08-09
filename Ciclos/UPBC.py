#Alan Cordova
#Programa que regristra 3 alumnos

c = 0 #acumulador para suma
a = 0
r = 0 

print(" UPBC ")

for i in range(10):#damos rango dependiendo de la variable
  
  nombre = (input(f"{i+1}.- Ingrese nombre del alumno : "))
  c1 = float(input("Ingrese la calificacion de la U1: "))
  c2 = float(input("Ingrese la calificacion de la U2: "))
  c3 = float(input("Ingrese la calificacion de la U3: "))
  c = c+c1+c2+c3  #suma del acumulador mas la cantidad de numero ingresados
  c = c/3
  
  print(" ")
  print(f"{nombre}")
  print(f"Su calificacion de la U1 es: {c1}")
  print(f"Su calificacion de la U2 es: {c2}")
  print(f"Su calificacion de la U3 es: {c3}")
  print(f"Su promedio es: {c}")
  print(" ")

  if c >= 60:
    a = a + 1
    print("Aprobado")
    print(" ")
    
  else:
    r = r + 1
    print("Reprobado")
    print(" ")  
   


print(f"Total de aprobados: {a}")
print(f"Total de reprobados: {r}")

  

  





