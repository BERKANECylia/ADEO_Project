from django.db import connection

def showMissingValues(df):
    df_new=df.isnull().sum().reset_index().rename(columns={'index': 'Column', 0: 'count'})
    #comment
    return(df_new)

def mergeTables(dfADR,dfPRG,dfSTU):
    result="Tables Merged in version V"
    return(result)

# 17-may-19
def return_distinct_prg(df):
    df_prg_uniq=df['PRG'].unique().tolist()     ## later try sorting alphabetically
    return(df_prg_uniq)

def return_distinct_ville(df):
    df_ville_uniq = df['VILLE'].unique().tolist()
    return(df_ville_uniq)

def return_distinct_cp(df):
    df_cp_uniq = df['CODE_POSTAL'].unique().tolist()
    return (df_cp_uniq)

def return_distinct_rem(df):
    df_Rem_uniq = df['REMUNERATION'].unique().tolist()
    return (df_Rem_uniq)

def return_distinct_year(df):
    df_year_uniq = df['ANNEE_SCOLAIRE'].unique().tolist()
    return (df_year_uniq)
