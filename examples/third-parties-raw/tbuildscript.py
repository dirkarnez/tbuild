from pathlib import Path
import sys
sys.path.append(str(Path(__file__).absolute().parent.parent.parent))
# import tbuild
import sys

# setting path
from tbuild import TBuild

tbuild = TBuild(Path.home() / "Downloads" / "winlibs-x86_64-posix-seh-gcc-11.2.0-mingw-w64-9.0.0-r1" / "mingw64" / "bin", "", "tbuild-build", "tbuild-installation")
# tbuild = TBuild(Path("D:") / "Softwares" / "winlibs-x86_64-posix-seh-gcc-11.2.0-mingw-w64-9.0.0-r1" / "mingw64" / "bin", "")

# https://github.com/AndersKaloer/Ring-Buffer

# {
#   installation location installation\ringbuffer
#   public_includes -I location
#   third_party_static_libraries -L location and .a file name
# }
ringbuffer_library = tbuild.install_an_static_library(
  directory=Path("third-parties/AndersKaloer/Ring-Buffer")
  public_include_directory="installation/third-parties/AndersKaloer/Ring-Buffer/includes"
  public_includes=[
    "ringbuffer.h"
  ],
  objects=[
    tbuild.build_an_object(
      tbuild.get_gcc(), 
      "ringbuffer.c", 
      "ringbuffer.o"
    )
  ],
  static_library_file_directory="installation/third-parties/AndersKaloer/Ring-Buffer/lib"
  static_library_file="ringbuffer.a"
)

tbuild.build_an_object(
  tbuild.get_gcc(), 
  third_party_public_includes_directories=[
    ringbuffer_library.public_include_directory
  ],
  "main.c", 
  "main.o"
)

tbuild.build_an_executable_from_object_files(
  tbuild.get_gcc(), 
  third_party_static_libraries=[
    {
      ringbuffer_library.static_library_lib_file
      ringbuffer_library.static_library_lib_file_directory
    }
  ],
  ["main.o"], 
  "helloworld.exe", 
  "-static"
)

tbuild.build()

print()