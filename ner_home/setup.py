import sys
from cx_Freeze import setup, Executable
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtWidgets
import re
global arq_csv
from PyQt5 import QtCore, QtGui, QtWidgets


base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("app.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = ["PyQt5"],
        include_files = [],
        excludes = []
)




setup(
    name = "NER",
    version = "1.0",
    description = "Descrição do programa",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
