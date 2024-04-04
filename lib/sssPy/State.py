"""
main file for StupidSimpleStatesPython
A State instance is just a TypedList instance with only TypedVars
"""

import logging

from lib.pyTypes import TypedList, TypedVar


class State(TypedList):

    def __init__(self):
        super().__init__()
        super().setType(TypedVar)


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    logging.debug("====commencing self test for State.py====")
    state = State()
    logging.debug("type should already be set to TypedVar: {}".format(state.getType()))
    state.append(TypedVar('test'))
    logging.debug("TypedVar(test) should be added to state: {}".format(state.getType())

