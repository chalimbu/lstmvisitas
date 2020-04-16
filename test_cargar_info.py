import unittest
import cargar_info

class TestCargarInfo(unittest.TestCase):

    def test_valida_tipo_parametros(self):
        self.assertRaises(TypeError,lambda: cargar_info.cargar_info(1))
        self.assertRaises(TypeError, lambda: cargar_info.convertir_numero_formato_analitics(1))


    def test_carga_datos_del_archivo_mock(self):
        self.assertEqual([2473, 2370, 2240, 1296, 843, 2233, 2113, 2139, 1990, 1738, 969, 672, 1113, 2105, 2216, 1700],cargar_info.cargar_info("mock-visitas.csv"))

    def test_permite_convertir_solo_numero_hasta_999999(self):
        self.assertRaises(ValueError, lambda: cargar_info.convertir_numero_formato_analitics("111.112.13"))

    def test_si_se_le_pasan_un_numero_no_valido(self):
        self.assertRaises(ValueError, lambda: cargar_info.convertir_numero_formato_analitics("111.dos"))

    def test_convierto_un_numero_en_formato_analitics(self):
        self.assertEqual(11, cargar_info.convertir_numero_formato_analitics("11"))
        self.assertEqual(1120, cargar_info.convertir_numero_formato_analitics("1.12"))
        self.assertEqual(2233, cargar_info.convertir_numero_formato_analitics("2.233"))
        self.assertEqual(1990, cargar_info.convertir_numero_formato_analitics("1.99"))