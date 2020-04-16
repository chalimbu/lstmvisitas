import unittest
import service_logging
import logging

class TestLogginCreator(unittest.TestCase):
    """el servicio de logeo debe retornar un objeto de logging"""
    def test_clase_correcta(self):
        self.assertIsInstance(service_logging.obtenerLoggin(), logging.RootLogger)

    """el servicio de loggeo debe retornar un objeto de loggin que tenga nivel 10"""
    def test_nivel_loggeo(self):
        self.assertEqual(service_logging.obtenerLoggin().level,10)