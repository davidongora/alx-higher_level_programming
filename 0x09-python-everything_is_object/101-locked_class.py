#!/usr/bin/python3
class LockedClass:
    """first attribute must be named first_class"""
    __slot__ = ["first_name"]
