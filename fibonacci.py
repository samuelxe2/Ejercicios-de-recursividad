'''
Elaborado por: 
Amir Zoleyt Vanegas Cárdenas
20211020015

NOTA:
Se utiliza lru_cache para optimizar las funciones 
recursivas y hacer más rápido los cálculos.
'''
from functools import lru_cache
import cmath


'''
Esta función recursiva de fibonacci es generalizada
a todos los enteros (Negativos y positivos)
'''
@lru_cache(maxsize=None)
def fibonacci_sequence(n: int):
    if n < 0:
        return int(fibonacci_sequence(-n) * (-1)**(n + 1))
    elif n < 2:
        return n
    else:
        return fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2)

'''
Esta función recursiva de fibonacci es generalizada 
a los números complejos. fib(z) retorna el valor
de la fórmula de binet, para calcular el fn. 
Phi es el número aúreo.
'''
@lru_cache(maxsize=None)
def complex_fibonacci(z: complex):
    def phi():
        return (1 + cmath.sqrt(5)) / 2 

    def fib(z: complex):
        return (
            cmath.exp(z * cmath.log(phi())) - cmath.cos(z * cmath.pi) * cmath.exp(-z * cmath.log(phi()))
        ) / cmath.sqrt(5) 

    if z.real < 2:
        return fib(z)
    else:
        return complex_fibonacci(z - 1) + complex_fibonacci(z - 2)


def print_list_fibonacci(first: int, last: int):
    print(f"f{first}: ", fibonacci_sequence(first))

    if first == last: return None
    print_list_fibonacci(first + 1, last)

#Cómputo de los valores de las sucesiones de fibonacci
print_list_fibonacci(-10, 10)
print("Complex value of fn: ", complex_fibonacci(3+4j))
