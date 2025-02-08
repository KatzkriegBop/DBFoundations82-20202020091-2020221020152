# Authors: 
-Kevin Estiven Lozano Duarte-20221020152
-Juan David Quiroga-20222020206
-Juan Pablo Borja Espitia - 20202020091

# UDSQL - A Simple Database System

UDSQL is a simple database system that implements CRUD operations (Create, Read, Update, Delete) using a command-line interface (CLI). Tables are managed in text files, and data is stored in a structured format.

## Features

- Create tables with specific columns and types.
- Insert data into tables.
- Query data with filters.
- Update existing data in tables.
- Delete records from tables.
- The Datebase text file uses metadata

## Project Structure

The project is organized as follows:
        -UDSQL
            -CORE #This module is for the creation and configuration
                __init__.py
                database.py
                metadata.py
                table.py
            -OPERATIONS #This module is to perform all database operations. 
                __init__.py
                create.py
                delete.py
                insert.py
                select.py
                uptade.py
            -UTILS #This module is responsible for ensuring that the syntax is valid 
                __init__.py
                constant.py
                file_headler.py
                validators.py
            __init__.py
            main.py
        -Students.txt #This is explame of database created with UDSQL
        -README.md
