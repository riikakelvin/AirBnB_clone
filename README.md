# AirBnB Clone - The Console

## Project Description

The AirBnB Clone Console is the first step towards building a full web application: the AirBnB clone. This initial stage is crucial as it forms the foundation for subsequent projects, such as HTML/CSS templating, database storage, API development, and front-end integration.

Each task in the project is interlinked and contributes to the following objectives:

* Implement a parent class, BaseModel, responsible for handling the initialization, serialization, and deserialization of future instances.
* Establish a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> File.
* Create classes for AirBnB components (e.g., User, State, City, Place) that inherit from BaseModel.
* Develop the first abstracted storage engine of the project: File storage.
* Design and execute comprehensive unit tests to validate all classes and storage engine implementations.


## Command Interpreter Description
The AirBnB Clone Command Interpreter closely resembles the functionality of a typical shell but is tailored to suit our specific project requirements. It enables us to manage the objects within our project effectively. The command interpreter provides the following capabilities:

* Creation of new objects (e.g., User, Place) with specified attributes.
* Retrieval of objects from files, databases, and other sources.
* Performing operations on objects, such as counting and computing statistics.
* Updating attributes of existing objects.
* Removing objects from the system.

## Usage

### Interactive Mode

To launch the AirBnB Clone Console in interactive mode, execute the following command:

```
$ ./console.py
```

Once inside the console, you can enter commands and interact with the system. Use the `help` command to access a list of available commands and their descriptions.

Example:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

### Non-interactive Mode

The AirBnB Clone Console can also be used in non-interactive mode, similar to a shell script. You can provide commands through standard input or by executing scripts.

Example:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

### Commands currently available:

| Command | Syntax |
| ------- | ------- |
| Run the console | `./console.py` |
| Quit the console | `(hbnb) quit` |
| Display help for a command | `(hbnb) help <command>` |
| Create an object (prints its ID) | `(hbnb) create <class>` |
| Show an object | `(hbnb) show <class> <id>` or `(hbnb) <class>.show(<id>)` |
| Destroy an object | `(hbnb) destroy <class> <id>` or `(hbnb) <class>.destroy(<id>)` |
| Show all objects or instances of a class | `(hbnb) all` or `(hbnb) all <class>` |
| Update an attribute of an object | `(hbnb) update <class> <id> <attribute name> "<attribute value>"` or `(hbnb) <class>.update(<id>, <attribute name>, "<attribute value>")` |

This table format presents the commands in a clear and organized manner, making it easy for users to understand and reference the available functionality of the AirBnB Clone Console.


## Models

The `models` folder contains all the classes used in this project.

| File         | Description                               | Attributes                                                                                             |
| ------------ | ----------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| base_model.py | BaseModel class for all other classes     | id, created_at, updated_at                                                                             |
| user.py      | User class for storing user information    | email, password, first_name, last_name                                                                 |
| amenity.py   | Amenity class for storing amenity information | name                                                                                                   |
| city.py      | City class for storing location information | state_id, name                                                                                         |
| state.py     | State class for storing location information | name                                                                                                   |
| place.py     | Place class for storing accommodation information | city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids |
| review.py    | Review class for storing user/host review information | place_id, user_id, text                                                                           |

## File Storage
The **`engine`** folder manages the serialization and deserialization of data using the JSON format.

The **`file_storage.py`** file defines a FileStorage class with methods that follow the following flow: **`<object> -> to_dict() -> <dictionary> -> JSON dump -> <json string> -> FILE -> <json string> -> JSON load -> <dictionary> -> <object>`**

The **`__init__.py`** file instantiates the FileStorage class as **`storage`** and calls the **`reload()`** method on that instance. This automatically reloads the serialized data during initialization.

## Tests
All code is thoroughly tested using the unittest module. The tests for the classes are located in the test_models folder.

## Authors
* Emeka Emodi - emodiemeka@gmail.com
* Etomchukwu Oguejiofor - etoogueji@gmail.com
