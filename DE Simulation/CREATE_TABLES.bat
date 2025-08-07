@echo off
set MYSQL_CMD="C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe"
set USER="root"
set PASSWORD="Jian1234"
set DATABASE="simul"

echo Running CREATE_TABLES.sql...
%MYSQL_CMD% -u %USER% -p%PASSWORD% %DATABASE% < "C:\Program Files\MySQL\MySQL Server 8.0\bin\CREATE_TABLES.sql" >> "C:\Program Files\MySQL\MySQL Server 8.0\bin\log.txt" 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Error executing CREATE_TABLES.sql. Exiting.
    pause
    exit /b
)

echo All SQL scripts executed successfully.
pause


