class Auto:
    cantidadCreados = 0
    def __init__(self,modelo,precio,asientos,marca,motor,registro,cantidadCreados):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadCreados = cantidadCreados

    def cantidadAsientos(self):
        asientos = 0
        for i in asientos:
            if i != null:
                asientos = asientos + 1
        return asientos


    def verificarIdentidad(self):
        bool verificado = False
        if self.motor.registro == self.registro:
            for i in asientos:
                if i != null:
                    if i.registro != self.registro:
                        verificado = True
                        break
            if verificado == False:
                return "Auto original"
            else:
                return "Las piezas no son originales"
        else:
            return "Las piezas no son originales"


