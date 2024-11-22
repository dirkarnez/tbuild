from pathlib import Path
import subprocess
from typing import List
import os
import sys
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

class CodeGenerator(IBuilder):
    def build（self) -> str:
        return """#ifndef HEATSHRINK_H
        #define HEATSHRINK_H
        
        #define HEATSHRINK_AUTHOR "Scott Vokes <vokes.s@gmail.com>"
        #define HEATSHRINK_URL "https://github.com/atomicobject/heatshrink"
        
        /* Version 0.4.1 */
        #define HEATSHRINK_VERSION_MAJOR 0
        #define HEATSHRINK_VERSION_MINOR 4
        #define HEATSHRINK_VERSION_PATCH 1
        
        #define HEATSHRINK_MIN_WINDOW_BITS 4
        #define HEATSHRINK_MAX_WINDOW_BITS 15
        
        #define HEATSHRINK_MIN_LOOKAHEAD_BITS 3
        
        #define HEATSHRINK_LITERAL_MARKER 0x01
        #define HEATSHRINK_BACKREF_MARKER 0x00
        
        #endif"""
        
class TBuild(IBuilder):
  build_directory: Path

  def __init__(self, location: Path, compiler_prefix: str, build_directory: Path, installation_directory: Path):
    self.location = location
    self.compiler_prefix = compiler_prefix
    self.build_directory = Path(build_directory)
    self.installation_directory = Path(installation_directory)
    self.tasks = []

  def build_an_object(self, compiler: Path, source_file: Path, output_object_name: str):
    # f"{Path(source_file).stem}.o"
    self.tasks.append(TBuildTask(tool_executable=compiler, commands=["-c", source_file, "-o", str(self.build_directory / output_object_name)], expected_output_files=[self.build_directory / output_object_name]))

  # $(AS) -o startup.o startup.s
  def assemble_an_object(self, compiler: Path, source_file: Path, output_object_name: str):
    # f"{Path(source_file).stem}.o"
    self.tasks.append(TBuildTask(tool_executable=compiler, commands=[source_file, "-o", str(self.build_directory / output_object_name)], expected_output_files=[self.build_directory / output_object_name]))

  # def build_an_executable_from_source_files(self, source_files: String, commands: String) -> bool:
  #   __run_command(__get_gcc())

  def build_an_executable_from_object_files(self, compiler: Path, object_files: List[Path], output_executable_name: str, additional_command: str = ""):
    self.tasks.append(TBuildTask(tool_executable=compiler, commands=[*[str(self.build_directory / object_file) for _, object_file in enumerate(object_files)], "-o", self.build_directory / output_executable_name, *additional_command.split()], expected_output_files=[self.build_directory /output_executable_name] ))

  # $(LD) -T link_script.ld startup.o hello_world.o -o hello_world.elf
  def link_an_executable_from_object_files(self, compiler: Path, linker_script_file: Path, object_files: List[Path], output_executable_name: str, additional_command: str = ""):
    self.tasks.append(TBuildTask(tool_executable=compiler, commands=["-T", str(linker_script_file), *[str(self.build_directory / object_file) for _, object_file in enumerate(object_files)], "-o", output_executable_name, *additional_command.split()], expected_output_files=[self.build_directory / output_executable_name] ))
    # linker script

  def build_a_static_library_from_object_files(self, compiler: Path, output_executable_name: str, object_files: List[Path], additional_command: str = ""):
    self.tasks.append(TBuildTask(tool_executable=compiler, commands=["rcs", self.build_directory / output_executable_name, *[str(self.build_directory / object_file) for _, object_file in enumerate(object_files)], *additional_command.split()], expected_output_files=[self.build_directory / output_executable_name] ))

  # def build_a_shared_library():
  
  # def build_a_static_library():

  def __get_executable_extension_with_dot(self) -> str:
    return ".exe" if sys.platform.startswith('win32') else ""

  def get_linker(self) -> Path:
    return Path(self.location) / f"{self.compiler_prefix}ld{self.__get_executable_extension_with_dot()}"

  def get_assembler(self) -> Path:
    return Path(self.location) / f"{self.compiler_prefix}as{self.__get_executable_extension_with_dot()}"

  def get_ar(self) -> Path:
    return Path(self.location) / f"{self.compiler_prefix}ar{self.__get_executable_extension_with_dot()}"

  def get_gcc(self) -> Path:
    return Path(self.location) / f"{self.compiler_prefix}gcc{self.__get_executable_extension_with_dot()}"

  def get_g_plus_plus(self) -> Path:
    return Path(self.location) / f"{self.compiler_prefix}g++{self.__get_executable_extension_with_dot()}"

  def __run_command(self, commands: List[str]):
    print(f"{' '.join([str(elem) for elem in commands])}\n")
    # myenv = {**os.environ, 'PATH': os.environ['PATH'] + ";" + self.location }
    subprocess.call(commands) #, env=myenv)

  def __is_good_run(self, expected_output_files: List[str]) -> bool:
    for k, file_to_check in enumerate(expected_output_files):
      if not os.path.exists(file_to_check):
        return False
    return True

  def build(self):
    with open('report.txt', 'w') as the_file:
      self.build_directory.mkdir(parents=True, exist_ok=True)
      for i, l in enumerate(self.tasks):
        if not os.path.exists(l.tool_executable):
          report_line=f"\"{l.tool_executable}\" not exists"
          print(report_line)
          the_file.write(report_line)
          exit(1)
        for j, file in enumerate(l.expected_output_files):
          if os.path.exists(file):
            os.remove(file)
            print(f"deleting existing {file}\n")
            the_file.write(f"deleting {file}\n")
          self.__run_command([l.tool_executable, *l.commands])
          good=self.__is_good_run(l.expected_output_files)
          the_file.write(f"\"{' '.join([str(l.tool_executable), *[str(command) for _, command in enumerate(l.commands)]])}\" ran {'perfectly' if good else 'badly'}\n")
          if not good:
            exit(1)
    print("everything is good")


