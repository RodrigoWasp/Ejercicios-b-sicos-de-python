#!/usr/bin/env python
# -*- coding: utf-8 -*-

#funciones que encierran otras
def funcionA(x):
    def funcionb(y):
        return x+y
    return funcionb

"""
valor = funcionA(5)
print(valor(3))
"""
## decoradores

#fuciones que modifican otras funciones

def primerD(funcion):
    def funciondecorada(*args,**kkwars):
        print("primer decorador")
    return funciondecorada

@primerD
def funcion():
    print("Mi primer decorador")

funcion()
