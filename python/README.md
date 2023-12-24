# 🌅 Roadmap

## [1. Learn the Basics](https://trello.com/c/EDFcfSj8/56-1-learn-the-basics)

### Lists, Tuples, Sets, and Dictionaries

- Lists

  - Like dynamically sized arrays.
  - Need NOT be homogeneous.

- Tuples

  - A collection of Python objects separated by commas.
  - In some ways, a tuple is similar to a list in terms of indexing, nested objects and repetition.

  > A tuple is immutable, unlike lists that are mutable.

- Sets

  - An unordered collection data type that is iterable, mutable, and has no duplicate elements.

- Dictionaries

  - An ordered (since Py 3.7) [unordered (Py 3.6 & prior)] collection of data values, is used to store data values like a map.

    > Data Types that hold only a single value as an element, <br/>
    > Dictionary holds key:value pair. Key-value is provided in the dictionary to make it more optimized.

## Hierarchy of Exception

```bash
Exception(*)
|
+-- SystemExit
+-- StandardError(*)
    |
    +-- KeyboardInterrupt
    +-- ImportError
    +-- EnvironmentError(*)
    |   |
    |   +-- IOError
    |   +-- OSError
    |       |
    |       +-- PermissionError
    |       +-- FileNotFoundError
    |
    +-- EOFError
    +-- ArithmeticError
    |   |
    |   +-- ZeroDivisionError
    |   +-- FloatingPointError
    |
    +-- RuntimeError
    |   |
    |   +-- NoImplementedError(*)
    |
    +-- ExceptionGroup
    +-- NameError
    +-- AttributeError
    +-- SyntaxError
    +-- TypeError
    +-- AssertionError
    +-- LookupError(*)
...
```

## Local Development

Python and pip are using

```bash
which python3
which pip3
```

Where is `site-packages` located at

```bash
python3 -m site
```

Show Debian-style package information

```bash
pip3 show <package_name>
```

## 📚 Courses

📑

- following [roadmap/python](https://roadmap.sh/python)
- [realpython](https://realpython.com/)

📹

Located at 🗂️ python/

- [Python Programming](https://www.youtube.com/playlist?list=PL_c9BZzLwBRLrHc6MntpdrNPKoC2tJr0z)
- [anthony explains](https://www.youtube.com/playlist?list=PLWBKAf81pmOaP9naRiNAqug6EBnkPakvY)
