def multiplicar_recursivo(a, b):
    if b == 0:
        return 0
    return a + multiplicar_recursivo(a, b - 1)
try:
    a = int(input("Ingrese el primer número (a): "))
    b = int(input("Ingrese el segundo número (b): "))
    
    # Verificar si b es negativo para ajustar el signo
    if b < 0:
        resultado = -multiplicar_recursivo(a, -b)
    else:
        resultado = multiplicar_recursivo(a, b)
    
    print(f"El resultado de {a} x {b} es: {resultado}")
except ValueError:
    print("Por favor, ingrese números enteros válidos.")
