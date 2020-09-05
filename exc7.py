nota_1 = 90
nota_2 = 95
nota_3 = 77
nota_4 = 92
sumatoria = nota_1 + nota_2 + nota_3 + nota_4
promedio = sumatoria / 4
if promedio <= 60:
    print("Calificacion : F")
elif promedio <= 70:
    print("Calificacion : D")
elif promedio <= 80:
    print("Calificacion : C")
elif promedio <= 90:
    print("Calificacion : B")
else:
    print("Calificacion: A")