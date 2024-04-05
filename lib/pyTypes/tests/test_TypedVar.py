from unittest import TestCase
from types import NoneType
from lib.pyTypes import TypedVar


class TestTypedVar(TestCase):
    defaultAlias = "NO_ALIAS"
    defaultType = NoneType
    defaultValue = None

    def test_implicit_all(self):
        """ test None Type and None Value """
        typedVar = TypedVar()
        self.assertEqual(typedVar.getAlias(), self.defaultAlias)
        self.assertEqual(typedVar.getType(), self.defaultType)
        self.assertEqual(typedVar.getValue(), self.defaultValue)

    def test_explicit_type(self):
        """ test explicit Type and None Value """
        testType = int
        typedVar = TypedVar(Type=testType)
        self.assertEqual(typedVar.getAlias(), self.defaultAlias)
        self.assertEqual(typedVar.getType(), testType)
        self.assertEqual(typedVar.getValue(), self.defaultValue)

    def test_explicit_value(self):
        """ test implicit Type inference and explicit Value """
        testValue = 10
        testType = type(testValue)
        typedVar = TypedVar(Value=testValue)
        self.assertEqual(typedVar.getAlias(), self.defaultAlias)
        self.assertEqual(typedVar.getType(), testType)
        self.assertEqual(typedVar.getValue(), testValue)

    def test_valid_explicit_all(self):
        """ test valid explicit Type and explicit Value"""
        testValue = 10
        testType = type(testValue)
        typedVar = TypedVar(Type=testType, Value=testValue)
        self.assertEqual(typedVar.getAlias(), self.defaultAlias)
        self.assertEqual(typedVar.getType(), testType)
        self.assertEqual(typedVar.getValue(), testValue)

    def test_invalid_explicit_all(self):
        """ test invalid explicit Type and explicit Value"""
        testValue = 10
        testType = str
        self.assertRaises(TypeError, lambda: TypedVar(Type=testType, Value=testValue))

    def test_setValue(self):
        """ test valid setValue() call and implicit type inference"""
        testValue = 10
        typedVar = TypedVar()
        typedVar.setValue(testValue)
        self.assertEqual(typedVar.getValue(), 10)
        self.assertEqual(typedVar.getType(), type(testValue))

    def test_setValue_fail(self):
        """ test invalid setValue() call"""
        testValue = 10
        testType = str
        typedVar = TypedVar(Type=testType)
        self.assertRaises(TypeError, lambda: typedVar.setValue(testValue))

