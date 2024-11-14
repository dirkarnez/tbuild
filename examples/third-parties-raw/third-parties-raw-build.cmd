@echo off

@REM set PREFIX=D:\Softwares
set PREFIX=%USERPROFILE%\Downloads

if not exist build mkdir build
if not exist %~dp0build\ringbuffer mkdir %~dp0build\ringbuffer

cd .\third-parties\Ring-Buffer &&^
%PREFIX%\winlibs-x86_64-posix-seh-gcc-11.2.0-mingw-w64-9.0.0-r1\mingw64\bin\g++.exe -c ringbuffer.c -o %~dp0build\ringbuffer\ringbuffer.o &&^
%PREFIX%\winlibs-x86_64-posix-seh-gcc-11.2.0-mingw-w64-9.0.0-r1\mingw64\bin\ar.exe rcs %~dp0build\ringbuffer\ringbuffer.a %~dp0build\ringbuffer\ringbuffer.o &&^
pause