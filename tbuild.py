from pathlib import Path
import subprocess
from typing import List
import os
from dataclasses import dataclass
from abc import ABC, abstractmethod


class IBuilder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    @property
    @abstractmethod
    def build(self) -> None:
        pass



@dataclass
class TBuildTask:
    tool_executable: str
    commands: List[str]
    expected_output_files: List[str]

# from abc import ABC, abstractmethod

# class AccountingSystem(ABC):

#     @abstractmethod
#     def create_purchase_invoice(self, purchase):
#         pass

#     @abstractmethod
#     def create_sale_invoice(self, sale):
#         log.debug('Creating sale invoice', sale)

# class GizmoAccountingSystem(AccountingSystem):

#     def create_purchase_invoice(self, purchase):
#         submit_to_gizmo_purchase_service(purchase)

#     def create_sale_invoice(self, sale):
#         super().create_sale_invoice(sale)
#         submit_to_gizmo_sale_service(sale)

class TBuild(IBuilder):
  def __init__(self, location: Path, compiler_prefix: str):
    self.location = location
    self.compiler_prefix = compiler_prefix
    self.tasks = []

  def build_an_object(self, compiler: Path, source_file: Path, output_object_name: str):
    # f"{Path(source_file).stem}.o"
    self.tasks.append(TBuildTask(tool_executable=compiler, commands=["-c", source_file, "-o", output_object_name], expected_output_files=[output_object_name]))

  # $(AS) -o startup.o startup.s
  def assemble_an_object(self, compiler: Path, source_file: Path, output_object_name: str):
    # f"{Path(source_file).stem}.o"
    self.tasks.append(TBuildTask(tool_executable=compiler, commands=["-o", output_object_name, source_file], expected_output_files=[output_object_name]))

  # def build_an_executable_from_source_files(self, source_files: String, commands: String) -> bool:
  #   __run_command(__get_gcc())

  def build_an_executable_from_object_files(self, compiler: Path, object_files: List[Path], output_executable_name: str, additional_command: str = ""):
    self.tasks.append(TBuildTask(tool_executable=compiler, commands=[*[str(object_file) for i, object_file in enumerate(object_files)], "-o", output_executable_name, *additional_command.split()], expected_output_files=[output_executable_name] ))

  # $(LD) -T link_script.ld startup.o hello_world.o -o hello_world.elf
  def link_an_executable_from_object_files(self, compiler: Path, linker_script_file: Path, object_files: List[Path], output_executable_name: str, additional_command: str = ""):
    self.tasks.append(TBuildTask(tool_executable=compiler, commands=["-T", str(linker_script_file), *[str(object_file) for i, object_file in enumerate(object_files)], "-o", output_executable_name, *additional_command.split()], expected_output_files=[output_executable_name] ))
    # linker script

  # def build_a_shared_library():
  
  # def build_a_static_library():

  def get_linker(self) -> Path:
    return Path(self.location) / f"{self.compiler_prefix}ld"

  def get_assembler(self) -> Path:
    return Path(self.location) / f"{self.compiler_prefix}as"

  def get_gcc(self) -> Path:
    return Path(self.location) / f"{self.compiler_prefix}gcc"

  def get_g_plus_plus(self) -> Path:
    return Path(self.location) / f"{self.compiler_prefix}g++"

  def __run_command(self, commands: List[str]):
    print(' '.join([str(elem) for elem in commands]))
    # myenv = {**os.environ, 'PATH': os.environ['PATH'] + ";" + self.location }
    subprocess.call(commands) #, env=myenv)

  def __is_good_run(self, expected_output_files: List[str]) -> bool:
    for k, file_to_check in enumerate(expected_output_files):
      if not os.path.exists(file_to_check):
        return False
    return True

  def build(self):
    with open('report.txt', 'w') as the_file:
      for i, l in enumerate(self.tasks):
        # if not os.path.exists(l.tool_executable):
        #   print(f"{l.tool_executable} not exists")
        #   exit(1)
        for j, file in enumerate(l.expected_output_files):
          if os.path.exists(file):
            os.remove(file)
          else:
            self.__run_command([l.tool_executable, *l.commands])
            good=self.__is_good_run(l.expected_output_files)
            the_file.write(f"{' '.join([str(l.tool_executable), *l.commands])} ran {'perfectly' if good else 'badly'}\n")
            if not good:
              exit(1)
    print("everything is good")
