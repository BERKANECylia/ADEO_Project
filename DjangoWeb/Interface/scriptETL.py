import numpy as np
import pandas as pd

def showMissingValues(df):
    df[df == ""] = np.nan
    df_new=df.isnull().sum().reset_index().rename(columns={'index': 'Column', 0: 'count'})
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
    df_year_uniq = df['ANNEE_SCOLAIRE'].str[:4].unique().tolist()
    return (df_year_uniq)

def redefineDFTypes(df):
    for column in df:
        if column in ['ID_ANO']:
            df[column]= df[column].astype(str).astype(np.int64)
        if column in ['PRG','ANNE_SCOLAIRE','ANNEE_SCOLAIRE']:
            df[column]= df[column].astype(str)
    # print(df.dtypes)
    return(df)

def mergeTables(ADR,PRG,STU):
    df=PRG
    df=df.merge(ADR,left_on=['ID_ANO'], right_on=['ID_ANO'])
    df=df.merge(STU,left_on=['ID_ANO','PRG','ANNE_SCOLAIRE'],right_on=['ID_ANO','ANNEE','ANNEE_SCOLAIRE'])
    df['VILLE']=df['VILLE'].str.upper()
    df['PAYS']=df['PAYS'].str.upper()
    df['ADR_VILLE']=df['ADR_VILLE'].str.upper()
    df=df.drop(columns='ANNEE')
    return(df)

def deleteMissingValues(df):
    df[df == ""] = np.nan
    df=df.dropna()      
    return(df)

def writeDF2Table(df, table, version, description):
    
    a=table.count()
    for index, rows in df.iterrows():

        # if str(rows.ADR_CP).isdigit():
        #     rows.ADR_CP= int(rows.ADR_CP)
        # else:
        #     rows.ADR_CP=0
        
        # if str(rows.CODE_POSTAL).isdigit():
        #     rows.CODE_POSTAL= int(rows.CODE_POSTAL)
        # else:
        #     rows.CODE_POSTAL=0
        
        table.create(
            ID_ANO          =rows.ID_ANO      ,
            PRG             =rows.PRG         ,
            ANNEE_SCOLAIRE  =rows.ANNEE_SCOLAIRE ,
            SITE            =rows.SITE        ,
            ADR_CP          =rows.ADR_CP      ,
            ADR_VILLE       =rows.ADR_VILLE   ,
            ADR_PAYS        =rows.ADR_PAYS    ,
            ANNEE           =rows.PRG       ,
            ENTREPRISE      =rows.ENTREPRISE  ,
            CODE_POSTAL     =rows.CODE_POSTAL ,
            VILLE           =rows.VILLE       ,
            PAYS            =rows.PAYS        ,
            SUJET           =rows.SUJET       ,
            REMUNERATION    =rows.REMUNERATION,
            idCSV           =version,
            idCSVDescript   =description
         )
    b=table.count()
    print(a,b,a-b)
    return(b-a)
