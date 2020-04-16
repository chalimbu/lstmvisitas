import unittest
import extraer_data_modelo_persistente

class TestExtraerDataModeloPersistente(unittest.TestCase):

    def test_debe_validar_los_tipos_de_datos(self):
        self.assertRaises(TypeError, lambda: extraer_data_modelo_persistente.extraer_data_modelo_persistente(1))
        self.assertRaises(TypeError, lambda: extraer_data_modelo_persistente.extraer_data_modelo_persistente([[1,2],""]))

    def test_debe_validar_que_las_listas_tengan_dos_elementos(self):
        self.assertRaises(ValueError,
                          lambda: extraer_data_modelo_persistente.extraer_data_modelo_persistente([[1, 2], [1]]))

    def test_debe_retornar_lista_vacias_cuando_se_le_entrega_una(self):
        resultado_esperado= [],[]
        self.assertEqual (resultado_esperado,
                          extraer_data_modelo_persistente.extraer_data_modelo_persistente([]))

    def test_debe_retornar_dos_lista_con_los_datos_separados(self):
        datos=[[3, 2], [2, 1], [1, 5], [5, 1],[1,6]]
        resultado_esperado= [3,2,1,5,1],[2,1,5,1,6]
        self.assertEqual (resultado_esperado,
                          extraer_data_modelo_persistente.extraer_data_modelo_persistente(datos))