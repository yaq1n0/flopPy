
# Documentation for pyTypes

## classes available
### `TypedVar(Alias: str = "NO_ALIAS", Type: type = NoneType, Value: object = None)`

- TypedVar will default to `TypedVar("NO_ALIAS", NoneType, None)`
- TypedVar can be given a string alias at init or using `setAlias`
- TypedVar can be assigned a type at init or using `setType`
- TypedVar can be assigned a value at init or using `setValue`


- `setType` will allow you to set the Type regardless, even if it doesn't match with the current `.__value`
- `setValue` will only allow you to set the value as defined by the instance variable `.__type`, unless `override=True` (NOT RECOMMENDED)

- During init, if `Value` is given and `Type` is not given, TypedVar will infer `.__type` from `.__value`
- The TypedVar's type is an instance of `<class 'type'>` from invoking Python's builtin `type()` function