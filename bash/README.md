## 📄 Curriculum

1. [Inception](docs/1-inception.md)

   **NOTE:**

   - [Cheat-sheet](./misc/cheat-sheet.md)
   - [Change permission files and ownership](./misc/permission.md)

   ### Shell Scripting Real-Time Scenarios

   Find:

   - Find and kill all the zombie processes.
   - First 10 biggest files in the file system and write the output to a file.
   - The files created and their sizes. It should accept the number of days as input. Or a from and to date format as inputs.

   Automate the process of:

   - Creating new user accounts on a Linux server and setting up their permissions and SSH access.
   - Rotating log files and compressing old files to save disk space.
   - Updating a list of servers with the latest security patches.

   Others:

   - Gracefully unmount a disk.
   - Send email.
   - Monitor CPU, Memory, and Disk usage send the output to a file in table format and send an alert if either of them exceeds a certain threshold.
   - List of users logged in by date and write it to an output file.
   - Copy files recursively to remote hosts.
   - Displays the number of failed login attempts by IP address and location.
   - Parses a log file and forwards a specific value with a timestamp to an output file.
   - Check the status of a list of URLs and send an email notification if any of them are down.

### Ensure you include the following concepts in the shell scripts you are writing:

1. Variable definitions

2. Use Log Parsing Commands

- **GREP** searches any given input files, selecting lines that match one or more patterns.
- **CUT** cuts out selected portions of each line from each file and writes them to the standard output.
- **SED** reads the specified files, modifying the input as specified by a list of commands.
- **AWK** scans each input file for lines that match any of a set of patterns.
- **SORT** sorts text and binary files by lines.
- **UNIQ** reads the specified input file comparing adjacent lines and writes a copy of each unique input line to the output file.

3. Handling Input/ Output / Error redirection.

4. Conditions/ If else statements

5. Case statement scripts.

6. Loops (For/Do-While)

7. Exist status

8. Command line arguments

## 🗞️ Blogs

- [How to Learn Linux Shell Scripting for DevOps](https://devopscube.com/linux-shell-scripting-for-devops/)

## 📚 Courses

📑

- [The Bash Guide](https://guide.bash.academy/)
- [How to Change File Permissions and Ownership in Linux](https://www.freecodecamp.org/news/linux-chmod-chown-change-file-permissions/)
- [Play with text in Linux: GREP, CUT, AWK, SED](https://blog.knoldus.com/play-with-text-in-linux-grep-cut-awk-sed/)

📹

Located at 🗂️ linux

- [Bash Scripting on Linux](https://www.youtube.com/playlist?list=PLT98CRl2KxKGj-VKtApD8-zCqSaN2mD4w)
- [Linux Crash Course](https://www.youtube.com/playlist?list=PLT98CRl2KxKHKd_tH3ssq0HPrThx2hESW)
