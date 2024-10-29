from ..SerVivo import SerVivo

class Persona(SerVivo):

    def __init__(self, nombre, apellido, documento, genero, direccion, telefono):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__documento = documento
        self.__genero = genero
        self.__direccion = direccion
        self.__telefono = telefono
        super().__init__()

    def setNombre(self, nombre):
        if(len(nombre) > 3):
            self.__nombre = nombre
        else:
            print("Error, el nombre no cumple con la validación")
    
    def getNombre(self):
        return self.__nombre
    
    def setApellido(self, apellido):
        self.__apellido = apellido

    def getApellido(self):
        return self.__apellido
    
    def setDocumento(self, documento):
        self.__documento = documento

    def getDocumento(self):
        return self.__documento
    
    def setGenero(self, genero):
        self.__genero = genero

    def getGenero(self):
        return self.__genero
    
    def setDireccion(self, direccion):
        self.__direccion = direccion

    def getDireccion(self):
        return self.__direccion

    def setTelefono(self, telefono):
        self.__telefono = telefono

    def getTelefono(self):
        return self.__telefono
