""" 
This module implements the SelectOperation class, 
which is responsible for selecting data from a table. 
"""
class SelectOperation:
    """
    This class is responsible for selecting data from a table.

    Attributes:
        None
    Methods:
    staticmethod execute: Selects data from a table.
    """
    @staticmethod
    def execute(database, table_name, columns=None, condition=None):
        """
        Selects data from a table.
        Args:
            database (Database): The database object.
            table_name (str): The name of the table.
            columns (list): A list with the columns to be selected.
            condition (function): A function that returns True if the row should be selected, False otherwise.
        Returns:
            list: A list with the selected data.
        """
        if table_name not in database.metadata:
            return "Error: Table doesn't exist"

        table = database.tables[table_name]
        rows = table.file_headler.read_all()
        result = []
        for row in filter(None, rows):
            row_dict = table.row_to_dict(row)
            if condition is None or condition(row_dict):
                if columns is None:
                    result.append(row_dict)
                else:
                    result.append(row_dict)
                    #result.append({col: row_dict[col] for col in columns if col in row_dict})
        return result