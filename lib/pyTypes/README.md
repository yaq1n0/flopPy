
# Documentation for pyTypes

## classes available
### `TypedVar(name, val=None, strict=True)`

- `getName()`, `getVal()`, `setVal()`, `disableStrict()`, `enableStrict()`
- TypedVar must be given a variable name at initialization
- TypedVar can be given a first value at init or with the first call of `.setVal()`
- the first value assigned will be the fixed `<type>` of the TypedVar instance
- you can only use `setVal` with a value of the same type as the TypedVar's fixed `<type>`
- The TypedVar's type is an instance of `<class 'type'>` from invoking Python's builtin `type()` function
- TypedVars are `strict` by default. 
- You can disable `TypeError` throwing by disabling strict (NOT RECOMMENDED)