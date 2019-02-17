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
    prompt - 
    file - 
    """
    prompt = "(hbnb) "
    file = None        
    allowed = ["BaseModel", "User"]


    def do_quit(self, arg):
        """quits the program
        """
        self.close()
        return True

    def do_EOF(self, arg):
        """also exits the program
        """
        print()
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
        if not args:
            print("** class name missing **")
        if args[0] not in self.__allowed:
            print("** class doesn't exist **")
        obj = BaseModel()
        return obj

    def do_show(self, *args):
        """prints the string representation of a model
        """
        if not args:
            print("** class name missing **")
        if args[0] not in self.__allowed:
            print("** class doesn't exist **")
        if not args[1]:
            print("** instance id missing **")
        if args[1] not in storage.__objects.keys():
            print("** no instance found **")
        else:
            print(storage.__objects[(args[0] + "." + args[1])])

    def do_destroy(self, *args):
        """deletes an instance of a model
        """
        if not args:
            print("** class name missing **")
        if args[0] not in self.__allowed:
            print("** class doesn't exist **")
        if not args[1]:
            print("** instance id missing **")
        if args[1] not in storage.__objects.keys():
            print("** no instance found **")

    def do_all(self, *args):
        """prints all objects of a certain type
        """
        if args[0] not in self.__allowed:
            print("** class doesn't exist **")
        else:
            print([obj for obj in storage.__objects if 
                   args[0] in obj.id])

    def do_update(self, *args):
        """updates the value of an attribute for a
        given object
        """
        if not args:
            print("** class name missing **")
        if args[0] not in self.__allowed:
            print("** class doesn't exist **")
        if not args[1]:
            print("** instance id missing **")

        obj_id = args[0] + "." + args[1]

        if obj_id not in storage.__objects.keys():
            print("** no instance found **")
        if not args[2]:
            print("** attribute name missing **")
        if not args[3]:
            print("** value missing **")
        else:
            storage.__objects[obj_id].update(args[2], args[3])

if __name__ == "__main__":
    HBNBCommand().cmdloop()
