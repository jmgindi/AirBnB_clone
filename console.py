#!/usr/bin/python3
import cmd
import sys

"""
module contains 1 class:
    HBNBCommand
"""



class HBNBCommand(cmd.Cmd):
    """ HBNBCommand is a simple command line
    interpreter for the HBNB project
    
    Attributes:
    intro - 
    prompt - 
    file - 
    """
    prompt = "(hbnb) "
    file = None        


    def do_quit(self, arg):
        """ quits the program
        """
        self.close()
        return True

    def do_EOF(self, arg):
        """ also exits the program
        """
        self.close()
        return True

    def close(self):
        if self.file:
            self.file.close()
            self.file = None


if __name__ == "__main__":
    HBNBCommand().cmdloop()
