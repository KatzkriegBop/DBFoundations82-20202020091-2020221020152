""" 
This module implements the CreateOperation class,
which is responsible for creating a table.
"""
from core.table import table
class CreateOperation:
    """
    This class is responsible for creating a table.
    Attributes:
        None
    Methods:
        staticmethod execute: Creates a table."""
    @staticmethod
    def execute(database,table_name,columns):
        """
        Creates a table.
        Args:
            database (Database): The database object.
            table_name (str): The name of the table.
            columns (dict): A dictionary with the columns of the table.
        Returns:
            str: A message if the table was created successfully.
            str: A message if the table already exists.
            error: A message if the table doesn't exist.
        """
        if table_name in database.metadata:
            return "Error: Table already exists"
        database.metadata[table_name] = columns
        database.tables[table_name] = table(table_name,columns)
        database.save_metadata()
        database.tables[table_name].File_headler.write_headers(columns.keys())
        return "Table created succesfully"