import unittest
import escalar_entre_m1_y_1

class TestEscalarEntreM1Y1(unittest.TestCase):

    def test_escalar_entre_m1_Y_1_valida_parametros(self):
        """se le debe pasar una lista y esta lista debe ser de enteros"""
        self.assertRaises(TypeError, escalar_entre_m1_y_1.escalar_entre_m1_y_1, 1)
        self.assertRaises(TypeError, escalar_entre_m1_y_1.escalar_entre_m1_y_1, [3, 2, "4"])

    def test_escalar_entre_m1_Y_1_valida_que_la_lista_tenga_dos_elementos_distintos(self):
        self.assertRaises(ValueError, escalar_entre_m1_y_1.escalar_entre_m1_y_1, [])
        self.assertRaises(ValueError, escalar_entre_m1_y_1.escalar_entre_m1_y_1, [1])
        self.assertRaises(ValueError, escalar_entre_m1_y_1.escalar_entre_m1_y_1, [4,4])

    def test_escalar_entre_m1_Y_1_devuelve_el_mayor_y_menor_valor(self):
        min1,max1,lista1 = escalar_entre_m1_y_1.escalar_entre_m1_y_1([1,10,3,5,8])
        self.assertEqual(min1,1)
        self.assertEqual(max1,10)
        min2, max2, lista2 = escalar_entre_m1_y_1.escalar_entre_m1_y_1([0.58, 0.49, 0.18, 0.148, 0.378])
        self.assertEqual(min2,0.148)
        self.assertEqual(max2,0.58)

    def test_escalar_entre_m1_Y_1_escala(self):
        non, non, lista1 = escalar_entre_m1_y_1.escalar_entre_m1_y_1([10,9])
        self.assertEqual(lista1,[1,-1])
        non, non, lista2 = escalar_entre_m1_y_1.escalar_entre_m1_y_1([8, 9,10])
        self.assertEqual(lista2, [-1, 0, 1])
        non, non, lista3 = escalar_entre_m1_y_1.escalar_entre_m1_y_1([200, 100, 400,-100,30])
        self.assertEqual(lista3, [0.19999999999999996, -0.19999999999999996, 1.0, -1.0, -0.48])
