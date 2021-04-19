def sumar(Numero, sum):
    sum += Numero
    return sum


sum = 0
while True:
    try:
        num = int(input("Ingrese su numero: "))
    except ValueError:
        print("Solo ingrese numeros, por favor.")
        continue
    if num == 0:
        break
    else:
        sum = sumar(num, sum)
        print("La suma es: ", sum)
