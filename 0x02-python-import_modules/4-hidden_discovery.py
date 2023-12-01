#!/usr/bin/python3
if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import imp
    filename_pyc = 'hidden_4.pyc'
    module = filename_pyc
    for i in dir(module):
        if not i.startswith("__"):
            print("{}".format(i))
