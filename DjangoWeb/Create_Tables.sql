-- create table mergedtables2 (
--     id integer primary key autoincrement, 
--     ID_ANO TEXT , PRG TEXT , 
--     ANNEE_SCOLAIRE TEXT , SITE TEXT , ADR_CP INT , 
--     ADR_VILLE TEXT , ADR_PAYS TEXT , ANNEE TEXT , 
--     ENTREPRISE TEXT , CODE_POSTAL INT , VILLE TEXT ,
--     PAYS TEXT , SUJET TEXT , REMUNERATION DECIMAL,
--     idCSV int
-- );

-- ALTER TABLE "PRG_STUDENT_SITE" ADD COLUMN idCSV int;


-- INSERT INTO mergedtables (
--     ID_ANO , PRG , 
--     ANNEE_SCOLAIRE , SITE , ADR_CP  , 
--     ADR_VILLE , ADR_PAYS  , ANNEE , 
--     ENTREPRISE , CODE_POSTAL , VILLE  ,
--     PAYS , SUJET , REMUNERATION, idCSV )

--     SELECT     ID_ANO , PRG , 
--     ANNEE_SCOLAIRE , SITE , ADR_CP  , 
--     ADR_VILLE , ADR_PAYS  , ANNEE , 
--     ENTREPRISE , CODE_POSTAL , VILLE  ,
--     PAYS , SUJET , REMUNERATION, 1
    
--     FROM mergedtables_OLD;

    /* SELECT COUNT(*) FROM mergedtables; */

--     ALTER TABLE mergedtables RENAME TO mergedtables_OLD;

-- create table ADR_STUDENTS (
--     id integer primary key autoincrement, 
--     ADR_CP TEXT,
--     ADR_VILLE TEXT,
--     ADR_PAYS TEXT,
--     ID_ANO TEXT,
--     idCSV int
-- );

-- drop table "adr_students_temp";

-- INSERT INTO "ADR_STUDENTS" (
--     ADR_CP, ADR_VILLE ,
--     ADR_PAYS ,   ID_ANO ,
--     idCSV
-- )
--     SELECT 
--     ADR_CP, ADR_VILLE ,
--     ADR_PAYS ,   ID_ANO ,
--     1
--     FROM "adr_students_temp1";

-- create table STUDENT_INTERNSHIP (
--     id integer primary key autoincrement,
--     ANNEE TEXT,
--     ANNEE_SCOLAIRE TEXT,
--     ENTREPRISE TEXT,
--     CODE_POSTAL TEXT,
--     VILLE TEXT,
--     PAYS TEXT,
--     SUJET TEXT,
--     REMUNERATION TEXT,
--     ID_ANO TEXT,
--     idCSV int
-- );

-- INSERT INTO STUDENT_INTERNSHIP (
--     ANNEE  ,    ANNEE_SCOLAIRE  ,    ENTREPRISE  ,    CODE_POSTAL  ,
--     VILLE  ,    PAYS  ,    SUJET  ,    REMUNERATION  ,    ID_ANO  ,
--         idCSV )
--     SELECT 
--     ANNEE  ,    ANNEE_SCOLAIRE  ,    ENTREPRISE  ,    CODE_POSTAL  ,
--     VILLE  ,    PAYS  ,    SUJET  ,    REMUNERATION  ,    ID_ANO  ,
--     1
--     FROM "student_inter_temp" ;

-- DROP TABLE ADR_LOCATION;

-- CREATE TABLE ADR_LOCATION (
--     id integer primary key autoincrement,
--     CODE_POSTAL TEXT,
--     LAT TEXT,
--     LON TEXT,
--     PAYS TEXT,
--     VILLE TEXT,
--     idCSV int
--   );

-- INSERT INTO
--   "ADR_LOCATION" (CODE_POSTAL, idCSV, LAT, LON, PAYS, VILLE)
-- SELECT CODE_POSTAL, 1, LAT, LON, PAYS, VILLE
--    FROM temp_LOCATION;
  