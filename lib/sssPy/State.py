"""
main file for StupidSimpleStatesPython
A State instance is just a TypedList instance with only TypedVars
"""

import logging

from lib.pyTypes import TypedList, TypedVar


class State(TypedList):

    def __init__(self):
        super().__init__()
        # add and remove a TypedVar instance at init to set the TypedList instance type to TypedVar
        typedVar = TypedVar()
        super().append(typedVar)
        super().remove(typedVar)


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    state = State()
    state.append(TypedVar('test'))
    print(state.getItems())

