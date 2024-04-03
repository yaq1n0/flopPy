"""
main file for TypedVar
"""

import logging


class TypedVar():
    def __init__(self, val=None, _strict=True):
        self.value = None
        self.type = None
        self.strict = _strict

        self.setVal(val)

    def __repr__(self):
        # this seems to show in print() statements
        return "TypeVar(val={})".format(self.value)

    def __str__(self):
        # this seems to show in logger() statements
        return "TypeVar(val={})".format(self.value)

    def getVal(self):
        return self.value

    def getType(self):
        return self.type

    def setVal(self, val):
        if self.value is None:
            self.value = val
            self.type = type(val)
            logging.debug("[pyTypes.TypedVar] successfully assigned initial value {} with type {}".format(val, self.type))
            return

        if type(val) is self.type:
            self.value = val
            logging.debug("[pyTypes.TypedVar] successfully assigned new value {}".format(val))
            return

        if self.strict:
            raise TypeError('')
        else:
            logging.error("[pyTypes.TypedVar] TypeConflict: can't assign new value {} with type {} to TypedVar with type {}".format(val, type(val), self.type))

    def enableStrict(self):
        self.strict = True

    def disableStrict(self):
        self.strict = False


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    logging.debug("====commencing self test for TypedVar.py====")
    typedVar = TypedVar('testStringVal')
    typedVar.setVal('testStringValChanged')
    print(typedVar.getVal())

    # this should just not change the value
    # typedVar.disableStrict()
    # typedVar.setVal(1)

    # this should yell at you and throw an error
    # logging.debug("==an error should follow==")
    # typedVar.enableStrict()
    # typedVar.setVal(1)
