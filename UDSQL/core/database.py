"""
This module contains the database class which 
is the main class of the UDSQL package.

"""
from .metadata import metadataManager
from .table import table
class database:
    """
    This class is responsible for managing the database.

    Attributes:
        metadata (dict): A dictionary with the metadata of the database.
        tables (dict): A dictionary with the tables of the database.
    Methods:
        load_tables: Loads the tables of the database.
        save_metadata: Saves the metadata of the database.
    """
    def __init__(self):
        """
        The constructor for the database class.
        
        Args:
            Self.metadata (dict): A dictionary with the metadata of the database.
            Self.tables (dict): A dictionary with the tables of the database.
            Self.load_tables: Loads the tables of the database.
        Returns:
            None
        """
        self.metadata = metadataManager.loadMetadata()
        self.tables = {}
        self.load_tables()
    def load_tables(self):
        """
        Loads the tables of the database.
        
        Args:
            self.metadata (dict): A dictionary with the metadata of the database.
            self.tables (dict): A dictionary with the tables of the database.
        Returns:
            None
        """
        for table_name,columns in self.metadata.items():
            self.tables[table_name] = table(table_name,columns)
    def save_metadata(self):
        """
        Saves the metadata of the database.
        
        Args:
            self.metadata (dict): A dictionary with the metadata of the database.
        Returns:
            None"""
        metadataManager().saveMetadata(self.metadata)
