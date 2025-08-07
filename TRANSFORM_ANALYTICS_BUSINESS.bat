@echo off
set MYSQL_CMD="C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe"
set USER="root"
set PASSWORD="Jian1234"
set DATABASE="simul"

echo Running TRANSFORM_ANALYTICALBUSINESSTABLE.sql...
%MYSQL_CMD% -u %USER% -p%PASSWORD% %DATABASE% < "C:\Users\labva\OneDrive\Desktop\DE Simulation\TRANSFORM_ANALYTICALBUSINESSTABLE.sql" >> "C:\Program Files\MySQL\MySQL Server 8.0\bin\log.txt" 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Error executing TRANSFORM_ANALYTICALBUSINESSTABLE.sql. Exiting.
    pause
    exit /b
)

echo All SQL scripts executed successfully.
pause

