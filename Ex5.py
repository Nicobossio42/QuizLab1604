def frecuencia(numero, digito):
    cantidad = 0
    while numero != 0:
        ultimoDigito = numero % 10
        if ultimoDigito == digito:
            cantidad += 1
        numero = numero // 10
    return cantidad


numeroo = int(input("ingrese su número: "))
undigito = int(input("Ingrese su dígito: "))
print("Frecuencia del dígito en el número:", frecuencia(numeroo, undigito))