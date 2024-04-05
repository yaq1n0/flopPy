from unittest import TestCase
from types import NoneType
from lib.pyTypes import TypedList


class TestTypedList(TestCase):
    defaultAlias = "NO_ALIAS"
    defaultType = NoneType
    defaultValue = []

    def test_implicit_all(self):
        """ test None Type and None Value """
        typedList = TypedList()
        self.assertEqual(typedList.getAlias(), self.defaultAlias)
        self.assertEqual(typedList.getType(), self.defaultType)
        self.assertEqual(typedList.getItems(), self.defaultValue)
        print("test_implicit_all:", typedList)

    def test_fromList(self):
        typedList = TypedList()
        List = ['string', 'int', 'float']
        expectedType = str
        typedList.fromList(List)
        self.assertEqual(typedList.getType(), expectedType)
        self.assertEqual(typedList.getItems(), List)
        print("test_fromList:", typedList)

    def test_append(self):
        typedList = TypedList()
        List = ['string', 'int', 'float']
        expectedType = str
        for element in List:
            typedList.append(element)
        self.assertEqual(typedList.getType(), expectedType)
        self.assertEqual(typedList.getItems(), List)
        print("test_append:", typedList)



