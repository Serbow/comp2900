def invertir_cadena(cadena):
    array_length = len(cadena)
    nueva_cadena = ''
    for i in range(array_length):        
        nueva_cadena += (cadena[array_length-1-i] )
    return nueva_cadena

mensaje = "Me duele la cabeza"
print(mensaje)
print(invertir_cadena(mensaje))