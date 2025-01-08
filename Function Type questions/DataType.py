---
title : Check if a number is prime
---
# Problem statement

Write a function `is_prime(n)` that checks if a number `n` is prime number or not.

**Example**

```python
is_prime(7) # True , 7 is a prime number
is_prime(4) # False , 4 is not a prime number
is_prime(11) # True , 11 is a prime number
```


#Solution

```py3 test.py -r 'python test.py'
<prefix>
# some prefix
</prefix>
<template>
def is_prime(n: int) -> bool:
    '''
    Checks if a number is prime.

    Arguments:
    n: int - the number to check

    Return: bool - True if the number is prime, False otherwise.
    '''
    
    <los>...</los>
    <sol>
    if n <= 1:
        return False
    if n in (2,3):
        return True
    if n%2 == 0 or n%3 == 0:
        return False
    return all(n%i != 0 for i in range(5, int(n**0.5)+1 , 2))
    </sol>
    test = <los>...</los><sol>'test'</sol> #tests
</template>
<suffix>
#some suffix
</suffix>
<suffix_invisble>
{% include '../function_type_and_check.py.jinja'%}
</suffix_invisble>
```

# Public Test Cases

## Input 1
```
is_equal(
    is_prime(13),
    True
)

```

## Output 2
```
True
```

## Input 2

```
is_equal(
    is_prime(8),
    False
)
```

```
## Output 2
False
```

## Input 3
```
is_equal(
    is_prime(1),
    False
)
```

```
## Output 3
False
```


# Private Test Cases
## Input 1
```
is_equal(
    is_prime(29),
    True
)
```

```
## Output 1
True
```

## Input 2
```
is_equal(
    is_prime(15),
    False
)
```

```
## Output 2
False
```


## Input 3
```
is_equal(
    is_prime(2),
    True
```

```
## Output 3
True
```
## Input 4
```
is_equal(
    is_prime(0),
    False
```

```
## Output 3
False
```


