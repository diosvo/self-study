# Docker

## 🔥 Docker Daemon (Host)

A background service responsible for managing Docker objects.

## 🧲 Docker Engine (Client)

Responsible for running and managing containers. Consists of the daemon, a REST API and a CLI.

## Components

### Images

- A read-only template for creating containers
- Contains application code, libraries, and dependencies.

### Container

- An instance of an image.
- A lightweight and standalone executable package that includes everything needed to run an application.

### Volumes

Allows data to persist outside of containers and to be shared between container instances.

### [Dockerfile](dockerfile/readme.md)

A script-like file that defines the steps to create a Docker image.
