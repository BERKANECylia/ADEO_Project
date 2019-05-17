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
 /* ALTER TABLE mergedtables ADD COLUMN idCSVDescript TEXT; */

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
--     2
--     FROM "temp_ADR1";

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
    -- ANNEE  ,    ANNEE_SCOLAIRE  ,    ENTREPRISE  ,    CODE_POSTAL  ,
    -- VILLE  ,    PAYS  ,    SUJET  ,    REMUNERATION  ,    ID_ANO  ,
    --     idCSV )
    -- SELECT 
    -- ANNEE  ,    ANNEE_SCOLAIRE  ,    ENTREPRISE  ,    CODE_POSTAL  ,
    -- VILLE  ,    PAYS  ,    SUJET  ,    REMUNERATION  ,    ID_ANO  ,
    -- 1
    -- FROM "temp_STU1" ;

-- INSERT INTO
--   "PRG_STUDENT_SITE" (ANNE_SCOLAIRE, ID_ANO, idCSV, PRG, SITE)
--     SELECT
--         ANNEE_SCOLAIRE, ID_ANO, 2, PRG, SITE
--     FROM "temp_PRG1";


-- INSERT INTO
--   "PRG_STUDENT_SITE" (ANNE_SCOLAIRE, id, ID_ANO, idCSV, PRG, SITE)
-- VALUES
--   (
--     'ANNE_SCOLAIRE:TEXT',
--     id:INT,
--     ID_ANO:INT,
--     idCSV:int,
--     'PRG:TEXT',
--     'SITE:TEXT'
--   );


select a.*, b.*
    from PRG_STUDENT_SITE a
      join ADR_STUDENTS b on a.ID_ANO=b.ID_ANO
;


-- select count(*) from STUDENT_INTERNSHIP;

