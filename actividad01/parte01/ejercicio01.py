def maximo (a, b):
    if a > b:
        return a
    else:
        return b
    
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
resultado = maximo(num1, num2)

print("El máximo entre", num1, "y", num2, "es:", resultado)