#!/usr/bin/python3
"""Console Program"""
import cmd
from models.base_model import BaseModel
import shlex

class HBNBCommand(cmd.Cmd):
    """Program contains the entry point of the command interpreter"""
    prompt = "(hbnb) "
    valid_classes = ["BaseModel"]

    def do_EOF(self, line):
        "Quit command to exit the program"
        print()
        return True

    def do_quit(self, line):
        "Quit command to exit the program"
        return True

    def emptyline(self):
        """Called when an empty line is entered. Do nothing."""
        pass

    def do_create(self, arg):
        """
        Create a new instance of BaseModel and save it to the JSON file.
        Usage: create <class_name>
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
