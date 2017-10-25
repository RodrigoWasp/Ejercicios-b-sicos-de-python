# -*- coding: utf-8 -*-
#!/usr/bin/env python

#metodos propios de la intancia, metodos de clase, estáticos y dinamicos



class A():
    def __init__(self):
        pass

    #prueba de funcion tipo lambda
    def potencia(self,dato):
        f = lambda x: x**2
        self.valor  = f(dato)

    def saltar(self):
        print("salto")
    #un metodo de clase, permite manipular los parametros propios de la clase
    @classmethod
    def correr(cls):
        print("corro")
    #un metodo estatico es un metodo que solo accede a las variables de la clase donde se le escribe
    #permite ordenar funciones que operan con la clase, pero sin la necesidad de instancia
    @staticmethod
    def nadar():
        print("nado")

new = A()
new.potencia(2)
print(new.valor)
A.nadar()
