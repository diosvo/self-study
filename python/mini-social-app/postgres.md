# 🗄️ Postgres

- Each instance of Postgres can be carved into multiple separate databases.
- By default, every Postgres installation comes with one database already created called "Postgres".
- This is important because Postgres requires you to specify the name of a database to make a connection. So there needs to always be one database.

**NOTE**:

A default database cluster with:

```bash
initdb --locale=C -E UTF-8 /opt/homebrew/var/postgresql@16
```

Need to have postgresql@16 first in your PATH, run:

```bash
echo 'export PATH="/opt/homebrew/opt/postgresql@16/bin:$PATH"' >> ~/.zshrc
```

For compilers to find postgresql@16, need to set:

```bash
export LDFLAGS="-L/opt/homebrew/opt/postgresql@16/lib"
export CPPFLAGS="-I/opt/homebrew/opt/postgresql@16/include"
```

To start postgresql@16 now and restart at login:

```bash
brew services start postgresql@16
```

Or, if you don't want/need a background service you can just run:

```bash
LC_ALL="C" /opt/homebrew/opt/postgresql@16/bin/postgres -D /opt/homebrew/var/postgresql@16
```

## Tables & Schema Basics

1. Table

   Represents a subject or event in an application.

2. Columns & Rows

   - A table is made up of columns and rows.
   - Each column represents a different attribute.
   - Each row represents a different entry in the table.

3. DataTypes

   | Data Type | Postgres                | Python     |
   | :-------- | :---------------------- | :--------- |
   | Numeric   | int, decimal, precision | int, float |
   | Text      | varchar, text           | string     |
   | Boolean   | boolean                 | bool       |
   | Sequence  | array                   | list       |

4. Primary Key

   - Is a column or group of columns that uniquely identifies each row in a table.
   - The table can have one and only one PK. The PK does NOT have to be the ID column. It's up to you to decide which column uniquely defines each record.

5. Unique Constraints

   - A UNIQUE constraint can be applied to any column to make sure every record has <u>a
     unique value</u> for that column.

6. Null Constraints

   - By default, when adding a new entry to a database, any column can be left blank. When <u>a column is left blank</u>, it has a null value.
   - If you need column to be properly filled in to create a new record, a NOT NULL constraint can be added to the column to ensure that the column is never left blank.
