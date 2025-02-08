# Authors: 
- Kevin Estiven Lozano Duarte-20221020152
- Juan David Quiroga-20222020206
- Juan Pablo Borja Espitia - 20202020091

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

UDSQL/ │ ├── CORE/ # This module is for the creation and configuration of the database system │ ├── init.py │ ├── database.py # Contains the logic for handling tables and database operations │ ├── metadata.py # Handles the metadata information of the database │ └── table.py # Defines table structure and data handling │ ├── OPERATIONS/ # This module is responsible for performing all the database operations │ ├── init.py │ ├── create.py # Handles table creation │ ├── delete.py # Responsible for deleting records from the database │ ├── insert.py # Handles inserting data into tables │ ├── select.py # Responsible for querying and selecting data │ ├── update.py # Handles updating existing data in tables │ ├── UTILS/ # This module ensures syntax validation and other utility functions │ ├── init.py │ ├── constant.py # Contains constant values used throughout the project │ ├── file_handler.py # Responsible for reading and writing files │ └── validators.py # Contains functions to validate user inputs and data │ ├── init.py # Marks the root directory of the UDSQL package └── main.py # Main entry point to run the UDSQL shell

Students.txt # An example of a database created with UDSQL README.md # Project documentation file