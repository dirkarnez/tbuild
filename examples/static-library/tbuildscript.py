from pathlib import Path
import sys
sys.path.append(str(Path(__file__).absolute().parent.parent.parent))
# import tbuild
import sys

# setting path
from tbuild import TBuild

tbuild = TBuild(Path.home() / "Downloads" / "winlibs-x86_64-posix-seh-gcc-11.2.0-mingw-w64-9.0.0-r1" / "mingw64" / "bin", "", "build", "installation")
# tbuild = TBuild(Path("D:") / "Softwares" / "winlibs-x86_64-posix-seh-gcc-11.2.0-mingw-w64-9.0.0-r1" / "mingw64" / "bin", "")

tbuild.build_an_object(
  tbuild.get_gcc(), 
  "sum.c", 
  "sum.o"
)

tbuild.build_a_static_library_from_object_files(
  tbuild.get_ar(), 
  "libsum.a",
  ["sum.o"]
)

tbuild.build()

print()