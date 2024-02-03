# Mini Social Application

## 🌟 Recap _<sup>Start learning FastAPI</sup>_

**DO** with standard modern Python (3.8+) types.

**DO NOT** have to learn the new syntax, the methods or classes of a specific library, etc.

With a single declaration:

1. Editor support, including:

   - Completion.
   - Type checks.

2. Validation of data:

   - Automatic and clear errors when the data is invalid.
   - Validation even for deeply nested JSON objects.

3. [Conversion](## "aka: serialization, parsing, and marshaling") of input data: coming from the network to Python data and types. Reading from:

   - JSON.
   - Path Parameters.
   - Query Parameters.
   - Cookies.
   - Headers.
   - Forms.
   - Files.

4. [Conversion](## "aka: serialization, parsing, and marshaling") of output data: converting from Python data and types to network data (as JSON):

   - Convert Python types (`str`, `int`, `float`, `bool`, `list`, etc).
   - `datetime` objects.
   - `UUID` objects.
   - Database models.

     ...

5. Automatic interactive API documentation, including 2 alternative user interfaces:

   - Swagger UI - 127.0.0.1:8000/docs
   - ReDoc - 127.0.0.1:8000/redoc

## 👀 Details

To start a project:

```bash
uvicorn app.main:app --reload
```

### 👾 Tutorial - User Guide

#### Includes:

- Declaration of **parameters**: headers, cookies, form fields and files.
- **Validation** Constraints: `maximum_length`, `regex`.
- A very powerful and easy-to-use [**Dependency Injection**](## "aka: components, resources, providers, services, injectable") system.
- Security and authentication, including support for **OAuth2** with **JWT tokens** and **HTTP Basic** Authentication.
- More advanced (but equally easy) techniques for declaring **deeply nested JSON models**.
- **GraphQL** integration with [Strawberry](https://strawberry.rocks/) and other libraries.
- Many extra features as:

  - **WebSockets**
  - Extremely easy tests based on HTTPX and pytest
  - **CORS**
  - **Cookie Sessions**

    ...

### 🚨 NOTEs:

API Path order matters!

#### ❓ Why do need Schema

- It's a pain to get all the values from the body.
- The client can send whatever data they want.
- The data isn't getting validated.
- We ultimately want to force the client to send the data in a schema that we expect.

#### ❓ What is a database

- Database is a collection of organized data that can be easily accessed and managed.
- We do not work or interact with databases directly. Instead, we make use of software referred to as a Database Management System (**DMBS**):

  1. [Relational Databases](## "MySQL, PostgreSQL, Oracle, SQL Server.") & [Structured Query Language](## "Language used to communicate with DBMS.") - Read [Postgres](postgres.md) for more details.

  2. [NoSQL](## "MongoDB, DynamoDB, Oracle, SQL Server.")

#### ❓ What is Object Relational Mapper (ORM)

- Layer of abstraction that sits between the database and us.
- We can perform all database operations through traditional Python code. No more SQL!

## 📚 References

- [Learn section](https://fastapi.tiangolo.com/learn/) - @official-page
- [FastAPI + Testing + Deployment + CI/CD](https://www.youtube.com/playlist?list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM) - @SanjeevThiyagarajan
