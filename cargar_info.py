from pandas import read_csv

def cargar_info():
    series = read_csv('recursos/Analytics All Web Site Data Visión general de la audiencia 20141001-20200226.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
    #https://machinelearningmastery.com/time-series-forecasting-long-short-term-memory-network-python/
    #https://www.google.com/search?client=firefox-b-d&q=lstm+tensor+flow
    #https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM
    #https://www.tensorflow.org/guide/keras/rnn
    #https://www.tensorflow.org/tutorials/structured_data/time_series
    #https://www.google.com/search?newwindow=1&client=firefox-b-d&sxsrf=ALeKk02C-szJ7JvLL-H2DMRLvYRHwj-_1Q%3A1586957189208&ei=hQuXXvONDOeZ_Qbx24voDA&q=tf.keras.models.Sequential+loss&oq=tf.keras.models.Sequential+loss&gs_lcp=CgZwc3ktYWIQAzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQR0oJCBcSBTEyLTI5SggIGBIEMTItMlDMGljMGmCTHGgAcAJ4AIABAIgBAJIBAJgBAKABAaoBB2d3cy13aXo&sclient=psy-ab&ved=0ahUKEwiz5KScxOroAhXnTN8KHfHtAs0Q4dUDCAs&uact=5
    #https://www.tensorflow.org/api_docs/python/tf/keras/Sequential
    #https://www.tensorflow.org/api_docs/python/tf/keras/losses
    #https://www.google.com/search?client=firefox-b-d&q=mean_squared_error
    #https://www.google.com/search?client=firefox-b-d&q=read+csv+pandas
    #https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html