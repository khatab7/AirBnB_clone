#!/usr/bin/python3
"""Console Program"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Program contains the entry point of the command interpreter"""
    prompt = "(hbnb) "

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
