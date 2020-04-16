import unittest
import slices

class TestSlicesGenerador(unittest.TestCase):

    def test_validacion_tipo_parametros(self):
        """el metodo de crear slices debe validar que los tipos de paramteros que se le pasan son los esperados"""
        #primer parametro una lista
        self.assertRaises(TypeError, slices.obtener_slices_de_tamanio,(132,1))
        #segundo parametro un entero
        self.assertRaises(TypeError, slices.obtener_slices_de_tamanio,([], []))

    def test_validacion_valores_parametros(self):
        #los slices deben ser de tamaño 1 o mas para poder crearlos
        any_list=[1,2,"3"]
        self.assertRaises(ValueError,lambda: slices.obtener_slices_de_tamanio(any_list,-1))
        self.assertRaises(ValueError, lambda: slices.obtener_slices_de_tamanio(any_list,0))

    def test_tipo_valor_retorno(self):
        #si la funcion termina bien debe retornar una lista
        any_list=[1,2,"3"]
        self.assertIsInstance(slices.obtener_slices_de_tamanio(any_list,1), list)

    def test_retorne_slices_tamanio_uno(self):
        # si la funcion termina bien debe retornar una lista
        tamanio_slice=1
        primera_lista = [1, 2, 3]
        self.assertEqual(slices.obtener_slices_de_tamanio(primera_lista,tamanio_slice),[[1],[2],[3]])
        segunda_lista = ["1","2","3","4","5"]
        self.assertEqual(slices.obtener_slices_de_tamanio(segunda_lista,tamanio_slice),[["1"],["2"],["3"],["4"],["5"]])

    def test_retorne_slices_tamanio_dos(self):
        # si la funcion termina bien debe retornar una lista
        tamanio_slice=2
        primera_lista = [1, 2, 3]
        self.assertEqual(slices.obtener_slices_de_tamanio(primera_lista,tamanio_slice),[[1,2],[2,3]])
        segunda_lista = ["1","2","3","4","5"]
        self.assertEqual(slices.obtener_slices_de_tamanio(segunda_lista,tamanio_slice),
                         [["1","2"],["2","3"],["3","4"],["4","5"]])
        tercera_lista= [3,2,1,5,1]
        self.assertEqual(slices.obtener_slices_de_tamanio(tercera_lista, tamanio_slice),
                         [[3,2],[2,1],[1,5],[5,1]])
