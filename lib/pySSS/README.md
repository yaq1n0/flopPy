
# Documentation for PythonStupidSimpleStates (pySSS)

### A `State` is a wrapper around a `TypedList<TypedVar>` instance with additional logic.
<b>Class signature:</b> `State()`


###  A `StateReader` instance can be used to read a file into a `State` object
<b>Class signature:</b> `StateReader(Path="path/to/your/stateFile.statefile")`

- `.read()` method returns a `State` instance, assuming a valid `.__path`

###  A `StateWriter` instance can be used to write a `State` object to a file
<b>Class signature:</b> `StateWriter(State=stateInstance, Path="path/to/your/stateFile.statefile)`

- `.write()` turns a `State` instance into a valid stateFile, assuming a valid `.__path`

### `.stateFile` file is a file that contains the file representation of a state.

## Architectural Notes
- `State` could have been defined as a subclass of `TypedList<TypedVar>`. 
However, inherited methods could lead to unintended or undefined behaviour. 
By using a wrapper structure, this is avoided.
