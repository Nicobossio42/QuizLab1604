def EsPrimo(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

def aplicando():
    num = int(input('Escriba su número: '))
    resultado = EsPrimo(num)

    if resultado is True:
        print('el numero es primo')
    else:
        print('El numero no es primo')

if __name__ == '__main__':
    aplicando()