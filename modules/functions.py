## organizing code in modules

# constant naming convention—it signals to other programmers
# that FILEPATH is intended to remain the same throughout the program.
# CONSTANTS are put at the top of the module
FILEPATH = "todos.txt" # if we physically rename the todos.txt, we just change it once here.

def read_file_todos(filename=FILEPATH):
    """
    Reads the text file and returns a list
    of To-do items.
    """
    with open(filename, "r") as file:
        todos_local = file.readlines()
    return todos_local

def write_file_todos(todos_arg, filename=FILEPATH): # non-default params come first
    """
    Writes a list of todos to a text file
    """
    with open(filename, "w") as file:
        file.writelines(todos_arg)


# print("This is a message from modules") # this is executed when we run cli.py -
# to prevent use:

# explanation: The code runs in the functions.py file
# because __name__ is set to "__main__" only when the file is
# executed directly (run it here to see this in practice),
# but when imported as a module in another file, __name__ takes the module's name instead.

# It runs in functions.py because __name__ == "__main__" is only True when
# the file is run directly, not when imported as a module

# "__main__" is just a special name Python assigns to the script
# that's being run directly. It doesn't refer to your cli.py file—if you
# import functions.py into cli.py, functions.py's __name__ will be
# "functions", not "__main__".

# print(__name__) # uncomment this here and run cli.py and you will
# see the value is module.functions but when we run functions.py directly here the value
# is __main__

if __name__ == "__main__":
    print("Hello from modules")