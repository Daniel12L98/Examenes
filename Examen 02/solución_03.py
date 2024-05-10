def ingresar_datos():
    while True:
        try:
            val_1 = float(input("Ingrese el primer número: "))
            val_2 = float(input("Ingrese el segundo número: "))
            return val_1, val_2
        except ValueError:
            print("Error: Por favor ingrese números válidos.")


def division_valor():
    while True:
        try:
            val_1, val_2 = ingresar_datos()
            division = val_1 / val_2
            print("El resultado de la división es: {}".format(division))
            break
        except ZeroDivisionError:
            print("No se puede dividir entre cero, ingrese números válidos")


def suma_valor():
    while True:
        try:
            val_1, val_2 = ingresar_datos()
            suma = val_1 + val_2
            if suma < 0:
                raise ValueError
            print("La suma es: {}".format(suma))
            break
        except ValueError:
            print("La suma no es válida")
division_valor()
suma_valor()