lista = []
lista.append(1)
lista.append(5)
lista.append(3)
lista.append(7)
lista.append(9)
lista.append(15)
lista.append(12)
lista.append(25)
lista.append(367)
lista.append(47)
print("La lista con datos aleatorios es: {}".format(lista))
print(len(lista))

for valores in lista:
valores_al_cubo = valores ** 3
lista_cubos.append(valores_al_cubo)
print("Los valores de la lista al cubo son: {}".format(lista_cubos))