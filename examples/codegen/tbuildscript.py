from pathlib import Path
import sys
sys.path.append(str(Path(__file__).absolute().parent.parent.parent))
# import tbuild
import sys

# setting path
from tbuild import TBuild

tbuild = TBuild(Path.home() / "Downloads" / "arm-gnu-toolchain-12.2.rel1-mingw-w64-i686-aarch64-none-elf" / "arm-gnu-toolchain-12.2.rel1-mingw-w64-i686-aarch64-none-elf" / "bin", "aarch64-none-elf-", "build", "installation")
# tbuild = TBuild(Path("D:") / "Softwares" / "winlibs-x86_64-posix-seh-gcc-11.2.0-mingw-w64-9.0.0-r1" / "mingw64" / "bin", "", "build", "installation")


# TODO calling code-gen in .tbuild/generate-array.py
