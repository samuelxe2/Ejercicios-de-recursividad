def division(dividendo, divisor):
    if divisor == 0:
        raise ValueError("El divisor no puede ser 0")
    
    if dividendo < divisor:
        return 0
    
    return 1 + division(dividendo - divisor, divisor)

dividendo = int(input("Ingrese el dividendo: "))
divisor = int(input("Ingrese el divisor: "))

try:
    result = division(dividendo, divisor)
    print(f"El resultado de la division de {dividendo} entre {divisor} es: {result}")
except ValueError as e:
    print(e)
