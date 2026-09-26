## DICT MODULE
Create a class named `Dicty`. The class must accept a variable number of keyword arguments. The class must have the following attributes: `dictionary`, `keywords`, `values`. The class must return the dictionary created

Recreate and create the following dictionary-related methods according to the requirements below.

### class variables, initiation and return
Receive a variable number of keyword arguments. If no keyword arguments are provided, initialize an empty dictionary. Otherwise, initialize a dictionary containing all received key-value pairs. Store the dictionary in `self.dictionary`. Store a list containing all dictionary keys in `self.keywords`. Store a list containing all dictionary values in `self.values`. The constructor must not return a value.
### Prototype example:
```py
def __init__(self, **KVobj: Value) -> None:
```
#### Authorized:
```txt
None
```

### create()
Create a dictionary from a variable number of keyword arguments. Receive keyword arguments and return a dictionary containing all received key-value pairs.
#### Authorized:
```txt
None
```

### get_values()
Recreate the behavior of `dict.values()`. Receive a dictionary and return a list containing all its values.
#### Authorized:
```txt
None
```

### get_keys()
Recreate the behavior of `dict.keys()`. Receive a dictionary and return a list containing all its keys.
#### Authorized:
```txt
None
```

### get_type()
Create a function that describes the types contained in a dictionary. Receive a dictionary and return a string describing the types of its keys and values. The returned string must follow this pattern:

`"[key_type, value_type]"`

Each type must appear only once. For example, given a dictionary:
```py
di = {
    0, "hello, world"
    "name": "False":
    "height": 5.4
}
```
the result must be: `"[int | str, str | float]"`

If there is more than two types, must return unknown type value. For example, given the dictionary
```py
di = {
    0, "hello, world"
    "name": False:
    "height": 5.4
}
```
the result must be: `"[int | str, Any | Value]"`
#### Authorized:
```txt
None
```

### append()
Create a function that adds a key-value pair to a dictionary. Receive a dictionary, a key and a value. Add the key-value pair to the dictionary. Return `None`.
#### Authorized:
```txt
None
```