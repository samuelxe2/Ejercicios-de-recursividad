'''
Elaborado por: 
Samuel Antonio Sanchez Peña
20212020151
'''

def multiplicar_recursivo(a, b):
    if b == 0:
        return 0
    return a + multiplicar_recursivo(a, b - 1)

def solicitar_valores():
    return resultado(int(input("Ingrese el primer número: ")), int(input("Ingrese el segundo número: ")))

def resultado(a, b):
    if b < 0:
        return a, b, multiplicar_recursivo(a, -b)
    else:
        return a, b, multiplicar_recursivo(a, b)

def imprimir_pantalla(valores):
    print(f"El resultado de {valores[0]} x {valores[1]} es: {valores[2]}")

imprimir_pantalla(solicitar_valores())
    
    


