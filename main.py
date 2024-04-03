

# def func0(s):
#     print(s)
#
# def func1(s):
#     print("World")
#
# x = [func0, func1]
#
# for i in x:
#     i('hello')

from lib.pyTypes.TypedList import TypedList
from lib.pyTypes.TypedVar import TypedVar

typedList = TypedList()
typedVar = TypedVar('stringVar')
print(type(typedVar))
