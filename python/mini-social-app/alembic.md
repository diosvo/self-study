# Alembic

Initialize a new script directly:

```bash
alembic init <folder_name>
```

Create a new revision:

```bash
alembic revision -m "<message>"
```

Display the current revision for a database:

```bash
alembic current
```

Upgrade the specific revision:

```bash
alembic upgrade {<revision_id>,head}
```

Show current available heads in the script directory:

```bash
alembic heads
```