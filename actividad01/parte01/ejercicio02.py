def area_triangulo (base, altura):
    return (base * altura) / 2
    
base = int(input("Ingrese la base del triángulo: "))
altura = int(input("Ingrese la altura del triángulo: "))
area = area_triangulo(base, altura)

print(f"El área del triángulo es: {area}")