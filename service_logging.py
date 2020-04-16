import logging

def obtenerLoggin():
    """retorna un objeto loggin que se usara para logear la informacion/debugeo de la aplicacion a un archivo
    el loggin creado escribe al archivo logging y es nivel 10 permitiendo que todos los mensajes de loggin vayan al
    archivo"""
    # create and configure logger
    LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(filename="D:\\copia\\materias\\trabajo grado\\codigo de trabajo de grado\\desarrollo\\logging",
                        level=logging.DEBUG,
                        format=LOG_FORMAT)
    return logging.getLogger()