import logging
from types import NoneType


class TypedList(object):
    def __init__(self, Alias: str = "NO_ALIAS", Type: type = NoneType):
        # explicit strict type checking
        if not isinstance(Alias, str):
            raise TypeError("[pyTypes.TypedList] Alias must be a str")
        if not isinstance(Type, type):
            raise TypeError("[pyTypes.TypedList] Type must be a type")

        self.setAlias(Alias)  # self.__alias = Alias
        self.setType(Type)  # self.__type = Type
        self.resetItems()  # self.__items = []

    def __repr__(self) -> str:
        # this seems to show in print() statements
        return "[TypedList{}: {}]".format(self.__type, self.__items)

    def __str__(self) -> str:
        # this seems to show in logger() statements
        return "[TypedList{}: {}]".format(self.__type, self.__items)

    @staticmethod
    def isSingleTypedList(List: list) -> bool:
        # explicit type-checking
        if not isinstance(List, list):
            raise TypeError("[pyTypes.TypedList] isSingleTypedList() input must be a list")

        # handle empty list
        if len(List) == 0:
            raise IndexError("[pyTypes.TypedList] isSingleTypedList() input can't be empty list")

        # check each element's type against the first element,
        # if any aren't equal, the list isn't single typed, return false.
        for element in List:
            if type(element) != type(List[0]):
                return False

        # implicitly, if all the elements in the list are the same type, return True
        return True

    @staticmethod
    def getListType(List: list) -> type:
        # explicit type-checking
        if not isinstance(List, list):
            raise TypeError("[pyTypes.TypedList] getListType() input must be a list")

        # handle empty list
        if len(List) == 0:
            raise IndexError("[pyTypes.TypedList] getListType() input can't be empty list")

        if not TypedList.isSingleTypedList(List):
            raise TypeError(
                "[pyTypes.TypedList] getListType() can't get list type of a multi-typed list, maybe you meant getListTypes()?")

        return type(List[0])

    @staticmethod
    def getListTypes(List: list) -> [type]:
        # explicit type-checking
        if not isinstance(List, list):
            raise TypeError("[pyTypes.TypedList] getListTypes() input must be a list")

        # handle empty list
        if len(List) == 0:
            raise IndexError("[pyTypes.TypedList] getListTypes() input can't be empty list")

        type_list = []
        for element in List:
            if type(element) not in type_list:
                type_list.append(type(element))

        return type_list

    def getAlias(self):
        return self.__alias

    def getType(self):
        return self.__type

    def getItems(self):
        return self.__items

    def setAlias(self, Alias):
        # check if new Alias value is a string
        if not isinstance(Alias, str):
            raise TypeError("[pyTypes.TypedList] setAlias() error, Alias must be a string")
        else:
            self.__alias = Alias
            logging.debug("[pyTypes.TypedList] successfully set alias to {}".format(self.getAlias()))
            return True

    def setType(self, Type):
        # check if new Type value is a type
        if not isinstance(Type, type):
            raise TypeError("[pyTypes.TypedList] setType() error, Type must be a type")

        # implicit else, set new Type
        else:
            self.__type = Type
            logging.debug("[pyTypes.TypedList] successfully set type to {}".format(self.getType()))
            return True

    def resetItems(self):
        self.__items = []

    def append(self, Item) -> bool:
        # check if Item is an object
        if not isinstance(Item, object):
            raise TypeError("[pyTypes.TypedList] append() error, Item must be an object")

        if Item is None:
            raise TypeError("[pyTypes.TypedList] append() error, can't add None to a TypedList")

        # disregard .__type = NoneType and infer new .__type from Item
        if self.__type is NoneType:
            self.setType(type(Item))
            self.__items.append(Item)
            logging.debug(
                "[pyTypes.TypedList] successfully overridden default NoneType to {} & appended {} to __items ".format(
                    self.__type, Item))
            return True

        # type(Item) doesn't match .__type
        if type(Item) is not self.__type:
            raise TypeError(
                "[pyTypes.TypedList] append() error, can't append {} type to TypedList{}".format(
                    type(Item), self.__type))

        # type(Item) matches .__type
        if type(Item) is self.__type:
            self.__items.append(Item)
            logging.debug("[pyTypes.TypedList] successfully appended {} to TypedList{}".format(Item, self.__type))
            return True

        # undefined behavior catch all
        raise Exception("[pyTypes.TypedList] Unexpected error in setValue()")

    def get(self, index) -> object:
        if self.__items is []:
            raise IndexError("[pyTypes.TypedList] get() error, can't get from an empty Typedlist")

        if index < 0 or index >= len(self.__items):
            raise IndexError("[pyTypes.TypedList] get() error, invalid index")

        return self.__items[index]

    def remove(self, index) -> bool:
        if self.__items is []:
            raise IndexError("[pyTypes.TypedList] remove() error, can't remove from an empty Typedlist")

        if index < 0 or index >= len(self.__items):
            raise IndexError("[pyTypes.TypedList] remove() error, invalid index")

        del self.__items[index]
        return True

    def fromList(self, List: list) -> bool:
        if not isinstance(List, list):
            raise TypeError("[pyTypes.TypedList] fromList() List input must be a list")

        if list is []:
            raise TypeError("[pyTypes.TypedList] fromList() List input can't be empty list")

        if not TypedList.isSingleTypedList(List):
            raise TypeError("[pyTypes.TypedList] fromList() List input can only contain elements of a single type")

        if TypedList.getListType(List) is self.__type or self.__type is NoneType:
            for element in List: self.append(element)
            return

        elif TypedList.getListType(List) is not self.__type:
            raise TypeError(
                "[pyTypes.TypedList] List input of type {} doesn't match TypedList type {}".format(type(List[0]),
                                                                                                   self.__type))

        raise Exception("[pyTypes.TypedList] fromList() unexpected error occurred")
