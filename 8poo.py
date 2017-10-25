#!/usr/bin/env python
# -*- coding: utf-8 -*-

class circulo():

    def __init__(self,r = 1):
        self.radio = r

    def get_radio(self):
        return self.radio

    #propiedades propias de las clases, que tratan como atributo al lo procesado dentro de estos
    #ejemplo abajo:
    @property
    def area(self):
        val = 3.1416*((self.radio)**2)
        return round(val,2)



c = circulo(5)
print(c.radio)
#entrega del area como valor
print(c.area)
