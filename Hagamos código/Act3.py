class persona:
    def __init__(self, nombre="", edad=0, dni="", telefono="", email=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.telefono = telefono
        self.email = email
    def nombre(self):
        return self.__nombre # getter que te devuelve un valor.
    def edad(self):
        return self.__edad
    def dni(self):
        return self.__dni
    def telefono(self):
        return self.__telefono
    def email(self):
        return self.__email
    def nombre(self, nombre):
        self.__nombre = nombre # debes introducir un valor.
    def validar_dni(self):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        if len(self.__dni) != 9:
            print("DNI incorrecto")
            self.__dni = ""
        else:
            letra = self.__dni[8]
            num = int(self.__dni[:8])
            if letra.upper() != letras[num % 23]:
                print("DNI incorrecto")
                self.__dni = ""
    def dni(self, dni):
        self.__dni = dni
        self.validar_dni()
    def edad(self, edad):
        if edad < 0:
            print("Edad incorrecta")
            self.__edad = 0
        else:
            self.__edad = edad
    def telefono(self, telefono):
        if len(telefono)!=9:
            print("teléfono no tiene 9 dígitos")
        else:
            print("teléfono correcto")
            self.__telefono = telefono
    def email(self, email):
        if "@" in email:
            print("El email es válido")
            self.email = email
        else:
            print("El email no es válido")
    def mostrar(self):
        return "Nombre:" + self.nombre + " - Edad:" + str(self.edad) + " - DNI:" + self.dni + " - Teléfono:" + self.telefono + " - Email:" + self.email
    def esMayorDeEdad(self):
        return self.edad >= 18

prueba = persona("pepe", "123456789X", "58", "644017098", "reu@gmail.com")
p=persona.mostrar(prueba)
print(p)
