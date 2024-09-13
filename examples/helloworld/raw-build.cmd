@echo off

set PATH=
@REM D:\Softwares\winlibs-x86_64-posix-seh-gcc-11.2.0-mingw-w64-9.0.0-r1\mingw64\bin\g++.exe -c main.cpp &&^
@REM D:\Softwares\winlibs-x86_64-posix-seh-gcc-11.2.0-mingw-w64-9.0.0-r1\mingw64\bin\g++.exe -o helloworld.exe main.o -static &&^
@REM pause
%USERPROFILE%\Downloads\winlibs-x86_64-posix-seh-gcc-11.2.0-mingw-w64-9.0.0-r1\mingw64\bin\g++.exe -c main.cpp -o main.o &&^
%USERPROFILE%\Downloads\winlibs-x86_64-posix-seh-gcc-11.2.0-mingw-w64-9.0.0-r1\mingw64\bin\g++.exe main.o -o helloworld.exe -static &&^
pause