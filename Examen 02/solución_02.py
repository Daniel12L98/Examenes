from solución_01 import Persona
class Empleado(Persona):
    def __init__(self, nombre, edad, saldo):
        super().__init__()
        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo

    def mostrar_saldo(self):
        print("El saldo actual de {} es: {}".format(self.nombre, self.saldo))


    def transferencia(self, persona_2,monto):
        if self.saldo >= monto:
            self.saldo -= monto
            persona_2.saldo += monto
        else:
            print("El saldo que tienes es insuficiente")


persona1 = Empleado("Pedro", 45, 3000)
persona2 = Empleado("Valeria", 25, 2000)

persona1.transferencia(persona2, 2000)
persona1.mostrar_saldo()
# persona 2
persona2.mostrar_saldo()