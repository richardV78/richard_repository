##este ejemplo es para hacer el examen 
def factorial (n):
    if n == 0:
        return 1 
    else:
        return n * factorial(n - 1)
    
# ejemplo de uso
numero = 5
resultado = factorial(numero)
print(f"el factorial de {numero} es: {resultado}")