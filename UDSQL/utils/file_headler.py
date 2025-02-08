"""
This module contains the FileHandler class, which is 
responsible for reading and writing data to a file.
"""
from .constants import FIELD_SEPARATOR, ROW_SEPARATOR
class FileHandler:
    """
    This class is responsible for reading and writing data to a file.
    Attributes:
        filename (str): The name of the file to be read or written.
    Methods:
        read_all: Reads all the content of the file.
        write_headers: Writes the headers of the file.
        write_all: Writes all the content of the file.
        append_row: Appends a row to the file.
        deserialize: Deserializes a row from the file
    """
    def __init__(self, filename):
        """
        The constructor for the FileHandler class.
        Args:
            filename (str): The name of the file to be read or written.
        Returns:
            None
        """
        self.filename = filename

    def read_all(self):
        """
        Reads all the content of the file.
        Args:
            self.filename (str): The name of the file to be read.
            read_all (str): The content of the file.
        Returns:
            list: A list with the content of the file.
        """
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                content = f.readlines()
                return [line.strip().split(ROW_SEPARATOR) for line in content if line.strip()]
        except FileNotFoundError:
            return []



    def write_headers(self, headers):
        """
        Writes the headers of the file.
        Args:
            headers (list): A list with the headers of the file.
        Returns:
            None
            """
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write(FIELD_SEPARATOR.join(headers))

    def write_all(self, rows):
        """
        Writes all the content of the file.
        Args:
            rows (list): A list with the content of the file.
        Returns:
            None
        """
        with open(self.filename, 'w', encoding='utf-8') as f:
            for row in rows:
                print(row)
                f.write(row + '\n')
                #f.write(FIELD_SEPARATOR.join(row) + '\n')

    def append_row(self, row):
        """
        Appends a row to the file.
        Args:
            row (list): A list with the row to be appended.
        Returns:
            str: A message indicating the success of the operation.
        """
        current_content = self.read_all()
        current_content.append(row)
        self.write_all(current_content)
        return "Data inserted successfully"
    def deserialize(self, row):
        """
        Deserializes a row from the file.
        Args:
            row (str): A string with the row to be deserialized.
        Returns:
            list: A list with the deserialized row."""
        return row.split(FIELD_SEPARATOR)
