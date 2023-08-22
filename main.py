class Auto:
    cantidadCreados = 0
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        c_asientos = 0
        for i in self.asientos:
            if i != None:
                c_asientos = c_asientos + 1
        return c_asientos


    def verificarIntegridad(self):
        verificado = False
        if self.motor.registro == self.registro:
            for i in self.asientos:
                if i != None:
                    if i.registro != self.registro:
                        verificado = True
                        break
            if verificado == False:
                return "Auto original"
            else:
                return "Las piezas no son originales"
        else:
            return "Las piezas no son originales"




class Motor:
    def __init__(self, numeroCilindros,tipo,registro):
        self.numeroCilindos = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self,registro):
        self.registro =  registro

    def asignarTipo(self,tipo):
        if  tipo == "electrico" or tipo == "gasolina":
            self.tipo = tipo


class Asiento:
    def __init__(self,color,precio,registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self,color):
        colores = ["rojo","verde","amarillo","negro","blanco"]
        if color in colores:
            self.color  = color

