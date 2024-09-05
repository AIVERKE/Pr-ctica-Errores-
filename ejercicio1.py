import math

# Definimos la función original f(x)
def f(x):
    return 25*x**3 - 6*x**2 + 7*x - 88

# Definimos las derivadas de la función f(x)
def f_prime(x):
    return 75*x**2 - 12*x + 7

def f_double_prime(x):
    return 150*x - 12

def f_triple_prime(x):
    return 150

# Expansión de Taylor hasta tercer orden alrededor de x = 1
def taylor_series_approx(x_base, x_value, order):
    approximation = f(x_base)
    if order >= 1:
        approximation += f_prime(x_base) * (x_value - x_base)
    if order >= 2:
        approximation += (f_double_prime(x_base) * (x_value - x_base)**2) / math.factorial(2)
    if order >= 3:
        approximation += (f_triple_prime(x_base) * (x_value - x_base)**3) / math.factorial(3)
    return approximation

# Cálculo del error relativo porcentual verdadero
def true_relative_error(true_value, approx_value):
    return abs((true_value - approx_value) / true_value) * 100

# Parámetros
x_base = 1   # Punto base
x_value = 3  # Valor donde queremos aproximar
true_value = f(x_value)  # Valor verdadero de la función en x = 3

# Calcular aproximaciones y errores
for order in range(4):
    approx_value = taylor_series_approx(x_base, x_value, order)
    error = true_relative_error(true_value, approx_value)
    print(f"Aproximación de orden {order}: {approx_value}")
    print(f"Error relativo porcentual: {error:.5f}%\n")
