#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Clase encargada de efectuar una suma de números
# a partir de una cadena.
class Calculadora:

    # Función encargada de hacer la suma de un listado
    # de números que entran por parámetro, separados por
    # ",", "&" o ":"
    def sumar(self, cadena):
        if len(cadena) == 0:
            return 0
        elif len(cadena) == 1:
            return 1
        else:
            if "," in cadena or ":" in cadena or "&" in cadena:
                cadena = cadena.replace(":", ",")
                cadena = cadena.replace("&", ",")
                array = cadena.split(",")
                cont = 0

                for a in array:
                    cont += int(a)

                return cont

            else:
                raise ValueError("El formato de la cadena es incorrecto.")