def Average(lst): 
    return sum(lst) / len(lst) 
 
def promedio(lista_numeros):
    suma = 0  
    array_length = 0  
    for valor in lista_numeros:
        suma = suma + valor #   suma += valor
        array_length = array_length + 1       #   ctr++
    return (suma / array_length)

lst = [15, 9, 55, 41, 35, 20, 62, 49]

print(lst)
print(f'El valor promedio de la lista es {promedio(lst)}')