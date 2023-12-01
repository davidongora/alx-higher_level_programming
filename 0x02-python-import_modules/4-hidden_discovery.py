#!/usr/bin/python3
if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import imp
    filename_pyc = 'hidden_4.pyc'
    for i in dir(filename_pyc):
        if i[0] != '__':
            print("{}".format(i))
