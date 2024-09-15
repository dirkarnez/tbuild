@REM run as Administrator
@echo off

set SEVENZIP=C:\"Program Files"\7-Zip\7z.exe
set PYTHON_DIR=%USERPROFILE%\Downloads\python-3.10.8-amd64-portable
set PYTHON_EXE=%PYTHON_DIR%\python.exe

if not exist %PYTHON_EXE% (
cd /d "%TEMP%" &&^
%SystemRoot%\System32\curl.exe "https://github.com/dirkarnez/python-portable/releases/download/v3.10.8/python-3.10.8-amd64-portable.zip" -L -O  &&^
%SEVENZIP% x python-3.10.8-amd64-portable.zip -o"%PYTHON_DIR%"  &&^
del python-3.10.8-amd64-portable.zip
)

if exist %PYTHON_EXE% (
    echo python %PYTHON_EXE% found
)
