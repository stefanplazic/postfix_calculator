# -*- coding: utf-8 -*-
"""
Modul sadrži implementaciju steka na osnovu liste.
"""


class StackError(Exception):
    """
    Model Stack exceptions
    """
    pass


class Stack(object):
    """
    Stack implementation using list
    """

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        """
        Check if stack is empty
        """
        return len(self._data) == 0

    def push(self, e):
        """
        Add element on top of stack

        Argument:
        - `e`: new element to add
        """
        self._data.append(e)

    def top(self):
        """
        Return element on top of stack, but do not remove it!
        """
        if self.is_empty():
            raise StackError('Stek je prazan.')
        return self._data[-1]

    def pop(self):
        """
        Remove the element on top of the stack
        """
        if self.is_empty():
            raise StackError('Stek je prazan.')
        return self._data.pop()


