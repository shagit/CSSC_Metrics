#!/usr/bin/python
# -*- coding: latin-1 -*-
import pandas as pd
import numpy as np
import pyodbc
import pandas.io.sql as psql
from pandas import *
from xlrd import *
import os.path
import csv
connection = pyodbc.connect('Driver={SQL Server};Server=INQ69NBOCBPWMV1;Database=Test;Trusted_Connection=yes;')
cursor = connection.cursor()
result = "SELECT * FROM OE_Count where Doc_Date='2015-06-01 00:00:00' "
df = pd.read_sql_query(result,connection)
table = pivot_table(df, values=["Document"], index=["Created"],columns=["SaTy"], aggfunc=lambda x: len(x.unique()))
print table