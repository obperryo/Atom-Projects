import os, sys, getpass, cmd
from colorama import init, Style, Fore
from termcolor import colored
from msvcrt import getch

user = os.path.expanduser('~' + getpass.getuser())
init(autoreset=True)

class Console(cmd.Cmd):


    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '^how may I help you? '
        self.intro = self.do_help(arg=None)
        os.chdir('C:\\')

    def do_cd(self, arg='.'):
        try:
            os.chdir(arg)
        except:
            print(arg + ' is not a path')
        self.prompt = os.getcwd() + ' '

    def do_rename(self, args):
        if len(args.split()) == 3:
            filename, rename, directory = args.split()
        elif len(args.split()) == 2:
            filename, rename = args.split()
            directory = user + '\\Downloads'

        try:
            os.chdir(directory)
        except:
            print(directory + ' is not a path')

        self.do_find(filename)

    def do_renames(self):
        filext
        user = os.path.expanduser('~' + getpass.getuser())
        directory = user + '\\Downloads\\Rename Files'
        try:
            os.chdir(directory)
        except:
            print(directory + ' is not a path')

        for f in os.listdir():
            print(colored(f,'cyan','on_magenta'))
            f_name, f_ext = os.path.splitext(f)
            full_n = colored(f_name,'cyan')+colored(f_ext,'magenta')
            print( full_n )
            print(colored(f_name,'cyan'))

            new_name = input( Style.BRIGHT + colored('Enter new name: ','cyan' ))

            if new_name.strip():
                if new_name.lower() == 'cancel':
                    self.prompt = 'What now? '
                    break
                elif 'cd' in new_name.lower():
                    command, path = new_name.split()
                    self.do_cd(directory = path or '.')
                    self.do_renames(filext=None, directory='.')
                    break
                else:
                    print( full_n )
                    print('{}{}'.format(Style.BRIGHT + colored(new_name.strip(),'cyan' ), colored(f_ext.strip(),'magenta')))
                    rename = '{}{}'.format(new_name.strip(), f_ext.strip())

                    while True:
                        print('Press Enter to rename or Escape to exit...')
                        key = ord(getch())
                        if key == 27:
                            print('Good Bye')
                            raise SystemExit
                        elif key ==13:
                            break
                    os.rename(f, rename)
                    print('Rename Complete')
            else:
                print(Style.BRIGHT + 'Next file is')

    def do_find(self, args):
        if len(args.split()) == 2:
            name, directory = args.split(' ')
        elif len(args.split()) == 1:
            name = args
            directory = '.'

        for root, dirs, files in os.walk(directory):
            if name in files:
                os.chdir(os.path.dirname(os.path.join(root, name)))
                self.prompt = os.getcwd() + ' '

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    Console().cmdloop()
