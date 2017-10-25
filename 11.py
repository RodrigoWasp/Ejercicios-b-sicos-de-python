#!/usr/bin/env python
# -*- coding: utf-8 -*-


#excepciones y cómo capturarlas
"""
lista = ["1","2"]
try:
    for i in range(2):
        print(lista[i])
except Exception:
    print("Error : indice fuera de rango en la revision de la lista...")
else:
    print("no hay error")
finally:
    print("proceso ejecutado")

"""
#excepciones y cómo lanzarlas
try:
    raise TypeError
except:
    print("errores con los tipos")
