from django.db import connection

def showMissingValues(df):
    df_new=df.isnull().sum().reset_index().rename(columns={'index': 'Column', 0: 'count'})
    #comment
    return(df_new)