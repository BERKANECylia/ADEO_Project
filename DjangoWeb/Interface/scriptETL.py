import pandas as pd
from django.db import connection

from .models import ProgramTable, mergedTables

def showMissingValues(df):
    df_new=df.isnull().sum().reset_index().rename(columns={'index': 'Column', 0: 'count'})
    return(df_new)