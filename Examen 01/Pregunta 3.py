var_1 = {"nombre": "Daniel", "apellido": "León", "edad": int(25), "dni": int(75111299)}
input("Cual es el valor de nombre: ")
input("Cual es el valor de apellido: ")
input("Cual es el valor de la edad: ")
input("Cual es el valor del dni: ")
var_1_values = list(var_1.values())
print("Los values del diccionario son: {}".format(var_1_values))
var_2 = var_1["edad"] + 10
print("Los values del diccionario con la edad más 10 es: {}".format(var_2))
var_1["profesion"] = "Ingeniero"
print("El diccionario con el nuevo key es: {}".format(var_1_values))
del var_1["dni"]
print("El diccionario con el el key de dni eliminado es: {}".format(var_1))