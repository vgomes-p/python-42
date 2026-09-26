## INT MODULE
Create a class named `Integer`. The class must accept a string, float or bool. The class must have the following attributes: `squared`, `rooted`, `times`, `object`. The class must return the object.

Recreate and create the following integer-related methods according to the requirements below.

### class variables, initiation and return
Receive a string, float or bool and convert it to an integer. 

For `bool`:

- `True` must become `1`.
- `False` must become `0`.

For `float`:

- Round up when the decimal portion is greater than or equal to `0.5`.
- Round down otherwise.

Store the resulting integer in `self.object`. Set `self.times` to a list containing the multiplication table of the resulting integer from 1 to 10. Set `self.squared` to the squared value of the resulting integer. Set `self.rooted` to the square root of the resulting integer. The constructor must not return a value.
### Prototype example:
```py
def __init__(self, x: str | bool | float = 0) -> None:
```

#### Authorized:
```txt
None
```

### set()
Recreate the behavior of converting a value to an integer. Receive a string, bool or float and return an integer.

For `bool`:
- `True` must become `1`.
- `False` must become `0`.

For `float`:
- Round up when the decimal portion is greater than or equal to `0.5`.
- Round down otherwise.

#### Authorized:
```txt
None
```

### range()
Recreate the behavior of `range()` for the specified argument order. Receive a stop value and an optional start value. Create and return a list of integers starting at `start` and ending before `stop`. The start value must default to `0`. The arguments must follow this order:
```py
def range(stop: int, start: int = 0) -> list[int]:
```
#### Authorized:
```txt
None
```

### times()
Create a multiplication table for an integer. Receive an integer and return a list containing the multiplication results from 1 to 10.
#### Authorized:
```txt
None
```

### squared()
Create a function that returns the squared value of an integer. Receive an integer and return an integer.
#### Authorized:
```txt
None
```

### root()
Create a function that returns the square root of an integer. Receive an integer and return its square root. The behavior for values that are not perfect squares must be defined by the implementation requirements.
#### Authorized:
```txt
None
```

### sized()
Create a function that counts the number of digits in an integer. Receive an integer and return an integer.
#### Authorized:
```txt
None
```

### google()
Create a function that appends zeroes to an integer. Receive two integers. Return the first integer followed by the number of zeroes specified by the second integer.
*For example: `google(4, 5) → 400000`*
#### Authorized:
```txt
None
```

### is_valid_number()
Create a function that checks whether a `Value` represents a valid number. Receive a `Value` and return a `bool`. Return `True` for valid numbers and `False` otherwise. The implementation requirements must define which types and values are considered valid numbers.
#### Authorized:
```txt
None
```

### is_negative()
Create a function that checks whether a `Value` represents a valid negative number. Receive a `Value` and return a `bool`. Return `True` for valid negative numbers and `False` otherwise.
#### Authorized:
```txt
None
```

## FLOAT MODULE
UNDER CONSTRUCTION