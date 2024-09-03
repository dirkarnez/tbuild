from pathlib import Path
import subprocess
from typing import List
import os

from abc import ABC, abstractmethod

class AccountingSystem(ABC):

    @abstractmethod
    def create_purchase_invoice(self, purchase):
        pass

    @abstractmethod
    def create_sale_invoice(self, sale):
        log.debug('Creating sale invoice', sale)

class GizmoAccountingSystem(AccountingSystem):

    def create_purchase_invoice(self, purchase):
        submit_to_gizmo_purchase_service(purchase)

    def create_sale_invoice(self, sale):
        super().create_sale_invoice(sale)
        submit_to_gizmo_sale_service(sale)
      
class TBuild:
  def __init__(self, location: Path, compiler_prefix: str):
    self.location = location
    self.compiler_prefix = compiler_prefix
    
  def build_an_object(self, compiler: Path, source_file: Path) -> str:
    self.__run_command([self.__get_g_plus_plus(), "-c", source_file])
    return f"{Path(source_file).stem}.o"

  # def build_an_executable_from_source_files(self, source_files: String, commands: String) -> bool:
  #   __run_command(__get_gcc())

  def build_an_executable_from_object_files(self, compiler: Path, object_files: Path, executable_name: str, additional_command: str):
    self.__run_command([self.__get_g_plus_plus(), "-o", executable_name, object_files, *additional_command.split()])

  # def build_a_shared_library():
  
  # def build_a_static_library():

  def get_g_plus_plus(self) -> Path:
    return Path(self.location) / f"{self.compiler_prefix}g++"

  def __run_command(self, command: List[str]):
    # myenv = {**os.environ, 'PATH': os.environ['PATH'] + ";" + self.location }
    subprocess.call(command) #, env=myenv)
    



# tbuild = TBuild("aarch64-none-elf-")
# tbuild.


# g++ -c file1.cpp -o file1.o
# g++ -c file2.cpp -o file2.o
# g++ -c file3.cpp -o file3.o
# g++ -o MyProgram.exe file1.o file2.o file3.o

# gcc -c 
# gcc -o hello hello.o


# https://github.com/dirkarnez/qemu-cortex-a7-baremetal/blob/main/Makefile
# hello_world.elf: link_script.ld startup.o hello_world.o
# 	# Link the two object files to an elf file
# 	$(LD) -T link_script.ld startup.o hello_world.o -o hello_world.elf

# startup.o: startup.s
# 	$(AS) -o startup.o startup.s

# hello_world.o: hello_world.c
# 	$(CC) -c -o hello_world.o hello_world.c

# clean:
# 	rm -f hello_world.o startup.o hello_world.elf

