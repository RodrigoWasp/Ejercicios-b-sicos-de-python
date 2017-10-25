#!/usr/bin/env python
# -*- coding: utf-8 -*-

#polimorfismo

class Perro():
    def __init__(self):
        pass

    def avanzar(self):
        print("avanzando")

class Gato():
    def __init__(self):
        pass

    def avanzar(self):
        print("caminando")

def mover(animal):
    animal.avanzar()


#interpretacion del tipo de metodo que se ocupa en cada instancia del objeto
mauk = Gato()
sebita = Perro()
mover(mauk)
mover(sebita)
