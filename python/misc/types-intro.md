# 🐍 [Python Types Intro](https://fastapi.tiangolo.com/python-types/)

Python has support for optional "**type hints**" (also called "type annotations"), which are special syntaxes that allow declaring the [type](## "e.g. string, int, float, bool") of a variable.

_e.g._

```python
def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + str(age)
    return name_with_age
```

## Declaring Types

> [!TIP]
> If we use Python 3.9+, we DO NOT have to `import <Type> from typing`. We can use the same regular `<Type>` type instead.

### Simple types:

For example:

- `int`

- `float`

- `bool`

- `bytes`

### Generic types with type parameters:

Some data structures can contain other values, like `dict`, `list` `set`, `tuple`.

> [!NOTE]
> Those internal types in the square brackets are called "**type parameters**".

#### List

```python
def process_items(items: list[str]):
    for item in items:
        print(item)
```

That means: "the variable `items` is a `list`, and each item in this list is a `str`".

#### Tuple ans Set

```python
def process_items(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s
```

This means:

- The variable `items_t` is a `tuple` with 3 items: an `int`, another `int`, and a `str`.

- The variable `items_s` is a `set`, and each item is of type `bytes`.

#### Dict

```python
def process_items(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name) # Key
        print(item_price) # Value
```

This means:

- The variable prices is a dict:

  - The keys are of type `str`.

  - The values are of type `float`.

#### Union

It can be of **several types**.

> From Python 3.10, we can use the [vertical bar (`|`)](## "also called bitwise or operator") to define unions of types.

```python
def process_item(item: int | str):
    print(item)
```

This means that `item` could be an `int` or a `str` in both cases.

#### Possibly `None`

A value could help a type, like `str`, but it could also be `None`.

```python
def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")
```

#### Using `Union` or `Optional`

- 🚨 Avoid using `Optional[SomeType]`

- Instead ✨ **use `Union[SomeType, None]`** ✨

Both are equivalent, and underneath, they are the same, but the word "**optional**" would seem to imply that the value is optional, meaning "it can be `None`", even if it's not optional and is still required.

### Classes as Types

Declare a class as the type of a variable.

_e.g._ Declare a class `Person`, with a name:

```python
class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name
```

This means that `one_person` is an **instance** of the class `Person`.

## Type Hints with Metadata Annotations

Allow putting **additional metadata** in these type hints using `Annotated`.

_e.g._

```python
from typing import Annotated


def say_hello(name: Annotated[str, "this is just metadata"]) -> str:
    return f"Hello {name}"
```

> [!TIP]
> The fact that this is standard Python means that we will still get the best possible developer experience in the editor, with the tools used to analyze and refactor the code, etc. ✨
> <br/> <br/>
> And the code will also be compatible with many other Python tools and libraries. 🚀
