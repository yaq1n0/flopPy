from unittest import TestCase
from types import NoneType
from lib.pySSS import State
from lib.pyTypes import TypedVar


class TestState(TestCase):
    defaultAlias = "UNNAMED_STATE"
    defaultType = TypedVar
    defaultValue = []

    def test_implicit_all(self):
        """ test None Type and None Value """
        state = State()
        self.assertEqual(state.getAlias(), self.defaultAlias)
        self.assertEqual(state.getType(), self.defaultType)
        self.assertEqual(state.getItems(), self.defaultValue)
        print(state)