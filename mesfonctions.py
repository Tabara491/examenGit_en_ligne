# <!-- premiere ligne -->

def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b if b != 0 else None

def carre(x):
    return x * x

# <!-- premiere ligne -->

def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b if b != 0 else None

def carre(x):
    return x * x

def cube(x):
    return x ** 3

def est_pair(n):
    return n % 2 == 0

def max_deux(a, b):
    return a if a > b else b

def min_deux(a, b):
    return a if a < b else b

def factorielle(n):
    if n == 0:
        return 1
    return n * factorielle(n - 1)