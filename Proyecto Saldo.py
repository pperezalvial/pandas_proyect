# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 10:22:25 2019

@author: rabarral
"""

#from datetime import timedelta
#import datetime as dt
import pandas as pd
#import numpy as np
#import shutil
#import time
import glob
#import math
import os

path = r"C:/Users/ppereza/Documents/pago/"
os.chdir(path +'/')
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
os.chdir(path)
#types={'SUSCRIPTOR':str, 'SALDO MONEDERO':str, 'SALDO IBS':str}
df = pd.concat([pd.read_csv(f   , sep=';', dtype={'SUSCRIPTOR':str, 'SALDO MONEDERO':str, 'SALDO IBS':str}) for f in all_filenames])

#Si quiero exportar la union completa de las bases Anti
df.to_excel(path +'/saldos.xlsx',
          index=False,
          index_label=False)
#          date_format='%d-%m-%Y')
