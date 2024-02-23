# lista de numero 
numero = [1, 2, 3, 4, 5]

# imprimir la lista original 
print("Lista original: ", numero)

# accer a elementos individuales por indice 
print("Primer elemento: ", numero[0])
print("Ultimo elemento: ", numero[-1])

# reemplazar un elemento de la lista
numero[2] = 10 
print("lista despues de reemplazar el tercer elemento", numero)

# agregar un elemento al fial de la lista 
numero.append(6)
print("lista despues de agregar un nuevo elemento",numero)

# eliminar un elemneto de la lista por valor 
numero.remove(4)
print("lista despes de eliminar e numero 4", numero)