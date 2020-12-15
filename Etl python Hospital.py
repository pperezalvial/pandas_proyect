# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import datetime as dt
import seaborn as sb #libreria para cambiar nombre a columnas
import numpy as np
import pandas as pd
import glob
import shutil
import time
import glob
import math
import os

path = r"C:/Users/manuel.caceres/Documents/proyectos"


excel_files = glob.glob(path + '/*.xlsx')

#Creamos una lista vacía sobre la cual vamos a ir añadiendo dataframes, y a continuación escribimos un loop para ir leyendo los ficheros que tienen el patrón generado anteriormente.


list_data = []


# Escribimos un loop que irá a través de cada uno de los nombres de archivo a través de globbing y
#el resultado final será la lista dataframes


for filename in excel_files:
    data = pd.read_excel(filename, index_col=None, header=0)
    #cambiar nombres de columna
    data.columns    
    data = data.rename(columns={'FECHA HORA ADMISION':'fecha_admision', 'NUMERO DAU': 'nro_dau', 'PREVISION INGRESO': 'prevision'})
    #cambiar formato a fecha datetime64
    data['fecha_admision'].apply(pd.to_datetime, format="%d/%m/%Y") 
    data['fecha_admision'] = pd.to_datetime(data["fecha_admision"].dt.strftime('%Y-%m'))

    #realiza un append o outter join y lista los datos de los excel
    list_data.append(data)

#muestra los datos del objeto 

#data = pd.DataFrame(list_data)
#datos = (path +'/output.csv')
#data.to_csv(datos, index=False, encoding='utf-8')


frame = pd.concat(list_data,ignore_index=True)
 
frame.to_excel(path +'/PRUEBA04.xlsx' ,engine='xlsxwriter')

frame