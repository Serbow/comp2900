def clasificar_numero(num):
    if num > 0:
        return "Positivo"
    elif num < 0:
        return "Negativo"
    else:
        return "Cero"

# Prueba
assert clasificar_numero(9) == "Positivo", "El valor NO es positivo."
assert clasificar_numero(-8) == "Negativo", "El valor NO es negativo."
assert clasificar_numero(0) == "Cero", "El valor NO es cero."