from .Persona import Persona

class Alumno(Persona):
    
    def __init__(self, matricula, habilidades, intereses, nombre, apellido, documento, genero, direccion, telefono):
        self.__matricula = matricula
        self.__habilidades = habilidades
        self.__intereses = intereses
        super().__init__(nombre, apellido, documento, genero, direccion, telefono)
     
    