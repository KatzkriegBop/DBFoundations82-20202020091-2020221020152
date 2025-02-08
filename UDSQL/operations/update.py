"""
This module implements the UpdateOperation class, which is 
responsible for updating the data in a table.
"""
class UpdateOperation:
    """
    This class is responsible for updating the data in a table.

    Attributes:
        None
    Methods:
        staticmethod execute: Updates the data in a table.
    """
    @staticmethod
    def execute(database, table_name, values, condition=None):
        """
        Updates the data in a table.
        Args:
            database (Database): The database object.
            table_name (str): The name of the table.
            values (dict): A dictionary with the values to be updated.
            condition (function): A function that returns True if the row should be updated, False otherwise.
        Returns:
            str: A message with the number of updated logs.
        """
        if table_name not in database.metadata:
            return "Error: Table doesn't exist"

        table = database.tables[table_name]
        rows = table.file_headler.read_all()
        updated_rows = []
        updates_count = 0

        for row in filter(None, rows):
            row_dict = table.row_to_dict(row)
            
            if condition is None or condition(row_dict):
                row_dict.update(values)
                updates_count += 1
            
            updated_rows.append(table.dict_to_row(row_dict))

        table.file_headler.write_all(updated_rows)
        return f"{updates_count} updated logs"