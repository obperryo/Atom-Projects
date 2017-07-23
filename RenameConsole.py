import os, sys, getpass, cmd
from colorama import init, Style, Fore
from termcolor import colored, cprint
from msvcrt import getch

init(autoreset=True)

class Console(cmd.Cmd):
    def cd(self, directory):

    def rename(self, filename, rename, directory):

    def rename_files(self, filext, directory):

    def do_find(self, name):
        for root, dirs, files in os.walk('.'):
            if name in files:
                print(os.path.join(root, name))
                return os.path.join(root, name)

if __name__ == '__main__':
    Console().cmdloop()
