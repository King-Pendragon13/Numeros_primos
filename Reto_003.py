""" * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100."""

# Función para verificar si un número es primo
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):  # optimización hasta raíz cuadrada
        if n % i == 0:
            return False
    return True

# Comprobar un número específico (ejemplo)
numero = int(input("Ingresa un número: "))
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")

# Imprimir los números primos del 1 al 100
print("\nNúmeros primos del 1 al 100:")
for i in range(1, 101):
    if es_primo(i):
        print(i, end=" ")