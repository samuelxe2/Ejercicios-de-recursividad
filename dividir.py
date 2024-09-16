def dividir_con_enteros(a, b, temp):
    if b > a:
        return 0
    b <<= 1
    temp <<= 1
    cociente = dividir_con_enteros(a, b, temp)
    b >>= 1
    temp >>= 1
    if a >= b:
        a -= b
        cociente += temp
    return cociente

def dividir_con_decimales(a, b, precision):
    if precision == 0:
        return 0
    a *= 10
    decimal_digit = 0
    while a >= b:
        a -= b
        decimal_digit += 1
    return decimal_digit * 10**(precision - 1) + dividir_con_decimales(a, b, precision - 1)

def dividir(a, b, precision=5):
    if b == 0:
        return "División por cero no está definida."
    temp = 1
    cociente = dividir_con_enteros(a, b, temp)
    decimales = dividir_con_decimales(a, b, precision)
    return f'El cociente de la división es {cociente}.{decimales}'

# Solicitar entrada de usuario
a = int(input('Número a: '))
b = int(input('Número b: '))

# Imprimir el resultado
print(dividir(a, b))
