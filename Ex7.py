def sumaDigitos(numero):
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma = suma + digito
        numero = numero // 10
    return suma


cantidad = 0
mayor = -1
numero = int(input("Ingrese un numero positivo: "))
while numero >= 0:
    suma = sumaDigitos(numero)
    if suma > mayor:
        mayor = suma
        numeromayorsuma = numero
    if suma < 10:
        cantidad += 1
    numero = int(input("Ingrese un numero positivos: "))
print("la Sumatoria de dígitos de", numeromayorsuma, ":", mayor)
print("Cantidad con sumatoria menor a 10:", cantidad)