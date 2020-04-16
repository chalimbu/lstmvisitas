import unittest
import sumar_lista

class TestSumarLista(unittest.TestCase):

    def test_sumar_lista_valida_parametros(self):
        """se le debe pasar una lista y esta lista debe ser de enteros"""
        self.assertRaises(TypeError, sumar_lista.sumar_lista ,1)
        self.assertRaises(TypeError, sumar_lista.sumar_lista, [3,2,"4"])

    def test_sumar_lista_devuelve_la_suma(self):
        self.assertEqual(sumar_lista.sumar_lista([1,2,3,4]),(1+2+3+4))
        self.assertEqual(sumar_lista.sumar_lista([0.5, 1.5, 3, 4]), 9)