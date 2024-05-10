import random


def lista_aleatoria():
    lista = [random.randint(1, 100) for _ in range(10)]
    print("La lista de números aleatorios es la siguiente: {}".format(lista))
    return lista


def lista_aleatoria_no_repetidos(lista):
    lista_sin_numeros_repetidos = list(set(lista))
    print("La lista sin números repetidos es la siguiente: "
          "{}".format(lista_sin_numeros_repetidos))
    return lista_sin_numeros_repetidos


def lista_ordenada(lista_sin_numeros_repetidos):
    lista_mayor_a_menor = sorted(lista_sin_numeros_repetidos, reverse=True)
    lista_menor_a_mayor = sorted(lista_sin_numeros_repetidos)
    print("Mi lista ordenada de mayor a menor es la siguiente: "
          "{}".format(lista_mayor_a_menor))
    print("Mi lista ordenada de menor a mayor es la siguiente: "
          "{}".format(lista_menor_a_mayor))
    return lista_mayor_a_menor, lista_menor_a_mayor


def valor_par(lista_sin_numeros_repetidos):
    valores_par = [num for num in lista_sin_numeros_repetidos if num % 2 == 0]
    if valor_par:
        valor_max_par = max(valores_par)
        print("El valor par más alto es el siguiente: "
              "{}".format(valor_max_par))
        return valor_max_par
    else:
        print("No hay valores pares en la lista")
        return None


mi_lista_aleatoria = lista_aleatoria()
mi_lista_sin_repetidos = lista_aleatoria_no_repetidos(mi_lista_aleatoria)
mi_lista_mayor_a_menor = lista_ordenada(mi_lista_sin_repetidos)
mi_valor_par = valor_par(mi_lista_sin_repetidos)
