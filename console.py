#!/usr/bin/python3
import cmd
import sys
from models.base_model import BaseModel


"""
module contains 1 class:
    HBNBCommand
"""



class HBNBCommand(cmd.Cmd):
    """HBNBCommand is a simple command line
    interpreter for the HBNB project
    
    Attributes:
    intro - 
    prompt - 
    file - 
    """
    prompt = "(hbnb) "
    file = None        


    def do_quit(self, arg):
        """quits the program
        """
        self.close()
        return True

    def do_EOF(self, arg):
        """also exits the program
        """
        self.close()
        return True

    def close(self):
        """closes files before termination
        """
        if self.file:
            self.file.close()
            self.file = None

    def do_create(self, *args):
        """creates a new instance of a model
        and adds it to the json file
        """
        if !args:
            print("** class name missing **")
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
        obj = BaseModel()
        return obj

    def do_show(self, *args):
        if !args:
            print("** class name missing **")
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
        if !args[1]:
            print("** instance id missing **")
        if args[1] not in [a thing]:
            print("** no instance found **")

    def do_destroy(self, *args):
        if !args:
            print("** class name missing **")
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
        if !args[1]:
            print("** instance id missing **")
        if args[1] not in [a thing]:
            print("** no instance found **")

    def do_all(self, *args):
        allowed = ["BaseModel", "FileStorage"]
        if args[0] not in allowed:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
