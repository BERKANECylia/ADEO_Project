create table mergedtables2 (
    id integer primary key autoincrement, 
    ID_ANO TEXT , PRG TEXT , 
    ANNEE_SCOLAIRE TEXT , SITE TEXT , ADR_CP INT , 
    ADR_VILLE TEXT , ADR_PAYS TEXT , ANNEE TEXT , 
    ENTREPRISE TEXT , CODE_POSTAL INT , VILLE TEXT ,
    PAYS TEXT , SUJET TEXT , REMUNERATION DECIMAL,
    idCSV int
);

INSERT INTO mergedtables2 (
    ID_ANO , PRG , 
    ANNEE_SCOLAIRE , SITE , ADR_CP  , 
    ADR_VILLE , ADR_PAYS  , ANNEE , 
    ENTREPRISE , CODE_POSTAL , VILLE  ,
    PAYS , SUJET , REMUNERATION )
    SELECT     ID_ANO , PRG , 
    ANNEE_SCOLAIRE , SITE , ADR_CP  , 
    ADR_VILLE , ADR_PAYS  , ANNEE , 
    ENTREPRISE , CODE_POSTAL , VILLE  ,
    PAYS , SUJET , REMUNERATION
    
    FROM mergedtables;

    SELECT COUNT(*) FROM mergedtables2;

    ALTER TABLE mergedtables RENAME TO mergedtables_OLD;