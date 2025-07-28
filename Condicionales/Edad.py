#Alan Adrian Cordova 
#Programa que calcula la edad por la fecha de nacimiento

# Fecha de nacimiento
dn = float(input("Ingresa tu dia de nacimiento: "))
mn = float(input("Ingresa tu dia de mes: "))
an = float(input("Ingresa tu dia de año: "))



# Fecha actual
dia_hoy = 27
mes_hoy = 7
ano_hoy = 2025

# Calcular años
anos = ano_hoy - an

# Ajustar si aún no ha cumplido años este año
if mes_hoy < mn:
    anos = anos - 1
else:
    if mes_hoy == mn and dia_hoy < dn:
        anos = anos - 1

# Si la edad es negativa, poner 0
if anos < 0:
    anos = 0

# Mostrar resultado
print("Tienes", anos, "años")