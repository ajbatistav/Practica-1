#variables de entrada
monto = input ("Introduzca monto prestado: ")
monto = float(monto)
cuotas = input ("Introduzca cantidad de cuotas: ")
cuotas = int(cuotas)
interes= input ("Introduzca porcentaje de interes: ")
interes = float(interes) / 100
#calculo
ex_1 = (1 + interes) ** cuotas
ex_2 = ( interes * ex_1) / (ex_1 - 1)
resultado = monto * ex_2
print(resultado)