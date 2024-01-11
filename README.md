# 0x00. AirBnB Clone - The Console
![image](https://github.com/MaazAlside/AirBnB_clone/assets/53683957/609132c9-889a-4f3e-ab4c-565c2fec65a7)

## Project Overview

This is a group project to build the first step towards creating an AirBnB clone. The primary objective is to develop a command-line interpreter (CLI) to manage AirBnB objects. The project is to be completed in teams of 2 people, with a start date on Jan 8, 2024, at 6:00 AM, and a deadline for completion by Jan 15, 2024, at 6:00 AM. The checker will be released on Jan 13, 2024, at 12:00 PM.

## Concepts

The project focuses on the following concepts:

- Python packages
- AirBnB clone

## Background Context

Welcome to the AirBnB clone project! Before starting, please read the AirBnB concept page. The initial step involves writing a command interpreter to manage AirBnB objects. This is crucial for building the foundation of the AirBnB clone and will be used in subsequent projects such as HTML/CSS templating, database storage, API, and front-end integration.

## What's a Command Interpreter?

Similar to a shell but limited to a specific use-case, the command interpreter is designed to manage objects within the project. Its functionalities include creating new objects, retrieving objects from files or databases, performing operations on objects, updating object attributes, and destroying objects.

## Learning Objectives

Upon completing this project, participants should be able to:

- Create a Python package
- Develop a command interpreter in Python using the cmd module
- Implement Unit testing in a large project
- Serialize and deserialize a Class
- Write and read a JSON file
- Manage datetime in Python
- Understand UUID (Universally Unique Identifier)
- Utilize *args and **kwargs in Python
- Handle named arguments in a function

## Requirements

### Python Scripts

- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A README.md file at the root of the project folder is mandatory
- Code should use pycodestyle (version 2.8.*)
- All files must be executable
- Length of files will be tested using `wc`
- All modules, classes, and functions should have documentation
- Documentation should provide a real sentence explaining the purpose of the module, class, or method

### Python Unit Tests

- Allowed editors: vi, vim, emacs
- All test files should end with a new line
- All test files should be inside a folder named `tests`
- Use the unittest module
- All test files should be Python files (extension: .py)
- All test files and folders should start with `test_`
- The organization of files in the `tests` folder should mirror the project structure
  - e.g., For `models/base_model.py`, unit tests must be in `tests/test_models/test_base_model.py`
- All tests should be executed using the command: `python3 -m unittest discover tests`

## Execution

The shell should work both in interactive mode and non-interactive mode. Examples are provided below:

**Interactive Mode:**
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) quit
$
```

**Non-Interactive Mode:**
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

All tests should also pass in non-interactive mode:

```bash
$ echo "python3 -m unittest discover tests" | bash
```

