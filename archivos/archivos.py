# -*- coding: utf-8 -*-
#!/usr/bin/env python

#-- tutorial para crear archivos en python


#creamos nuestra funcion para poder crear un archivo, siempre que se desee crear el archivo
#es necesario poner el argumento "w" en la segunda posicion del
def creararchivo():
    archivo = open("texto.txt","w")
    archivo.close()

def escribirarchivo():
    mensaje = input().strip()
    archivo = open("texto.txt","a")
    archivo.write(mensaje + "\n")
    archivo.close()
def leerarchivo():
    archivo = open("texto.txt","r")
    for linea in archivo:
        print(linea)
    archivo.close()


escribirarchivo()
leerarchivo()
