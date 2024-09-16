'''
Elaborado por: 
Esteban Alejandro Villalba Delgadillo
20212020064
'''

def division(dividendo, divisor):
    if divisor == 0:
        raise ValueError("El divisor no puede ser 0")
    
    if dividendo < divisor:
        return 0
    
    return 1 + division(dividendo - divisor, divisor)

def solicitar_valores():
    return resultado(int(input("Ingrese el dividendo: ")), int(input("Ingrese el divisor: ")))

def resultado(dividendo: int, divisor: int):
    return dividendo, divisor, division(dividendo, divisor)

def imprimir_pantalla(valores):
    print(f"El resultado de la division de {valores[0]} entre {valores[1]} es: {valores[2]}")

imprimir_pantalla(solicitar_valores())