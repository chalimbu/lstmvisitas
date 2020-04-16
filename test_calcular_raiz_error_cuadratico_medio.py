import unittest
import calcular_raiz_error_cuadratico_medio

class TestCalcularErrorCuadraticoMedio(unittest.TestCase):

    def test_calcular_error_cuadratico_medio_valida_datos(self):
        self.assertRaises(TypeError,lambda: calcular_raiz_error_cuadratico_medio.calcular_raiz_error_cuadratico_medio(1,[1]))
        self.assertRaises(TypeError, lambda: calcular_raiz_error_cuadratico_medio.calcular_raiz_error_cuadratico_medio([1], 1))
        self.assertRaises(TypeError, lambda: calcular_raiz_error_cuadratico_medio.calcular_raiz_error_cuadratico_medio([1,"uno"], [1,1]))

    def test_verifica_que_la_lista_de_verdaderor_y_esperados_es_del_mismo_tamanio(self):
        self.assertRaises(ValueError,
                          lambda: calcular_raiz_error_cuadratico_medio.calcular_raiz_error_cuadratico_medio([1, 3], [1, 1,4]))

    def test_si_la_prediccion_es_igual_al_valor_el_error_es_0(self):
        self.assertEqual(0,
                          calcular_raiz_error_cuadratico_medio.calcular_raiz_error_cuadratico_medio([1, 3,2],
                                                                                                            [1, 3, 2]))

    def test_si_la_prediccion_es_diferente_al_valor_real_calcular_el_error(self):
        self.assertAlmostEqual(0.4092676,
                          calcular_raiz_error_cuadratico_medio.calcular_raiz_error_cuadratico_medio([3.4,2,1,0],
                                                                                                            [3, 1.5, 0.5,-0.1]))
