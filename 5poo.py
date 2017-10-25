# -*- coding: utf-8 -*-
#!/usr/bin/env python

#Ejemplo de clase para practica con python

#clase : plantilla basica de una cosa representada en un programa
#atributos : caracteristicas de la cosa representada en el programa descrito
#metodos : funciones del objeto en la vida real

class Persona:
    #atributos
    nombre = ""
    apellido = ""
    edad = 0
    correo = "@gmail.com"
    #metodos
    def __init__(self):
        self.nombre = ""
        self.apelido = ""
        self.edad = 0
        self.correo = ""

    def get_nombre(self):
        return self.nombre

    def set_nombre(self,args):
        self.nombre = args

    def get_apellido(self):
        return self.apellido
    def set_apellido(self,args):
        self.apellido = args

# -- caso de herencia en python --
class hombre(Persona):
    sexo = "M"
    def saludo():
        print("hello world")

class mujer(Persona):
    sexo = "F"

    def saludo():
        print("Hello friend")

# --- fin del comentario ---

def main():
    #manera de instanciar una clase
    Rodrigo = Persona()
    print(type(Rodrigo))
    #prueba de metodo en el objeto instanciado
    Rodrigo.set_nombre("Rodrigo")
    print(Rodrigo.get_nombre())
    #herencia
    Rossana = mujer()
    print(type(Rossana))
    Rossana.set_nombre("Rossana")
    print(Rossana.get_nombre())

main()
