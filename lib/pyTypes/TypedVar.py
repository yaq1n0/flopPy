import logging
from types import NoneType


class TypedVar(object):
    """ TypedVar class """

    def __init__(self, Alias: str = "NO_ALIAS", Type: type = NoneType, Value: object = None) -> None:
        # explicit strict type checking
        if not isinstance(Alias, str):
            raise TypeError("[pyTypes.TypedVar] Alias must be a str")
        if not isinstance(Type, type):
            raise TypeError("[pyTypes.TypedVar] Type must be a type")
        if not isinstance(Value, object):
            raise TypeError("[pyTypes.TypedVar] Value must be a object")

        # set the .__alias field
        self.setAlias(Alias)

        # set the .__type and .__value fields with logic to handle implicit values
        # no Type provided, no Value provided
        if Type is NoneType and Value is None:
            self.setType(Type)
            self.setValue(Value)
            return

        # no Type provided, Value provided
        if Type is NoneType and Value is not None:
            self.setType(type(Value))
            self.setValue(Value)
            return

        # Type provided, Value not provided
        if Type is not NoneType and Value is None:
            self.setType(Type)
            self.setValue(Value)  # Value is None, will set Value regardless
            return

        # Type provided, Value provided
        if Type is not NoneType and Value is not None:
            if type(Value) is Type:
                self.setType(Type)
                self.setValue(Value)
            else:
                raise TypeError(
                    "[pyTypes.TypedVar] Can't assign Value of {} type to TypedVar{}".format(type(Value), Type))
            return

        # undefined behavior catch all
        raise Exception("[pyTypes.TypedVar] Unexpected error in constructor")

    def __repr__(self) -> str:
        # this seems to show in print() statements
        return "[TypedVar{}: {}]".format(self.__type, self.__value)

    def __str__(self) -> str:
        # this seems to show in logger() statements
        return "[TypedVar{}: {}]".format(self.__type, self.__value)

    def getAlias(self) -> str:
        return self.__alias

    def getType(self) -> type:
        return self.__type

    def getValue(self) -> object:
        return self.__value

    def setAlias(self, Alias: str) -> bool:
        # check if new Alias value is a string
        if not isinstance(Alias, str):
            raise TypeError("[pyTypes.TypedVar] setAlias() error, Alias must be a string")
        else:
            self.__alias = Alias
            logging.debug("[pyTypes.TypedVar] successfully set alias to {}".format(self.__alias))
            return True

    def setType(self, Type):
        # check if new Type value is a type
        if not isinstance(Type, type):
            raise TypeError("[pyTypes.TypedVar] setType() error, Type must be a type")

        # implicit else, set new Type
        else:
            self.__type = Type
            logging.debug("[pyTypes.TypedVar] successfully set type to {}".format(self.__type))
            return True

    def setValue(self, Value) -> bool:
        # check if new Value is an object
        if not isinstance(Value, object):
            raise TypeError("[pyTypes.TypedVar] setValue() error, Value must be an object")

        # disregard .__type = NoneType and infer new .__type from Value
        if self.__type is NoneType:
            self.setType(type(Value))
            self.__value = Value
            logging.debug(
                "[pyTypes.TypedVar] successfully overridden default NoneType to {} & set value to {} ".format(
                    self.__type, self.__value))
            return True

        # type(Value) doesn't match .__type
        if type(Value) is not self.__type:
            raise TypeError(
                "[pyTypes.TypedVar] setValue() error, can't assign {} type to TypedVar{}".format(
                    type(Value), self.__type))

        # type(Value) matches .__type
        if type(Value) is self.__type:
            self.__value = Value
            logging.debug("[pyTypes.TypedVar] successfully set value to {}".format(self.__type))
            return True

        # undefined behavior catch all
        raise Exception("[pyTypes.TypedVar] Unexpected error in setValue()")
