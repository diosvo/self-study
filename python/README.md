# 🐍 Python

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

Download `get-pip.py`:

```bash
curl -sSL https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

Python and `pip` are using:

```bash
which python3
which pip3
```

Where is `site-packages` located at:

```bash
python3 -m site
```

Show Debian-style package information:

```bash
pip3 show <package_name>
```

## Virtual environment

Download the virtual environment package:

```bash
sudo pip install virtualenv
```

Create a virtual environment:

```bash
virtualenv env
```

Access the virtual environment:

```bash
source env/bin/activate
```

> Exit the virtual environment with `deactivate` command

Install necessary packages after accessing to the virtual env.

## 📚 Courses

📑

- [roadmap/python](https://roadmap.sh/python)
- [realpython](https://realpython.com/)

📹

Located at 🗂️ python/

- [Mini Social Application](mini-social-app/)
- [NeuralNine](https://www.youtube.com/@NeuralNine)
- [Python Programming](https://www.youtube.com/playlist?list=PL_c9BZzLwBRLrHc6MntpdrNPKoC2tJr0z)
