#esta es la serie de fibonacci
print("Esta es la serie de fibonacci\n")
#Fn = Fn-1 + Fn-2 
def fibonacci (n):
    if n <= 1: 
        return n 
    else: 
        return fibonacci(n-1) + fibonacci(n-2)
    
#ejemplo de uso 
numero_terminos = 20 
print("serie de fibonacci: \n")
for i in range(numero_terminos):
    print(fibonacci(i))
    