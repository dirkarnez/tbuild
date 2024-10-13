tbuild
======
Transparent Build. Inspired by [Clecius/CppMagic: A Python 3 script to help build C/C++ projects cross-platform.](https://github.com/Clecius/CppMagic)

### Examples
- [dirkarnez/tbuild-example-helloworld](https://github.com/dirkarnez/tbuild-example-helloworld)
- [dirkarnez/tbuild-example-baremetal](https://github.com/dirkarnez/tbuild-example-baremetal)

### Feature
- [ ] no ENV
- [ ] no need to do pre-build
- [ ] file walker to re-build the only objects file you are writing code for
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

### TODOs
- [ ] Builder pattern interface?
- [ ] **Exit code**
- [x] linker script
  - [linker script 簡單教學 | CY's Blog](https://evshary.com/2018/06/02/linker-script-%E7%B0%A1%E5%96%AE%E6%95%99%E5%AD%B8/#%E5%8F%96%E5%BE%97-section-%E7%9A%84%E4%BD%8D%E7%BD%AE)
  - [dirkarnez/cpp-arm64-baremetal-playground](https://github.com/dirkarnez/cpp-arm64-baremetal-playground)
- [ ] build report (list of commands with `is_successful` and `run_on`)
- [ ] distributed
  - [Quickstart — Dask.distributed 2024.8.2 documentation](https://distributed.dask.org/en/stable/quickstart.html)
- [ ] CICD
  - testing across example projects
- [ ] CLI argument builder (for QEMU scripts, etc)
- [x] baremetal
- [ ] Shared library `g++ hash.cpp -fPIC -shared -o hash.so`
- [ ] Static library
