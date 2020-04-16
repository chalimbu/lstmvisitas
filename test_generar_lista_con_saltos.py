import unittest
import generar_lista_con_saltos

class TestGenerarListaConSaltos(unittest.TestCase):

    def test_debe_validar_los_tipos_de_datos(self):
        #tercer parametro lista
        self.assertRaises(TypeError,lambda: generar_lista_con_saltos.generar_lista_con_saltos(1,2,3))
        #primer parametro entero
        self.assertRaises(TypeError, lambda: generar_lista_con_saltos.generar_lista_con_saltos("1", 2, []))
        #segundo parametro entero
        self.assertRaises(TypeError, lambda: generar_lista_con_saltos.generar_lista_con_saltos(1, "", []))

    def test_debe_validar_que_los_saltos_sean_almenos_de_uno(self):
        self.assertRaises(ValueError,lambda: generar_lista_con_saltos.generar_lista_con_saltos(1,0,[1,2,3]))
        self.assertRaises(ValueError,lambda: generar_lista_con_saltos.generar_lista_con_saltos(1,-1,[1,2,3]))

    def test_con_un_salto_de_uno_genera_slices_sin_saltos(self):
        primera_lista = [1, 2, 3]
        salto_entre_elemento=1
        self.assertEqual(generar_lista_con_saltos.generar_lista_con_saltos(1,salto_entre_elemento,primera_lista), [[1], [2], [3]])
        self.assertEqual(generar_lista_con_saltos.generar_lista_con_saltos(2,salto_entre_elemento, primera_lista), [[1, 2], [2, 3]])
        segunda_lista = [3, 2, 1, 5, 1 ,6]
        self.assertEqual(generar_lista_con_saltos.generar_lista_con_saltos(2,salto_entre_elemento, segunda_lista),
                         [[3, 2], [2, 1], [1, 5], [5, 1],[1,6]])
        self.assertEqual(generar_lista_con_saltos.generar_lista_con_saltos(3, salto_entre_elemento, segunda_lista),
                         [[3, 2,1], [2, 1,5], [1, 5,1], [5, 1,6]])

    def test_si_las_lista_son_tamanio_cero_retorna_lista_vacia(self):
        self.assertEqual(generar_lista_con_saltos.generar_lista_con_saltos(0, 1, [1,2,3,4]),
                         [])

    def test_debe_saltar_un_elemento_cuando_el_salto_sea_2(self):
        self.assertEqual(generar_lista_con_saltos.generar_lista_con_saltos(2, 2, [1,2,3,4]),
                         [[1,3],[2,4]])
        lista_prueba2=[1,3,4,1,2,3,4,8,6,4,2,3,4,5,63,2,3,4,5,1]
        self.assertEqual(generar_lista_con_saltos.generar_lista_con_saltos(4, 3, lista_prueba2),
                         [[1, 1, 4, 4],[3, 2, 8, 2],[4, 3, 6, 3],[1, 4, 4, 4],[2, 8, 2, 5],[3, 6, 3, 63],[4, 4, 4, 2],
                           [8, 2, 5, 3],[6, 3, 63, 4],[4, 4, 2, 5],[2, 5, 3, 1]])