#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from Calculadora import Calculadora

class CalculadoraTest(TestCase):
    def test_sumar(self):
        self.assertEqual(Calculadora().sumar(""), 0, "Sumar cadena vacía")
