import sys
from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY'] = "C:\\Users\\Teodor\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\Teodor\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tk8.6"

Packages = []

build_exe_options = {"includes": ["tkinter"], "packages": ["numpy"], "include_files": ["C:\\Users\\Teodor\\AppData\\Local\\Programs\\Python\\Python36-32\\DLLs\\tcl86t.dll", "C:\\Users\\Teodor\\AppData\\Local\\Programs\\Python\\Python36-32\\DLLs\\tk86t.dll"]}

exe = Executable(
   script="app.py",
   base="Win32GUI",
   targetName="Test.exe"
   )

setup(
    name = "Schedule",
    version = "0.1",
    description = "A weekly schedule",
    options = {"build_exe": build_exe_options},
    executables = [exe])
