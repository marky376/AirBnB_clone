#!/usr/bin/python3

import cmd
from datetime import datetime

class HBNBConsole(cmd.Cmd):
    prompt = '(hbnb) '

    def do_EOF(self, line):
        return True
    def do_help(self, line):
        return True
    def do_quit(self, line):
        return True
    def emptyline(self):
        pass
    

if __name__ == '__main__':
    HBNBCONSOLE().cmdloop()