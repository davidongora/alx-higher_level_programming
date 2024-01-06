#!/usr/bin/python3
"""this is a locked class where the \
    first attribute has to be first_name"""
class LockedClass:
    """first attribute must be named first_class"""
    __slot__ = ["first_name"]