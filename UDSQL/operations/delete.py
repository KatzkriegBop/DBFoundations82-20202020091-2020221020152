""" 
This Module implements the DeleteOperation class, which 
is responsible for deleting data from a table. 
"""
class DeleteOperation:
    """
    This class is responsible for deleting data from a table.
    Attributes:
        None
    Methods:
    staticmethod execute: Deletes data from a table.
    """
    @staticmethod
    def execute(database, table_name, condition=None):
        """
        Deletes data from a table.
        Args:
            database (Database): The database object.
            table_name (str): The name of the table.
            condition (function): A function that returns True if the row should be deleted, False otherwise.
        Returns:
            str: A message with the number of deleted logs.
            str: A message if there are no logs to delete.
            error: A message if the table doesn't exist.
        """
        if table_name not in database.metadata:
            return "Error: Table doesn't exist"

        table = database.tables[table_name]
        rows = table.file_headler.read_all()
        kept_rows = []
        deleted_count = 0

        for row in filter(None, rows):
            row_dict = table.row_to_dict(row)
            
            if condition is None or not condition(row_dict):
                kept_rows.append(table.dict_to_row(row_dict))
            else:
                deleted_count += 1
        if kept_rows:
            table.file_headler.write_all(kept_rows)
            return f"{deleted_count} logs deleted."
        else:
            return "No logs to delete."