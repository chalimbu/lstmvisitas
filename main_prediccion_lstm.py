import tensorflow
import cargar_info
import slices
import sumar_lista
import escalar_entre_m1_y_1
import generar_lista_con_saltos
import extraer_data_modelo_persistente
import calcular_raiz_error_cuadratico_medio
import extraer_data_modelo_lstm
import dividir_entrenamiento_pruebas
import generar_modelo_lstm
import entrenar_modelo
import tensorflow as tf
import callback_guardar

tensorflow.random.set_seed(21)#garantiza reproducibilidad

visitas_diarias=cargar_info.cargar_info("AnalyticsAllWebSiteDataVisióngeneraldelaaudiencia20141001-20200226.csv")
slices_semanas= slices.obtener_slices_de_tamanio(lista_elementos=visitas_diarias,slice=7)
semanas_sumarizadas=list(map(sumar_lista.sumar_lista,slices_semanas))
min,max,semanas_estandarizadas = escalar_entre_m1_y_1.escalar_entre_m1_y_1(semanas_sumarizadas)
registros_serie_tiempo=generar_lista_con_saltos.generar_lista_con_saltos(tamanio_listas=31,salto_entre_elemento=7,lista=semanas_estandarizadas)
print("numero de registro para el modelo lstm "+str(len(registros_serie_tiempo)))
array_x,array_y=extraer_data_modelo_lstm.extraer_data_modelo_lstm(registros_serie_tiempo)
x_entreno,y_entreno,x_pruebas,y_pruebas=\
    dividir_entrenamiento_pruebas.dividir_entrenamiento_pruebas(0.2,array_x,array_y)
print("shape of x is"+str(x_entreno.shape))
print("shape of x is"+str(y_entreno.shape))
print("shape of x is"+str(x_pruebas.shape))
print("shape of x is"+str(y_pruebas.shape))
modelo_lstm=generar_modelo_lstm.generar_modelo_lstm(x_entreno)
callback_guardar=callback_guardar.callback_guardar("modelos/modelo3/epoch1000")
#cargar un modelo guardado
#checkpoint_path_charge = "modelos/modelo2/epoch1000"
#modelo_lstm.load_weights(checkpoint_path_charge)
modelo_entrenado=entrenar_modelo.entrenar_modelo(modelo=modelo_lstm,x_entreno=x_entreno,y_entreno=y_entreno,x_pruebas=x_pruebas,y_pruebas=y_pruebas,callbacks=[callback_guardar])
#print(modelo_entrenado.history.keys()) ##dict_keys(['loss', 'val_loss'])
print("loss"+str(modelo_entrenado.history['loss']))
print("val_loss"+str(modelo_entrenado.history['val_loss']))
