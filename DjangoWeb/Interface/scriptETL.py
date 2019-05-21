import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from math import radians, cos, sin, asin, sqrt

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
            df[column]=pd.to_numeric(df[column], errors='coerce')
            #df[column]= df[column].astype(str).astype(np.int64)
        if column in ['PRG','ANNE_SCOLAIRE','ANNEE_SCOLAIRE']:
            df[column]= df[column].astype(str)
        if column in ['REMUNERATION']:
            df[column]=pd.to_numeric(df[column], errors='coerce')
            # df[df[column] == ""] = "0"
            # df[column]= df[column].astype(np.float64)
            # df[df[column] == 0] = np.nan
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
    #print(df[pd.notnull(df['REMUNERATION'])])
    df=df[pd.notnull(df['REMUNERATION'])]
    df=df[pd.notnull(df['PRG'])]  
    df=df[pd.notnull(df['ANNEE_SCOLAIRE'])]  
    df=df[pd.notnull(df['CODE_POSTAL'])]  
    df=df[pd.notnull(df['ADR_CP'])]  
    df=df[pd.notnull(df['ADR_VILLE'])] 
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


# If User choose to update lines using algorithms
# By order 'PRG_STUDENT_SITE', 'ADR_STUDENTS', 'STUDENT_INTERNSHIP', 'df_location'
def UpdateMissingValues(ADR,PRG,STU,df_location):
    
    #updating missing values in ANNEE in table STU
    df=STU[STU['ANNEE'].isnull().T]
    for i in (df.index):
        df1=PRG[ PRG['ID_ANO']==STU.loc[i,'ID_ANO'] ]
        df2=df1[ df1['ANNEE_SCOLAIRE']==STU.loc[i,'ANNEE_SCOLAIRE'] ]
        STU.loc[i,'ANNEE']=df2['PRG'].values
    
    #updating missing values in ANNEE_SCOLAIRE in table STU
    df=STU[STU['ANNEE_SCOLAIRE'].isnull().T]
    for i in (df.index):
        df1=PRG[PRG['ID_ANO']==STU.loc[i,'ID_ANO']]
        df2=df1[df1['PRG']==STU.loc[i,'ANNEE']]
        STU.loc[i,'ANNEE_SCOLAIRE']=df2['ANNEE_SCOLAIRE'].values
    
    #updating missing values in CODE_POSTAL in table STU by the table df_location 
    df=STU[STU['CODE_POSTAL'].isnull().T]
    for i in (df.index):
        if df.loc[i,'VILLE']=='NaN':
            continue
        else:
            for j in (df_location.index):
                if df_location.loc[j,'VILLE']==STU.loc[i,'VILLE']:
                    STU.loc[i,'CODE_POSTAL']=df_location.loc[j,'CODE_POSTAL']
                    break
                    
    #updating missing values in VILLE in table STU by the table df_location
    df=STU[STU['VILLE'].isnull().T]
    for i in (df.index):
        if df.loc[i,'CODE_POSTAL']=='NaN':
            continue
        else:
            for j in (df_location.index):
                if df_location.loc[j,'CODE_POSTAL']==STU.loc[i,'CODE_POSTAL']:
                    STU.loc[i,'VILLE']=df_location.loc[j,'VILLE']
                    break
    
    #updating missing values in REMUNERATION in table STU
    re_df = STU[['REMUNERATION', 'ANNEE', 'ANNEE_SCOLAIRE', 'ENTREPRISE', 'PAYS']]
    le = preprocessing.LabelEncoder()
    cols=['ANNEE','ANNEE_SCOLAIRE', 'ENTREPRISE', 'PAYS']
    for col in cols:
        le.fit(re_df[col])
        re_df[col]=le.transform(re_df[col])
    known_re = re_df[re_df.REMUNERATION.notnull()].values
    unknown_re = re_df[re_df.REMUNERATION.isnull()].values
    # Target remuneration
    y = known_re[:, 0]
    # features
    X = known_re[:, 1:]
    # fit in RandomForestRegressor
    rfr = RandomForestRegressor(random_state=0, n_estimators=2000, n_jobs=-1)
    rfr.fit(X, y)
    # estimiation
    predictedRes = rfr.predict(unknown_re[:, 1:])
    # update
    STU.loc[ (STU.REMUNERATION.isnull()), 'REMUNERATION' ] = predictedRes 
 
 
     #updating missing values in ADR_CP in table ADR by df_location
    df=ADR[ADR['ADR_CP'].isnull().T]
    for i in (df.index):
        if df.loc[i,'ADR_VILLE']=='NaN':
            continue
        else:
            for j in (df_location.index):
                if df_location.loc[j,'VILLE']==ADR.loc[i,'ADR_VILLE']:
                    ADR.loc[i,'ADR_CP']=df_location.loc[j,'CODE_POSTAL']
                    break
                    
    #updating missing values in VILLE in table ADR by df_location
    df=ADR[ADR['ADR_VILLE'].isnull().T]
    for i in (df.index):
        if df.loc[i,'ADR_CP']=='NaN':
            continue
        else:
            for j in (df_location.index):
                if df_location.loc[j,'CODE_POSTAL']==ADR.loc[i,'ADR_CP']:
                    ADR.loc[i,'ADR_VILLE']=df_location.loc[j,'VILLE']
                    break
 
    return ADR,PRG,STU
