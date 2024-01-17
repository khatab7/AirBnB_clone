#!/usr/bin/python3
"""Console Program"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex
from models import storage


class HBNBCommand(cmd.Cmd):
    """Program contains the entry point of the command interpreter"""
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "City", "State", "Amenity", "Place",
               "Review"]

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
        """Creates a new instance of BaseModel"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models.classes():
            print("** class doesn't exist **")
        else:
            new_obj = models.classes()[args[0]]()
            storage.save()
            print(new_obj.id)

    def do_show(self, arg):
        """Shows the string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models.classes():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """Destroys an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models.classes():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """Prints all string representations of all instances"""
        args = arg.split()
        if len(args) > 0 and args[0] not in models.classes():
            print("** class doesn't exist **")
        else:
            objects = [
                str(obj) for key, obj in storage.all().items()
                if len(args) == 0 or args[0] == key.split(".")[0]
            ]
            print(objects)

    def do_update(self, arg):
        """Updates an instance"""
        args = arg.split()
        if len(args) < 4:
            print("** arguments missing **")
        else:
            cls_name = args[0]
            if cls_name not in models.classes():
                print("** class doesn't exist **")
            elif args[1] not in storage.all("{}.{}".format(cls_name, args[2])):
                print("** no instance found **")
            else:
                obj = storage.all()["{}.{}".format(cls_name, args[2])]
                attr_name = args[3]
                try:
                    attr_value = cast(args[4], obj.__dict__[attr_name].__class__)
                except (KeyError, AttributeError, ValueError):
                    print("** attribute name or value invalid **")
                else:
                    setattr(obj, attr_name, attr_value)
                    storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
