def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * (5/9)
    
fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
celsius = fahrenheit_a_celsius(fahrenheit)

print(f"La temperatura en grados Celsius es: {celsius}°")