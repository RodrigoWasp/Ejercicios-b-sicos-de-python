#!/usr/bin/env python
# -*- coding: utf-8 -*-

def lower(elementos): return elementos.lower()

lista = ["RoDRiGo", "jUaN","dIEgO"]
print(list(map(lower,lista)))
print([cad.lower() for cad in lista])

def saludo(idioma):
    def saludo_es():
        print("hola")
    def saludo_en():
        print("hello")
    idioma_func = {"es":saludo_es,
                    "en":saludo_en,
                    }
    return idioma_func[idioma]

saludar = saludo("en")
saludar()
