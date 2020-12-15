# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 10:22:25 2019

@author: rabarral
"""

from datetime import timedelta
import datetime as dt
import pandas as pd
import numpy as np
import shutil
import time
import glob
import math
import os

path = r"C:/Users/ppereza/Documents/Exclusión/Cobranza/PRUEBA"
os.chdir(path +'/')
extension = 'bak'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

def etl_raw_antidx(f):
    
    # Using Pandas with a column specification
    col_specification = [(0, 9), (10, 65), (65, 75), (75, 85),
                         (85, 90), (95, 125), (125, 140), (141,170),
                         (170,195), (185,195), (195,215), (216,230),
                         (317,324), (324,335), (336,349), (349,360),
                         (361,419), (419,424), (424,439), (439,494),
                         (494,520), (520,546), (546,604), (640,670),
                         (670,704), (704,755), (755,810), (810,855), 
                         (855,905), (905,955)]

    header = ['suscriptor', 'nombre_cliente', 'ini_adx', 'fin_adx',
              'prioridad', 'ciclo_base', 'ip', 'base',
              'fono1', 'fono2', 'fono3', 'fono4', 
              'proxy', 'moroso', 'fech_vcto', 'mop', 
              'fech_dx', 'mes_campania', 'fecha_maxima_convenio', 'prioridad2', 
              'score', 'mora_dias', 'fech_hold_1', 'fech_hold_2', 
              'fech_hold_3', 'fech_hold_4', 'fech_hold_5', 'fech_hold_6', 
              'fech_hold_7', 'fech_hold_8']
    
    #lo de converters es para mantener (o dejar en str) la data desde el origen, y que panda no transforme segun su criterio
    df = pd.read_fwf(f, 
                     colspecs=col_specification, 
                     header=None, 
                     names = header, 
                     converters={h:str for h in header})
    
    #Elimino columnas que no uso
    df = df.drop(columns = ['nombre_cliente',
                            'prioridad',
                          
                            'fono1',
                            'fono2',
                            'fono3',
                            'fono4',
                            'mes_campania',
                            'fecha_maxima_convenio',
                            'score',
                            'mora_dias',
                            'fech_hold_1',
                            'fech_hold_2',
                            'fech_hold_3',
                            'fech_hold_4',
                            'fech_hold_5',
                            'fech_hold_6',
                            'fech_hold_7',
                            'fech_hold_8'])
    #Transforma a fecha
    df[['ini_adx','fin_adx','fech_vcto','fech_dx']] = df[['ini_adx','fin_adx','fech_vcto','fech_dx']]\
                                                    .apply(pd.to_datetime, format="%d/%m/%Y")     
    return df

df = pd.concat([etl_raw_antidx(f) for f in all_filenames])

#Si quiero exportar la union completa de las bases Anti
df.to_csv(path +'/PRUEBA03.csv',
          sep = '|' ,
          index=False,
          index_label=False,
          date_format='%d-%m-%Y')
