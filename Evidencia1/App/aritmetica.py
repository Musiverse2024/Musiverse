# Funciones aritmeticas del programa ultima version
def sumar(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Ambos argumentos deben ser números.")
    return round(a + b, 2)

def restar(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Ambos argumentos deben ser números.")
    return round(a - b, 2)

def dividir(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Ambos argumentos deben ser números.")
    try:
        return round(a / b, 2)
    except ZeroDivisionError:
        return "Error: División por cero."

def multiplicar(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Ambos argumentos deben ser números.")
    return round(a * b, 2)

def sumar_n(*args):
    if not all(isinstance(x, (int, float)) for x in args):
        raise TypeError("Todos los argumentos deben ser números.")
    return round(sum(args), 2)

def promedio_n(*args):
    if not all(isinstance(x, (int, float)) for x in args):
        raise TypeError("Todos los argumentos deben ser números.")
    if len(args) == 0:
        return 0
    return round(sum(args) / len(args), 2)
