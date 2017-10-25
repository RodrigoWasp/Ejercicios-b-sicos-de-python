#!/usr/bin/env python
# -*- coding: utf-8 -*-



class Err(Exception):
    def __init__(self,val):
        print("fue el error por ", val)


try:
    raise Err(4)
except:
    print("Error de entorno")
