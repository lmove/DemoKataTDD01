#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from Calculadora import Calculadora

class CalculadoraTest(TestCase):

    def test_sumar_cadena_vacia(self):
        self.assertEqual(Calculadora().sumar(""), 0, "Sumar cadena vacía")

    def test_sumar_cadena_un_numero(self):
        self.assertEqual(Calculadora().sumar("1"), 1, "Sumar cadena con un número")