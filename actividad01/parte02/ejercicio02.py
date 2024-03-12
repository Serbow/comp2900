def mayor(lista):
    valor_mayor = lista[0]
    for n in lista:
        if (n > valor_mayor):
            valor_mayor = n
    return valor_mayor


lst = [15, 7, 18, 22, 4, 36, 5]
print(lst)
print(f'El valor mayor de la lista es: {mayor(lst)}')