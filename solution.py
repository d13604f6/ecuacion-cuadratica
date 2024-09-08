import math

def solution(a, b, c):
    """
    Calcula las soluciones de una ecuación cuadrática ax^2 + bx + c = 0.

    Parámetros:
    a (float): Coeficiente de x^2
    b (float): Coeficiente de x
    c (float): Término constante

    Retorna:
    tuple: Tupla con las soluciones de la ecuación cuadrática.
           Si no hay soluciones reales, devuelve una tupla vacía.
    """
    discriminante = b**2 - 4*a*c

    if discriminante < 0:
        # No hay soluciones reales
        return ()
    elif discriminante == 0:
        # Una solución real
        solucion = -b / (2*a)
        return (solucion,)
    else:
        # Dos soluciones reales
        solucion1 = (-b + math.sqrt(discriminante)) / (2*a)
        solucion2 = (-b - math.sqrt(discriminante)) / (2*a)
        return (solucion1, solucion2)

# Ejemplos de uso
print(solution(a=1, b=6, c=5))   # Debería imprimir (-5, -1)
print(solution(a=1, b=4, c=4))   # Debería imprimir (-2,)
print(solution(a=1, b=6, c=45)) # Debería imprimir ()
