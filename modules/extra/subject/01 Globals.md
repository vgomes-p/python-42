# GLOBAL EXERCISES
## TYPE ALIAS:
Create a type alias named `Value` that represents any of the following types: `str`, `int`, `float`, `bool`, `list`, `dict`, `set`, `tuple`, `None`

<!-- -+×+-=-+×+-=-+×+-=-+×+-=-+×+-=-+×+-=-+×+-=-+×+-=-+×+-=-+×+-=-+×+-=-+×+-=-+×+-=-+×+-=-+×+-=-+×+- -->

## CONSTANTS:
Create constants representing the following ANSI escape sequences:

- Default: `\033[m`
- Red: `\033[31m`
- Green: `\033[32m`
- Yellow: `\033[33m`
- Pink: `\033[35m`
- Cyan: `\033[36m`
- Blue
- Orange
- Bold: `\033[1m`
- Invert: `\033[1;4;7;97m`

<!-- -+×+-=-+×+-=-+×+-=-+×+-=-+×+-=-+×+-=-+×+-=-+×+-=-+×+-=-+×+-=-+×+-=-+×+-=-+×+-=-+×+-=-+×+-=-+×+- -->

## REFERENCES:
Create reusable references for the following character groups:
### Special characters

```['#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '/', '<', '=', '>', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~', '\\']```

### Punctuation characters
`['!', ',', '.', ':', ';', '?']`

### Final punctuation characters
`['!', '.', '?']`

<!-- -+×+-=-+×+-=-+×+-=-+×+-=-+×+-=-+×+-=-+×+-=-+×+-=-+×+-=-+×+-=-+×+-=-+×+-=-+×+-=-+×+-=-+×+-=-+×+- -->

## GLOBAL FUNCTIONS:
### Create the following global functions.

### ft_len()
Recreate the behavior of the built-in `len()` function. Receive a `Value` and return an integer representing the number of elements contained in the value. The built-in `len()` function must not be used.
#### Authorized:
```txt
None
```

### ft_type()
Recreate the behavior of retrieving the type name of an object. Receive a `Value` and return a string containing the name of its type. The built-in `type()` function must not be used.

`Hint: Find how to retrieve the class name of an object.`
#### Authorized:
```txt
None
```

### ft_typing()

Create a function that prints a string one character at a time. The function must receive a string, a delay and an ending string. The delay must define the time waited between each character. The delay must default to `0.05` seconds. The ending string must default to `'\n'`.

#### ### Prototype example:
```py
def ft_typing(entry: str, timer: float = 0.05, end: str = '\n') -> None:
```
#### Authorized:
```txt
import time, time.sleep(), print(flush=True)
```

### ft_print()
Create a function that receives a string and returns an integer. Print the string entered and return the number of characters printed.
#### Authorized:
```txt
import sys, sys.stdout(), sys.stdout().flush()
```

### ft_printd()
Create a function that receives a string and returns an integer. Print the string and reset the terminal color to the default color after printing. The returned integer must represent the number of characters printed.
#### Authorized:
```txt
print(), ft_print(), import sys, sys.stdout(), sys.stdout().flush()
```

### ft_input()
Create a function that receives a string and returns the user entry as an string.
#### Authorized:
```txt
import sys, sys.stdout(), sys.stdin()
```