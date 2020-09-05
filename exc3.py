numero = input("Introduzca un numero: ")
res = int(numero) % 2
if res == 0:
    print(numero + " es par")
else:
    print(numero + " es impar")