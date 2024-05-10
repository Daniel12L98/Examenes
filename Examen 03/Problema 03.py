import time


def medir_tiempo(funcionB):
    def funcionC(*args, **kwargs):
        inicio = time.time()
        resultado = funcionB(*args, **kwargs)
        fin = time.time()
        tiempo_medido_de_ejecucion = fin - inicio
        print("El tiempo de ejecución es el siguiente: "
              "{}".format(tiempo_medido_de_ejecucion))
        return resultado
    return funcionC


@medir_tiempo
def multiplicar(*numeros):
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado


valor_1 = multiplicar(2, 3, 2)
print("El valor de la multiplicación es el siguiente: {}".format(valor_1))
valor_2 = multiplicar(2, 2, 2)
print("El valor de la multiplicación es el siguiente: {}".format(valor_2))
valor_3 = multiplicar(2, 4, 2)
print("El valor de la multiplicación es el siguiente: {}".format(valor_3))
