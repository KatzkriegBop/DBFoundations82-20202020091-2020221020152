""" This module implements the table class
which is responsible for managing a table.
"""
from utils.constants import FIELD_SEPARATOR
from utils.file_headler import FileHandler

class table:
    """
    This class is responsible for managing a table.

    Attributes:
        name (str): The name of the table.
        columns (dict): A dictionary with the columns of the table.
        file_headler (FileHandler): A FileHandler object.
    Methods:
        get_Headers: Returns the headers of the table.
        row_to_dict: Converts a row to a dictionary.
        dict_to_row: Converts a dictionary to a row.
        insert: Inserts a row in the table.
        select: Selects rows from the table.
        update: Updates rows in the table.
        delete: Deletes rows from the table.
        read_all_rows: Reads all rows from the table.
    """
    def __init__(self, name, columns):
        """
        The constructor for the table class.

        Args:
            name (str): The name of the table.
            columns (dict): A dictionary with the columns of the table.
        Returns:
            None
        """
        self.name = name
        self.columns = columns
        self.file_headler = FileHandler(f"{name}.txt")
    def get_Headers(self):
        """
        Returns the headers of the table.
        
        Args:
            self.columns (dict): A dictionary with the columns of the table.
        Returns:
            list: A list with the headers of the table.
            """
        return list(self.columns.keys())
    def row_to_dict(self, row):
        """
        Converts a row to a dictionary.
        
        Args:
            row (str): A string with the row.
        Returns:
            dict: A dictionary with the row.
            """
        values = FIELD_SEPARATOR.join(row).split(FIELD_SEPARATOR)
        return dict(zip(self.get_Headers(),values))
    def dict_to_row(self, row_dict):
        """
        Converts a dictionary to a row.

        Args:
            row_dict (dict): A dictionary with the row.
        Returns:
            str: A string with the row.
            """
        return FIELD_SEPARATOR.join(str(row_dict.get(col,'')) for col in self.get_Headers())
    def insert(self, values):
        """
        Inserts a row in the table.
        
        Args:
            values (dict): A dictionary with the values to be inserted.
        Returns:
            bool: True if the row was inserted, False otherwise.
        """
        try:
            row = FIELD_SEPARATOR.join(str(values[col]) for col in self.columns)  # Uses the field separator to join the values
            with open(self.file_headler.filename, 'a', encoding='utf-8') as f:
                f.write(row + '\n')  # Make sure to add a newline character
            return True
        except Exception as e:
            print(f"Error in insertion: {str(e)}")
            return False

    def select(self, columns=None, condition=None):
        """
        Selects rows from the table.
        
        Args:
            columns (list): A list with the columns to be selected.
            condition (function): A function that returns True if the row should be selected, False otherwise.
        Returns:
            list: A list with the selected data.
        """
        rows = self.file_headler.read_all()
        result = []
        for row in filter(None, rows):
            row_dict = self.row_to_dict(row)
            if condition is None or condition(row_dict):
                if columns is None:
                    result.append(row_dict)
                else:
                    result.append({col: row_dict[col] for col in columns if col in row_dict})
        return result
    def update(self, values, condition=None):
        """
        Updates rows in the table.
        
        Args:
            values (dict): A dictionary with the values to be updated.
            condition (function): A function that returns True if the row should be updated, False otherwise.
        Returns:
            str: A message with the number of updated logs.
        """
        rows = self.file_headler.read_all()
        updated_rows = []
        updates_count = 0
        for row in filter(None, rows):
            row_dict = self.row_to_dict(row)
            if condition is None or condition(row_dict):
                row_dict.update(values)
                updates_count += 1
            updated_rows.append(self.dict_to_row(row_dict))
        self.file_headler.write_all(updated_rows)
        return f"{updates_count} logs updated."
    def delete(self, condition=None):
        """
        Deletes rows from the table.

        Args:
            condition (function): A function that returns True if the row should be deleted, False otherwise.
        Returns:
            str: A message with the number of deleted logs.
        """
        rows = self.file_headler.read_all()
        kept_rows = []
        deleted_count = 0
        for row in filter(None, rows):
            row_dict = self.row_to_dict(row)
            if condition is None or not condition(row_dict):
                kept_rows.append(row)
            else:
                deleted_count += 1
        self.file_headler.write_all(kept_rows)
        return f"{deleted_count} logs deleted."
    def read_all_rows(self):
        """
        Reads all rows from the table.
        
        Args:
            self.file_headler (FileHandler): A FileHandler object.
        Returns:
            list: A list with the content of the file.
        """
        return self.file_headler.read_all()
    