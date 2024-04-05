
# Documentation for pyTypes

### A `TypedList` is a wrapper around a `.__value` object, which forces it to follow a `.__type` directive.
<b>Class signature:</b> `TypedVar(Alias: str = "NO_ALIAS", Type: type = NoneType, Value: object = None)`
- `.__alias` can be set using `Alias` named constructor parameter or using `setAlias(Alias: str)` after init.
- `.__type` can be set using `Type` named constructor parameter or using `setType(Type: type)` after init. 
- `.__value` can be set using `Value` named constructor parameter or using `setValue(Value: object)` after init.


- if `.__value` is set while `.__type` is `NoneType`, TypedVar will infer the type from `type(Value)`.
- a `.__value` of `None` is treated as special, because it's valid for all `.__type` values.


- `setType(Type: type)` will allow you to set the Type regardless, even if it doesn't match with the current non-null `.__value`


- `setValue(Value: object)` will only allow you to set the value as defined by the instance variable `.__type`


### A `TypedList` is a wrapper around a `.__items` list, which forces all list items to follow a `.__type` directive.
<b>Class signature:</b> `TypedList(Alias: str = "NO_ALIAS", Type: type = NoneType)`

<b>NOTE: </b>It wraps the `.__items` list instead of being a subclass of `list` to limit undefined behaviour by restricting the interface methods to TypedList methods only. 

- `.__alias` can be set using `Alias` named constructor parameter or using `setAlias(Alias: str)` after init.
- `.__type` can be set using `Type` named constructor parameter or using `setType(Type: type)` after init. 


- append to `.__items` using `append(Item: object)` method, given that `Item` matches `.__type`
- remove from `.__items` using `remove(Item: object)` method, given that `Item` exists in a non-empty `.__items`
- get from `.__items` using `get(Item: object)` method, given that `Item` exists in a non-empty `.__items`
- get `.__items` as list using `getItems()` method


- if an item is appended to `.__items` while `.__type` is `NoneType`, TypeList will infer the type from `type(Value)`.


- `setType(Type: type)` will allow you to set the Type regardless, even if it doesn't match with type of the items in `.__items`

## Architectural Notes
- `TypedList` could have been defined as a subclass of `list`. 
However, inherited methods could lead to unintended or undefined behaviour. 
By using a wrapper structure, this is avoided.

