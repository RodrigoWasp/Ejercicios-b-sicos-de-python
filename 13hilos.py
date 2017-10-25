#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import time
#manejo de hilo de trabajo

#en proceso de entendimiento
class Mihilo(threading.Thread):
    def run(self):
        print("Inicio : {}".format((self.getName())))
        time.sleep(2)
        print("Fin : {}".format(self.getName()))

def main():
    for x in range(4):
        #mismo objeto, distintos hilos
        hilo = Mihilo(name = "Thread - {}".format(x+1))
        hilo.start()
        time.sleep(.5)

main()
