from datetime import datetime
class Persona:
    def __init__(self):
        self.nombre = " "
        self.edad = 0
        self.saldo = 0.0
        self.nacionalidad = "peruana"
    def solicitar_edad_nombre(self):
        while True:
            try:
                self.nombre = input("Ingrese su nombre: ")
                self.edad = int(input("Ingrese su edad: "))
                break
            except ValueError:
                print("Ingrese una edad válida")


    def cumpleaños(self):
        self.edad += 1
        print("{}".format(self.edad))


    def hora(self):
        return datetime.now().strftime("%d/%m/%Y""-""%H:%M")


persona = Persona()
# persona 1
print("Los datos de la persona 1 son los siguientes")
persona_1 = persona.solicitar_edad_nombre()

print("La edad actualizada de la persona es:")
persona_1 = persona.cumpleaños()

print("La hora en la que se registró la persona 1 es: {}".format(persona.hora()))
# persona 2
print(" ")
print("Los datos de la persona 2 son los siguientes")
persona_2 = persona.solicitar_edad_nombre()

print("La edad actualizada de la persona es:")
persona_2 = persona.cumpleaños()

print("La hora en la que se registró la persona 2 es: {}".format(persona.hora()))
