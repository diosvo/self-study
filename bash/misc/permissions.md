# Linux Permissions

## Permissions Types

`r` - Read. Can read a file, or list the contents of a directory.

`w` - Write. A file or the contents of a directory can be modified.

`x` - Execute. A file can be run as a program or a directory can be entered.

## User Types

`u` - User. The owner of the file or directory.

`g` - Group. Other users who are members of the file's group.

`o` - Others. All other users who aren't the owner or part of the group.

## Viewing permissions

Permissions can be viewed with the `ls -l` command, which returns a string if 10 characters.

_e.g._

```bash
$ ls -l

-rw-r--r--   1 diosvo  staff    0 Oct  3 17:14 README.md
```

| Character  | Note              |
| :--------- | :---------------- |
| `d` or `-` | Directory or File |
| `rw-`      | User (owner)      |
| `r--`      | Group             |
| `r--`      | Others            |

## Change Permissions

### chmod

Changes <u>permissions</u> using symbolic or numeric modes.

```bash
chmod <permissions> <filename>
```

#### Symbolic

Defines [a target](## "User Types") (u/g/o), action, and [permissions](## "Permissions Types") (r/w/x).

| Action | Description |
| :----- | :---------- |
| `+`    | Add         |
| `-`    | Remove      |
| `=`    | Set         |

_e.g._

```bash
chmod u+x <filename>
```

#### Numeric

Uses the octal numbering system, which uses digits 0-7

| Number | Permission            | Presentation |
| :----: | :-------------------- | :----------: |
|   0    | None                  |    `---`     |
|   1    | Execute only          |    `--x`     |
|   2    | Write only            |    `-w-`     |
|   3    | Write & Execute       |    `-wx`     |
|   4    | Read only             |    `r--`     |
|   5    | Read & Execute        |    `r-x`     |
|   6    | Read & Write          |    `rw-`     |
|   7    | Read, Write & Execute |    `rwx`     |

_e.g._

```bash
chmod 600 <filename>
```

### chown

Change <u>the owner</u> of a file or directory.

| Description                             | For examples                      |
| :-------------------------------------- | :-------------------------------- |
| User only                               | `chown <user> <filename>`         |
| User and group ownership simultaneously | `chown <user>:<group> <filename>` |
| Directory ownership                     | `chown -R <user> <dir>`           |
| Group ownership                         | `chown :<group> <filename>`       |

### chgrp

Changes <u>the group</u> of a file or directory.

_e.g._

```bash
chgrp <group> <filename>
```
