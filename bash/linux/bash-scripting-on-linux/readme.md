## 📄 Outline <sup>[Bash Scripting on Linux](https://www.youtube.com/playlist?list=PLT98CRl2KxKGj-VKtApD8-zCqSaN2mD4w)</sup>

- Class 01: Introduction & Welcome
- [Class 02](2-hello-world): Hello World
- [Class 03](3-variables): Variables
- [Class 04](4-math-functions): Math Functions
- [Class 05](5-if-statements): If Statements
- [Class 06](6-exist-codes): Exit Codes
- [Class 07](7-while-loops): While Loops
- [Class 08](8-universal-update-script): Universal Update Script
- [Class 09](9-loops): For Loops
- Class 10: Filesystem Locations for Scripts (_pending_)
- Class 11: Data Streams
- Class 12: Function
- Class 13: Case Statements
- Class 14: Scheduling Jobs (Part 1)
- Class 15: Scheduling Jobs (Part 2)
- Class 16: Arguments
- Class 17: Creating a Backup Script
- Class 18: Closing

## 💣 Details

_The details are only applicable to certain lessons._

### Class 03: Variables

- One of the reasons why we include a dollar sign in front of the variable name?

  -> Help us avoid name collisions

  ```bash
  $ ls="Hello Again"
  $ ls
  > ... # print list files in current working directory
  $ echo $ls
  > Hello Again
  ```

- Any variables in bash are tied to that session will be wiped out once you close the window (e.g. type `exit`)
- We use double quotes in bash, it's going to treat the variables inside the `echo` statement to show what the variables equal rather than the names themselves.
- Sub-shell (e.g. `$(pwd)`) allows you to execute the command in the background.
- Within the environment, many default variables are always declared (e.g. `$USER`). Type `env` to view the environment variables within the Linux system.
- Lowercase and uppercase variable names have an important distinction:
  - Uppercase: is commonly a system variable, something that's built-in.
  - Lowercase: our variables.

### Class 04: Math Functions

We can type `man test` to get all expressions that could be used.

| Syntax                | Description                                        |
| :-------------------- | :------------------------------------------------- |
| 1. Numeric Comparison |
| `-eq`                 | Equal                                              |
| `-ne`                 | Not equal                                          |
| `-gt`                 | Greater than                                       |
| 2. Files              |                                                    |
| `-f` / `-d`           | A check for the existence of files and directories |
| `command -v $package` | Check for the existence of a command               |

### Class 06: Exit Codes

- `ls -l /misc` - Bash perceives success and failure
- `$?` - Check the `$?` variable to determine a command's exit code, returns:

  - `0` - the command was successful
  - An exit code of anything other than zero constitutes failure
