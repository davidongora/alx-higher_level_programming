#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import imp

    names = 'hidden_4.pyc'
    for i in dir(names):
        if i[0] != '_':
            print("{}".format(i))
