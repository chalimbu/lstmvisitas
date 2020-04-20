def entrenar_modelo(modelo,x_entreno,y_entreno,x_pruebas,y_pruebas,callbacks):
    samples,din1,din2=x_entreno.shape
    return modelo.fit(x=x_entreno,y=y_entreno,epochs=10,validation_data=(x_pruebas,y_pruebas),batch_size=samples,callbacks=callbacks)