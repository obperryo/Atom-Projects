import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os", "sys", "getpass", "colorama", "termcolor", "msvcrt"]}

base = None
if sys.platform == "Win32":
            # base = "Win32GUI"
            pass

setup(      name = "RenameMachine",
                            version = "0.1",
                            description = "I can rename with the best of them",
                            options = {"build_exe": build_exe_options},
                            executables = [Executable("Rename.py", base=base)])
                            #use F6 "python setup.py bdist_msi"
