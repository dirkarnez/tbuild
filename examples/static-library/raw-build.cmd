@echo off

set PREFIX=D:\Softwares
@REM set PREFIX=%USERPROFILE%\Downloads

%PREFIX%\winlibs-x86_64-posix-seh-gcc-11.2.0-mingw-w64-9.0.0-r1\mingw64\bin\g++.exe -c sum.c -o sum.o &&^
%PREFIX%\winlibs-x86_64-posix-seh-gcc-11.2.0-mingw-w64-9.0.0-r1\mingw64\bin\ar.exe rcs libsum.a sum.o &&^
pause