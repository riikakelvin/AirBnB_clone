#!/usr/bin/python3

"""
The module contains the entry point of the command interpreter.
"""

import cmd
import re

from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse_args(arg):
    """
    Tokenizes the command argument into a list of individual
    components

    Args:
        arg (str): The command argument.

    Returns:
        list: The parsed arguments.

    Examples:
        >>> parse_args("BaseModel 1234-1234-1234")
        ['BaseModel', '1234-1234-1234']
    """
    curly_braces_match = re.search(r"\{(.*?)\}", arg)
    bracket_match = re.search(r"\[(.*?)\]", arg)

    if curly_braces_match is None:
        if bracket_match is None:
            return [component.strip(",") for component in split(arg)]
        else:
            tokenizer = split(arg[:brackets_match.span()[0]])
            tokenized = [component.strip(",") for component in tokenizer]
            tokenized.append(brackets_match.group())
            return tokenized
    else:
        tokenizer = split(arg[:curly_braces_match.span()[0]])
        tokenized = [component.strip(",") for component in tokenizer]
        tokenized.append(curly_braces_match.group())
        return tokenized


class HBNBCommand(cmd.Cmd):
    """
    Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
        available_classes (set): Set of available classes.
    """

    prompt = "(hbnb) "

    available_classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """
        Do nothing upon receiving an empty line.
        """
        pass

    def default(self, arg):
        """
        Default behavior for cmd module when input is invalid.

        Args:
            argument (str): The command argument.

        Returns:
            bool: False if the syntax is unknown,
            otherwise the result of the executed command.
        """
        command_mappings = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }

        match = re.search(r"\.", arg)
        if match:
            split_args = arg[:match.start()], arg[match.end():]
            match = re.search(r"\((.*?)\)", split_args[1])
            if match:
                command = split_args[1][:match.start()], match.group()[1:-1]
                if command[0] in command_mappings:
                    command_call = "{} {}".format(split_args[0], command[1])
                    return command_mappings[command[0]](command_call)

        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF signal to exit the program.
        """
        print("")
        return True

    def do_create(self, arg):
        """
        Usage: create <class>
        Create a new instance of a class and print its id.
        """
        args = parse_args(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in self.available_classes:
            print("** class doesn't exist **")
        else:
            instance = eval(args[0])()
            print(instance.id)
            storage.save()

    def do_show(self, arg):
        """
        Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance given its id.
        """
        args = parse_args(arg)
        obj_dict = storage.all()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.available_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """
        Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance given its id.
        """
        args = parse_args(arg)
        obj_dict = storage.all()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.available_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict:
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        """
        Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.

        If no class is specified, displays all instantiated objects.
        """
        class_name = parse_args(arg)
        if len(class_name) > 0 and class_name[0] not in HBNBCommand.available_classes:
            print("** class doesn't exist **")
        else:
            object_list = [
                obj.__str__() for obj in storage.all().values()
                if len(class_name) == 0 or obj.__class__.__name__ == class_name[0]
            ]
            print(object_list)

    def do_count(self, arg):
        """
        Usage: count <class> or <class>.count()

        Retrieve the number of instances of a given class.
        """
        args = parse_args(arg)
        count = 0
        class_name = args[0] if args else None
        if class_name:
            for obj in storage.all().values():
                if obj.__class__.__name__ == class_name:
                    count += 1
        else:
            count = len(storage.all())
        print(count)

    def do_update(self, arg):
        """
        Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)

        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary.
        """
        args = parse_args(arg)
        obj_dict = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in self.available_classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if f"{args[0]}.{args[1]}" not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(args) == 4:
            obj = obj_dict[f"{args[0]}.{args[1]}"]
            if args[2] in obj.__class__.__dict__.keys():
                value_type = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = value_type(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = obj_dict[f"{args[0]}.{args[1]}"]
            for key, value in eval(args[2]).items():
                if key in obj.__class__.__dict__.keys() and type(
                        obj.__class__.__dict__[key]
                ) in {str, int, float}:
                    value_type = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = value_type(value)
                else:
                    obj.__dict__[key] = value
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
