#!/usr/bin/env python
# -*- coding: utf-8 -*-

#variables de instancia
#variables que se relacionan unicamente con la instancia de la clase a la que
#pertenecen

#variables de clase
#variables que corren para toda la clase en general

class Persona():
    #variable de clase
    apellido = ""
    edad = 18

    def __init__(self,nombre,nacionalidad):
        #variables de instancia
        self.nombre = nombre
        self.nacionalidad = nacionalidad
    #metodo de instancia
    def saludar(self):
        print("Hola amigo...")


class Hombre():

    def __init__(self):
        pass
    def despedir(self):
        print("Adios")

    @classmethod
    def saludar(cls, nombre):
        print("estoy saludando a "+nombre)

Hombre.saludar("Walala")
