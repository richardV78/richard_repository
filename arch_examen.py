##este ejemplo es para hacer el examen 
def factorial (n):
    if n == 0:
        return 1 
    else:
        return n * factorial(n - 1)
    
# ejemplo de uso
# vamos a intentar pedir un numero al usuario para que le calcule el factiral 
    
num = int(input("ingresa un numero para calcularte el factorial \n"))
numero = num
resultado = factorial(numero)
print(f"el factorial de {numero} es: {resultado}")