
# Documentation for StupidSimpleStatesPython

## classes available
### `TypedVar(val=None, strict=True)`

- `getType()`, `getVal()`, `setVal()`, `disableStrict()`, `enableStrict()`
- TypedVar can be given a first value at init or with the first call of `.setVal()`
- the first value assigned will be the fixed `<type>` of the TypedVar instance
- you can only use `setVal` with a value of the same type as the TypedVar's fixed `<type>`
- The TypedVar's type is an instance of `<class 'type'>` from invoking Python's builtin `type()` function
- TypedVars are `strict` by default. 
- You can disable `TypeError` throwing by disabling strict (NOT RECOMMENDED)