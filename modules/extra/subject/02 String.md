## STR MODULE
Create a class named `String`. The class must accept a variable number of positional arguments, a separator and an ending string. The class must have the following attributes: `message`, `sep`, `end`, `object`. The class must return the message.

Recreate and create the following string-related methods according to the requirements below.

### class variables, initiation and return
Receive a variable number of positional arguments. Convert the received arguments to a single string using the specified separator. Store the resulting string in the appropriate object attribute. The separator must default to `' '`. The ending string must default to `'\n'`. The constructor must not return a value.
### Prototype example:
```py
def __init__(self, *objects: Value, sep: str = ' ', end: str = '\n') -> None:
```
#### Authorized:
```txt
None
```

### join()
Recreate the behavior of joining elements into a single string. Receive a list or dictionary and an optional separator. Join all elements using the specified separator. If no separator is provided, use `self.sep`. If no target object is provided, raise an appropriate exception. The returned string must always end with a newline.
#### Authorized:
```txt
None
```

### strip()
Recreate the behavior of stripping whitespace from a string. Receive a string and return a string. Remove unnecessary whitespace from the beginning and end of the string while keeping all other characters unchanged. If no string is provided, raise an appropriate exception.
#### Authorized:
```txt
None
```

### formal()
Create a function that formats a string. The first letter of the string must be uppercase. The first letter following a final punctuation character must also be uppercase. All other characters must remain unchanged.
#### Authorized:
```txt
None
```

### shuffle()
Create a function that randomly rearranges the characters of a string. Receive a string and return a string. If no string is provided, raise an appropriate exception.
#### Authorized:
```txt
import random, random.randint()
```

### split()
Recreate the behavior of splitting a string. Receive a string, an optional separator and an optional maximum number of splits. If no separator is provided, use `self.sep`. If `max_split` is provided, perform at most the specified number of splits. If `max_split` is not provided, split until the end of the string. If no string is provided, raise an appropriate exception. Return a list of strings.
#### Authorized:
```txt
None
```

### split_by()
Create a function that splits a string into chunks of a specified length. Receive a string and a chunk length. If no length is provided, or if the length is less than 3, raise a `ValueError`. If no string is provided, use `self.message`. Return a list of strings.
#### Authorized:
```txt
None
```

### div_str()
Create a function that divides a string into a specified number of parts. Receive a string and an integer representing the number of parts. The resulting parts must have equal lengths whenever possible. The last part may be shorter.
#### Authorized:
```
txt import math, math.ceil()
```

### is_punct()
Create a function that checks whether a character is a punctuation character. Receive a string and return a `bool`. The string must contain exactly one character. If the string length is different from one, raise a `ValueError`. If no string is provided, raise an appropriate exception.
#### Authorized:
```txt
None
```

### is_special()
Create a function that checks whether a character is a special character. Receive a string and return a `bool`. The string must contain exactly one character. If the string length is different from one, raise a `ValueError`. If no string is provided, raise an appropriate exception.
#### Authorized:
```txt
None
```

### there_is_punct()
Create a function that checks whether a string contains a punctuation character. Receive a string and a list of exceptions. Return `True` if the string contains at least one punctuation character that is not present in the exception list. If no string is provided, raise an appropriate exception.
#### Authorized:
```txt
None
```

### there_is_special()
Create a function that checks whether a string contains a special character. Receive a string and a list of exceptions. Return `True` if the string contains at least one special character that is not present in the exception list. If no string is provided, raise an appropriate exception.
#### Authorized:
```txt
None
```

### there_is_alpha()
Create a function that checks whether a string contains an alphabetic character. Receive a string and a list of exceptions. Return `True` if the string contains at least one alphabetic character that is not present in the exception list. If no string is provided, raise an appropriate exception.
#### Authorized:
```txt
None
```

### there_is_int()
Create a function that checks whether a string contains a numeric character. Receive a string and a list of exceptions. Return `True` if the string contains at least one numeric character that is not present in the exception list. If no string is provided, raise an appropriate exception.
#### Authorized:
```txt
None
```