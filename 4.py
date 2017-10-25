# -*- coding: utf-8 -*-
#!/usr/bin/env python

#-- map --

# la funcion map aplica una funcion a un valor entregado map(funcion a usar, variable a modificar)

# -- fin comentario --

#toma un string y lo splitea, lo transforma en lista

n = list(map(str,input().strip().split()))
print(n)

# ----------------

# crea una lista nueva y convierte los datos de la lista anterior en enteros
x = list(map(int,n))
for i in x:
    print(i, end=" ")
print("")
# ----------------
