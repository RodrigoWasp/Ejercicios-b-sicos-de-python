#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
archivo  = open("texto.txt","r")
for linea in archivo:
    print(linea)
"""
#iteracion sencilla y facil de entender

#generadores
def numeros():
    n = 1
    while True:
        yield n
        n = n+1
i = numeros()
print(i)
print(i.__next__())
print(i.__next__())
print(i.__next__())
