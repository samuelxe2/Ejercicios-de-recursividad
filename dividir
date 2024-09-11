print('Ingrese dos números enteros positivos y calcularé la división con decimales usando operaciones de desplazamiento de bits.')
a = int(input('Número a: '))
b = int(input('Número b: '))

cociente = 0
temp = 1
decimales = 0
precision = 5


if b == 0:
    print("División por cero no está definida.")
else:
   
    while b <= a:
        b <<= 1
        temp <<= 1

   
    while temp > 1:
        b >>= 1
        temp >>= 1
        if a >= b:
            a -= b
            cociente += temp


    for _ in range(precision):
        a *= 10
        decimal_digit = 0
        while a >= b:
            a -= b
            decimal_digit += 1
        decimales = decimales * 10 + decimal_digit

    print(f'El cociente de la división es {cociente}.{decimales}')