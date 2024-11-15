tbuild
======
tbuild = Transparent Build. Inspired by [Clecius/CppMagic: A Python 3 script to help build C/C++ projects cross-platform.](https://github.com/Clecius/CppMagic)

### Examples
- [dirkarnez/tbuild-example-helloworld](https://github.com/dirkarnez/tbuild-example-helloworld), WIP
- [dirkarnez/tbuild-example-baremetal](https://github.com/dirkarnez/tbuild-example-baremetal), WIP
- [dirkarnez/tbuild-example-static-library](https://github.com/dirkarnez/tbuild-example-static-library), WIP
- [codegen](./examples/codegen), WIP
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

### GCC
- [c - Running gcc's steps manually, compiling, assembling, linking - Stack Overflow](https://stackoverflow.com/questions/8527743/running-gccs-steps-manually-compiling-assembling-linking)
- [GCC and Make - A Tutorial on how to compile, link and build C/C++ applications](https://www3.ntu.edu.sg/home/ehchua/programming/cpp/gcc_make.html)

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
- [ ] Wraps Bazel
