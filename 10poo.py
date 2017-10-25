#!/usr/bin/env python
# -*- coding: utf-8 -*-

class intro():

    def __init__(self,dato):
        self.dato = dato
    def seg(self):
        print("segundo")
    def ter(self):
        print("tercero")

dato = intro("valor")
dir(dato)
print(dir(dato))
# pregunta si la intancia es instancia de la clase. True o False
print(isinstance(dato,intro))

#Pregunta si existe el atributo o metodo dentro de la clase
#en este caso retorna un true
print(hasattr(intro,"seg"))
#en este caso "funciondistitnta" no pertenece a la clase intro, por ende retorna
#un false
print(hasattr(intro,"funciondistinta"))
