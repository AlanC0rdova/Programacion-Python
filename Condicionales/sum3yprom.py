
#usa compuerta and e if anidados 

n1 = float(input("Ingresa un valor: "))
n2 = float(input("Ingresa un segundo valor: "))
n3 = float(input("Ingresa un tercer valor: "))

if n1 >= n2 and n1 >= n3:
    mayor = n1
elif n2 >= n1 and n2 >= n3:
    mayor = n2
else:
    mayor = n3


#imprimir el numero mayor
print(f"El numero mayor es: {mayor}")


   
