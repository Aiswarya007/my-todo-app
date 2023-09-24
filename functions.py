FILEPATH = "todos.txt"


# def get_todos(filepath):    # filepath is the parameter of the function
# def get_todos(filepath="files/subfiles/todos.txt"):  # default parameter
# def get_todos(filepath="todos.txt"):
def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
      to-do items.
      """
    # with open('files/subfiles/todos.txt', 'r') as file:
    with open(filepath, 'r') as file_local:
        # todos = file.readlines()
        todos_local = file_local.readlines()
    return todos_local


# print(help(get_todos))        # to get docstring

# this function is more like a procedure, it doesn't return anything
# def write_todos(filepath, todos_arg):
# todos_arg is the non-default parameter and it should come before default parameter
# def write_todos(filepath="files/subfiles/todos.txt", todos_arg):
def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


# print(__name__)
if __name__ == "__main__":
    print("Hello")
    print(get_todos())
