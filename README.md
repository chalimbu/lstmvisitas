# lstmvisitas

Haciendo uso de redes neuronales LSTM para predecir el numero de visitas a un sitio.

## Para instalar el proyecto.

Despues de clonarlo, se pueden instalar las dependencias/librerias mediante un ambiente de conda con el comando

**conda env create -f environment.yml**

Luego se puede activar el ambiente con el comando 

**conda activate lstmvisitas**

se recomienda ademas correr las pruebas unitarias para verificar qeu todo este bien con el comando 

**python -m unittest**

## Para correr el proyecto.

el archivo original de visitas es reservado pero en recursos se encuentra un mock de que estructura debe tener el archivo.
los arhivos main_xxxxxxx.py estan pensandos para que se corran con python asi.

**python main_xxxxxxx.py**

se probaron 13 modelos LSTM y un modelo persistente(que demostro mejores resultados por caminata aleatoria, para un documentacion completa del analisis realizado,graficas y documentacion ponerse en contacto conmigo)
para moverse a un modelo en especifico solamente se debe mover a la rama correspondiente

**git checkout feature/modelo[1-13]**

Saludos.
