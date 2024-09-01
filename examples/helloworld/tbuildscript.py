from pathlib import Path
from tbuild import TBuild

# tbuild = TBuild(Path.home() / "Downloads" / "winlibs-x86_64-posix-seh-gcc-11.2.0-mingw-w64-9.0.0-r1" / "mingw64" / "bin", "")
tbuild = TBuild(Path("D:") / "Softwares" / "winlibs-x86_64-posix-seh-gcc-11.2.0-mingw-w64-9.0.0-r1" / "mingw64" / "bin", "")

tbuild.build_an_executable_from_object_files(
  tbuild.build_an_object("main.cpp"),
  "helloworld.exe",
  "-static"
)

print()