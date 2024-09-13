from pathlib import Path
import sys
sys.path.append(str(Path(__file__).absolute().parent.parent.parent))
# import tbuild
import sys

# setting path
from tbuild import TBuild

tbuild = TBuild(Path.home() / "Downloads" / "winlibs-x86_64-posix-seh-gcc-11.2.0-mingw-w64-9.0.0-r1" / "mingw64" / "bin", "")
# tbuild = TBuild(Path("D:") / "Softwares" / "winlibs-x86_64-posix-seh-gcc-11.2.0-mingw-w64-9.0.0-r1" / "mingw64" / "bin", "")

tbuild.build_an_object(
  tbuild.get_g_plus_plus(), 
  "main.cpp", 
  "main.o"
)

tbuild.build_an_executable_from_object_files(
  tbuild.get_g_plus_plus(), 
  ["main.o"], 
  "helloworld.exe", 
  "-static"
)

tbuild.build()

print()