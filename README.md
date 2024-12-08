tbuild
======
tbuild = Transparent Build. Inspired by [Clecius/CppMagic: A Python 3 script to help build C/C++ projects cross-platform.](https://github.com/Clecius/CppMagic)

### Examples
- [dirkarnez/tbuild-example-helloworld](https://github.com/dirkarnez/tbuild-example-helloworld), WIP
- [dirkarnez/tbuild-example-helloworld-mixed-with-nasm](https://github.com/dirkarnez/tbuild-example-helloworld-mixed-with-nasm), WIP
- [dirkarnez/tbuild-example-baremetal](https://github.com/dirkarnez/tbuild-example-baremetal), WIP
  - [ErikOSProject/ErikBoot: ErikBoot is a UEFI-compatible bootloader for ErikOS.](https://github.com/ErikOSProject/ErikBoot)
  - [ErikOSProject/ErikKernel](https://github.com/ErikOSProject/ErikKernel)
- [dirkarnez/tbuild-example-static-library](https://github.com/dirkarnez/tbuild-example-static-library), WIP
- [codegen](./examples/codegen), WIP
  - [jdah/archimedes: C++20 reflection via code generation](https://github.com/jdah/archimedes)
  - webidl2
  - device tree parsing
- [third-parties-from-git-repo-source-files](./examples/third-parties-from-git-repo), WIP
  - should include patching
- [third-parties-from-prebuilt-static-binaries](./examples/third-parties-from-git-repo), WIP
- [third-parties-from-prebuilt-shared-binaries](./examples/third-parties-from-git-repo), WIP
- [third-parties-from-cmake-through-adapter](./examples/third-parties-from-git-repo), WIP

### Feature
- [ ] define third party inside `tbuildscript.py` without adding anything to its github repo
  - [ ] https://github.com/AndersKaloer/Ring-Buffer
- [ ] no `$ENV`
- [ ] no symlink
- [ ] no more OS shells (*nix, windows, just leverage Python!)
- [ ] support code-generation
      - version number
      - config.h
- [ ] language agnostic (focus on C and C++ at the moment)
- [ ] no need to do pre-build (especially third-parties)
- [ ] file walker to re-build the only objects file you are writing code for
  - [ ] build cache
- [ ] p2p (dask distributed)
  - [ymake/ymake/builder.py at main · evilbinary/ymake · GitHub](https://github.com/evilbinary/ymake/blob/main/ymake/builder.py)
  - [dirkarnez/dask-distributed-playground](https://github.com/dirkarnez/dask-distributed-playground)
- [ ] reporting
- [ ] dev-env-setup-as-code (download tools + set up)
- [ ] additional arguemnt for gcc and linker, for example:
  - `-mcpu=cortex-a72 -mlittle-endian -ffreestanding`
  - force `-std=c++20`
  - [g++ 常用链接参数-CSDN博客](https://blog.csdn.net/yz930618/article/details/94987459)

### Reference
- [SCons/scons: SCons - a software construction tool](https://github.com/SCons/scons)
- [texttheater/produce: Replacement for Make geared towards processing data rather than compiling code](https://github.com/texttheater/produce)
- [casey/just: 🤖 Just a command runner](https://github.com/casey/just)

### GCC
- [c - Running gcc's steps manually, compiling, assembling, linking - Stack Overflow](https://stackoverflow.com/questions/8527743/running-gccs-steps-manually-compiling-assembling-linking)
- [GCC and Make - A Tutorial on how to compile, link and build C/C++ applications](https://www3.ntu.edu.sg/home/ehchua/programming/cpp/gcc_make.html)
- [程序编译、链接相关问题（持续更新中......）_程序编译链接的一些常见疑问-CSDN博客](https://blog.csdn.net/whyaiw/article/details/73658194)
  - > 当对动态库与静态库混合连接的时候，使用-static会导致所有的库都使用静态连接的方式。这时需要作用-Wl的方式：
    - `gcc test.cpp -L. -Wl,-Bstatic -ltestlib  -Wl,-Bdynamic -ltestdll `
  - > 另外还要注意系统的运行库使用动态连接的方式，所以当动态库在静态库前面连接时，必须在命令行最后使用动态连接的命令才能正常连接，如：
    - `gcc test.cpp -L. -Wl,-Bdynamic -ltestdll -Wl,-Bstatic -ltestlib  -Wl,-Bdynamic`
    - > 最后的-Wl,-Bdynamic表示将缺省库链接模式恢复成动态链接。

### TODOs
- [ ] Get subprocess output
  ```python
  try:
    out_bytes = subprocess.check_output(['cmd','arg1','arg2'])
  except subprocess.CalledProcessError as e:
      out_bytes = e.output       # Output generated before error
      code      = e.returncode   # Return code
  ```
- [ ] Builder pattern interface?
- [ ] **Exit code**
- [x] linker script
  - [linker script 簡單教學 | CY's Blog](https://evshary.com/2018/06/02/linker-script-%E7%B0%A1%E5%96%AE%E6%95%99%E5%AD%B8/#%E5%8F%96%E5%BE%97-section-%E7%9A%84%E4%BD%8D%E7%BD%AE)
  - [dirkarnez/cpp-arm64-baremetal-playground](https://github.com/dirkarnez/cpp-arm64-baremetal-playground)
- [ ] build report (list of commands with `is_successful` and `run_on`)
- [ ] distributed
  - [Quickstart — Dask.distributed 2024.8.2 documentation](https://distributed.dask.org/en/stable/quickstart.html)
- [x] CICD
  - testing across example projects
- [ ] CLI argument builder (for QEMU scripts, etc)
- [x] baremetal
- [ ] Shared library `g++ hash.cpp -fPIC -shared -o hash.so`
- [ ] Static library
- [ ] Wraps CMake (also to make the install-less targets usable)
- [ ] Wraps AutoTools
  - [**静态编译OpenSSL并作为CMake第三方库 - 个人文章 - SegmentFault 思否**](https://segmentfault.com/a/1190000016017493)
- [ ] Wraps Bazel
- [ ] Use [Poetry](https://python-poetry.org/)?
