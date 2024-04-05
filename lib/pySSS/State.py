import logging

from lib.pyTypes import TypedList, TypedVar


class State(TypedList):

    def __init__(self, Alias: str = "UNNAMED_STATE"):
        super().__init__(Alias=Alias, Type=TypedVar)

    def __repr__(self) -> str:
        # this seems to show in print() statements
        return "[State: {}]".format(self.__items)



    def __str__(self) -> str:
        # this seems to show in logger() statements
        return "[State: {}]".format(self.__items)

    def setType(self, Type):
        raise Exception("[pySSS.State] you can't change the type of a State")



    def getByAlias(self, ItemAlias) -> TypedVar or None:
        for Item in super().getItems():
            if Item.getAlias() == ItemAlias:
                return Item
        return None


if __name__ == '__main__':

    logging.getLogger().setLevel(logging.DEBUG)
    logging.debug("====commencing self test for State.py====")
    state = State()
    logging.debug("type should already be set to TypedVar: {}".format(state.getType()))
    state.append(TypedVar('test'))
    logging.debug("TypedVar(test) should be added to state: {}".format(state.getType()))
