import requests as rq

res = rq.get("https://jsonplaceholder.typicode.com/users")
json = res.json()

usuario_id_6 = None
usuario_id_8 = None

for usuario in json:
    if usuario["id"] == 6:
        usuario_id_6 = usuario
    if usuario["id"] == 8:
        usuario_id_8 = usuario

if usuario_id_6 is not None and usuario_id_8 is not None:
    nombre_usuario_6 = usuario_id_6["name"]
    edad_6 = usuario_id_6["id"] * 2
    nombre_usuario_8 = usuario_id_8["name"]
    edad_8 = usuario_id_8["id"] * 2
    print("El nombre del usuario con id 6 es {}, y su edad es "
          "{}".format(nombre_usuario_6, edad_6))
    print("El nombre del usuario con id 8 es {} y su edad es "
          "{}".format(nombre_usuario_8, edad_8))

    if edad_6 is not None and edad_8 is not None:
        if edad_6 > edad_8:
            print("El usuario {} es mayor que el "
                  "{}".format(nombre_usuario_6, nombre_usuario_8))
        elif edad_6 == edad_8:
            print("Ambos usuarios tienen la misma edad.")
        else:
            print("El usuario {} es mayor que "
                  "{}".format(nombre_usuario_8, nombre_usuario_6))
    else:
        print("Las edades no están disponibles para esos id.")
else:
    print("Los usuarios no están disponibles para esos id.")
