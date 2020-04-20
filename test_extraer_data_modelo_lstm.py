import extraer_data_modelo_lstm
import unittest
import numpy

class TestExtraerDataModeloLstm(unittest.TestCase):

    def test_debe_validar_los_tipos_de_datos(self):
        self.assertRaises(TypeError, lambda: extraer_data_modelo_lstm.extraer_data_modelo_lstm(1))

    def test_debe_validar_que_almenos_halla_un_elemento_de_datos(self):
        self.assertRaises(ValueError, lambda: extraer_data_modelo_lstm.extraer_data_modelo_lstm([]))

    def test_debe_validar_que_si_hay_varios_registros_todos_tengan_el_mismo_tamanio(self):
        self.assertRaises(ValueError, lambda: extraer_data_modelo_lstm.extraer_data_modelo_lstm([[1,2,3],[4,5,6],[7,8],[8,9,10]]))

    def test_genera_los_datos_del_modelo_lstm(self):
        respuesta_esperada_x=numpy.array([[[3.],[1.],[2.]],[[1.],[4.],[5.]],[[9.],[7.],[8.]]], dtype=numpy.float32)
        respuesta_esperada_y= numpy.array([3., 6., 2.], dtype=numpy.float32)
        array_x,array_y=extraer_data_modelo_lstm.extraer_data_modelo_lstm([[3,1,2,3],[1,4,5,6],[9,7,8,2]])
        numpy.array_equal(respuesta_esperada_x,array_x)
        numpy.array_equal(respuesta_esperada_y,array_y)