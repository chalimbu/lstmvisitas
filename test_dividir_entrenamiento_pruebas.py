import unittest
import dividir_entrenamiento_pruebas

class TestExtraerDataModeloLstm(unittest.TestCase):

    def test_debe_validar_los_tipos_de_datos(self):
        self.assertRaises(TypeError, lambda: dividir_entrenamiento_pruebas.dividir_entrenamiento_pruebas(3,[[1],[2],[3]],[3,4,5]))

    def test_valida_que_porcentaje_entrenamiento_sea_aceptable(self):
        self.assertRaises(ValueError, lambda: dividir_entrenamiento_pruebas.dividir_entrenamiento_pruebas(1.2,[[1],[2],[3]],[3,4,5]))

    def test_divide_los_datos(self):
        x_entreno,y_entreno,x_pruebas,y_pruebas=dividir_entrenamiento_pruebas.dividir_entrenamiento_pruebas(0.2,[[1],[2],[3],[4],[5]],[3,4,5,6,7])
        self.assertEqual(len(x_entreno),4)
        self.assertEqual(len(x_pruebas), 1)
        self.assertEqual(len(y_entreno), 4)
        self.assertEqual(len(y_pruebas), 1)
        self.assertEqual(y_pruebas, [7])