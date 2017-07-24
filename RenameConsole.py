import os, sys, getpass, cmd
from colorama import init, Style, Fore
from termcolor import colored
from msvcrt import getch

class Console(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '^how may i help you? '
        intro = self.do_help(arg=None)

    init(autoreset=True)
    user = getpass.getuser()

    def cd(self, directory):
        chdir(directory)

    def do_rename(self, filename, rename, directory='C:\\Users\\{}\\Downloads\\Rename Files'.format(user)):
        do_find(filename)

    def do_renames(self, filext=None, directory='C:\\Users\\{}\\Downloads\\Rename Files'.format(user)):
        for f in os.listdir():
            print(colored(f,'cyan','on_magenta'))
            f_name, f_ext = os.path.splitext(f)
            full_n = colored(f_name,'cyan')+colored(f_ext,'magenta')
            print( f_full )
            print(colored(f_name,'cyan'))

            new_name = input( Style.BRIGHT + colored('Enter new name: ','cyan' ))

            if new_name.strip():
                if new_name.lower() == 'exit':
                    print('Good Bye')
                    raise SystemExit
                elif new_name.lower() == 'cd':
                    main()
                else:
                    print( f_full )
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

    def do_find(self, name):
        for root, dirs, files in os.walk('.'):
            if name in files:
                print(os.path.join(root, name))
                return os.path.join(root, name)

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    Console().cmdloop()
    console = Console()
