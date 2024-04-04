"""
main file for TypedList
TypedList is a list of single type

The current implementation isn't a subclass of list,
to prevent possible issues with undefined behavior from inherited methods

By instead wrapping the list instance with a TypedList instance,
you can better define, predict and control strict behavior
"""

import logging


class TypedList:
    def __init__(self, strict=True):
        self.items = []
        self.type = 'undefined'
        self.strict = strict

    def getItems(self):
        return self.items

    def getType(self):
        return self.type

    def setType(self, _type: type):
        self.type = _type

    def append(self, item):
        # if the type hasn't been defined yet, define it and add the first item
        if self.type == 'undefined':
            self.setType(type(item))
            self.items.append(item)
            logging.debug(
                "[pyTypes.TypedList] successfully added first item {} and set TypedList type to {}".format(item, self.type))
            return

        # type has been defined, var is correct type
        if type(item) is self.type:
            self.items.append(item)
            logging.debug("[pyTypes.TypedList] successfully added item {} to TypedList".format(item))
            return

        # type has been defined, var is wrong type, strict mode enabled
        msg = "[pyTypes.TypedList] TypeConflict: can't add new item {} with type {} to TypedList with type {}".format(item,
                                                                                                            type(item),
                                                                                                            self.type)
        if self.strict:
            raise TypeError(msg)

        # type has been defined, var is wrong type, strict mode enabled
        logging.error(msg)
        return

    def remove(self, item):
        # handle removing from empty list
        if not self.items:
            msg = "[pyTypes.TypedList] IndexError: can't remove from empty list"
            if self.strict:
                raise IndexError(msg)

            # if not strict, implicit else
            logging.error(msg)
            return

        # remove existing item from non-empty list
        if item in self.items:
            self.items.remove(item)
            logging.debug("[pyTypes.TypedList] successfully removed {} from TypedList".format(item))
            return

        # type conflict in non-empty list
        if type(item) is not self.type:
            logging.debug(
                "[pyTypes.TypedList] TypeConflict: item {} is not the same type as TypedList of type {}".format(item, self.type))
            return

        # item doesn't exist in non-empty list
        msg = "[pyTypes.TypedList] TypedList doesn't contain {} to remove".format(item)
        logging.error(msg)
        return

    def enableStrict(self):
        self.strict = True

    def disableStrict(self):
        self.strict = False


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    logging.debug("====commencing self test for TypedList.py====")
    typedList = TypedList()
    typedList.append('test0')
    typedList.append('test1')
    typedList.append('test2')
    typedList.remove('test1')
    print(typedList.getItems())

    # this should throw an error
    # typedList.extend(['test1', 2])

    # this should throw an error
    # typedList.extend('test1')
    # typedList.extend('test1')
