# [Dockerfile](https://docs.docker.com/engine/reference/builder/)

## Overview

The Dockerfile supports the following instructions:

| Instruction   | Description                                                 |
| :------------ | :---------------------------------------------------------- |
| `ADD`         | Add local or remote files and directories.                  |
| `ARG`         | Use build-time variables.                                   |
| `CMD`         | Specify default commands.                                   |
| `COPY`        | Copy files and directories.                                 |
| `ENTRYPOINT`  | Specify default executable.                                 |
| `ENV`         | Set environment variables.                                  |
| `EXPOSE`      | Describe which ports the application is listening on.       |
| `FROM`        | Create a new build stage from a base image.                 |
| `HEALTHCHECK` | Check a container's health on startup.                      |
| `LABEL`       | Add metadata to an image.                                   |
| `MAINTAINER`  | Specify the author of an image.                             |
| `ONBUILD`     | Specify instructions for when the image is used in a build. |
| `RUN`         | Execute build commands.                                     |
| `SHELL`       | Set the default shell of an image.                          |
| `STOPSIGNAL`  | Specify the system call signal for existing a container.    |
| `USER`        | Set user and group ID.                                      |
| `VOLUME`      | Create volume mounts.                                       |
| `WORKDIR`     | Change working directory.                                   |

## Format

Here is the format of the Dockerfile:

```bash
# Comment
INSTRUCTION arguments
```

_Where,_

- INSTRUCTION - is not case-sensitive and it should be uppercase.
- arguments - Execute commands using Linux.

**NOTE**:

- Docker runs instructions in a Dockerfile in order.
- Must begin with a `FROM` instruction.
