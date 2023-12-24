## Cheat Sheet

A cheat sheet of the commands I use most for Linux

### Bash Shortcuts

| Command    | Description                                          |
| :--------- | :--------------------------------------------------- |
| `Ctrl + R` | Search history                                       |
| `^abc^123` | Run the previous command, replacing `abc` with `123` |

### Directory Operations

| Operation | Options | Example            | Description             |
| :-------- | :------ | :----------------- | :---------------------- |
| `pwd`     |         | `mkdir <dir_name>` | Make a directory        |
| `mkdir`   |         |                    | Print working directory |
| `ls`      |         |                    | List files              |
|           | `-l`    |                    | Long listing format     |

### File Operations

| Operation | Example                 | Description                  |
| :-------- | :---------------------- | :--------------------------- |
| `touch`   | `touch <file>`          | Create file                  |
| `cat`     | `cat <file_1> <file_2>` | Concatenate files and output |

### Log Parsing Commands

🔍 **GREP** - Allow to search patterns in files. **ZGREP** for GZIP file.

```bash
grep <pattern> <file.log>
```

_Optional arguments:_

| Argument | Description                             |
| :------- | :-------------------------------------- |
| `-c`     | Count number of matches                 |
| `-E`     | Extended regex                          |
| `-i`     | Case insensitive                        |
| `-l`     | Find filenames that matches the pattern |
| `-n`     | Number of lines that matches            |
| `-v`     | Invert matches                          |

:scissors: **CUT** - Parse fields from delimited logs.

```bash
cut -d "." -f 2 <file.log>
```

_Optional arguments:_

| Argument | Description                   |
| :------- | :---------------------------- |
| `-c`     | Specifies characters position |
| `-d`     | Use the field delimiter       |
| `-f`     | The field number              |

🌊 **SED** (Stream Editor) - Replace strings in a file

```bash
sed s/regex/replace/g <filename>
```

_Optional arguments:_

| Argument | Description     |
| :------- | :-------------- |
| `d`      | Delete          |
| `g`      | Replace         |
| `s`      | Search          |
| `W`      | Append to file  |
| `-e`     | Execute command |
| `-n`     | Suppress output |

🛜 **NGREP** - Analyze network packets.

```bash
ngrep -I <file.pcap>
```

_Optional arguments:_

| Argument | Description                |
| :------- | :------------------------- |
| `-d`     | Specify network interface  |
| `-i`     | Case insensitive           |
| `-I`     | Recap pcap file            |
| `-t`     | Print timestamp            |
| `-X`     | Print in alternate hexdump |

### Other ones

| Command       | Description                                                |
| :------------ | :--------------------------------------------------------- |
| `echo $SHELL` | Which shell we are using within the terminal window        |
| `fg`          | Switch a job running in the background into the foreground |
| `which`       | Find out if file is actually present                       |
