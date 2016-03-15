#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from Calculadora import Calculadora

class CalculadoraTest(TestCase):

    # Prueba encargada de validar el retorno de 0 [ara una cadena vacía.
    def test_sumar_cadena_vacia(self):
        self.assertEqual(Calculadora().sumar(""), 0, "Sumar cadena vacía")

    # Prueba encargada de validar la suma de un solo número.
    def test_sumar_cadena_un_numero(self):
        self.assertEqual(Calculadora().sumar("1"), 1, "Sumar cadena con un número")

    # Prueba encargada de validar la suma de dos números separados por ",".
    def test_sumar_cadena_dos_numeros(self):
        self.assertEqual(Calculadora().sumar("1,2"), 3, "Sumar cadena con dos números")

    # Prueba encargada de validar la suma de varios números separados por ",".
    def test_sumar_cadena_varios_numeros(self):
        self.assertEqual(Calculadora().sumar("1,2,5,7,3"), 18, "Sumar cadena con varios números")

    # Prueba encargada de validar la suma de varios números separados por ",", "&" y/o ":".
    def test_sumar_cadena_varios_numeros_separadores(self):
        self.assertEqual(Calculadora().sumar("1&3:4,8&2:6,5"), 29, "Sumar cadena con varios números y separadores")