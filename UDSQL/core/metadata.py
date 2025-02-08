"""
This file contains the metadataManager class which is responsible 
for loading and saving metadata.
"""
import pickle
import os
from utils.constants import METADATA_FILE

class metadataManager:
    """
    This class is responsible for loading and saving metadata.
    
    Attributes:
        None
    Methods:
        loadMetadata: Loads the metadata.
        saveMetadata: Saves the metadata"""
    @staticmethod
    def loadMetadata(): 
        """
        Loads the metadata.
        
        Args:
            METADATA_FILE (str): The metadata file.
        Returns:
            dict: A dictionary with the metadata.
        """
        if os.path.exists(METADATA_FILE):
            with open(METADATA_FILE, 'rb') as f:
                return pickle.load(f)
        return {}
    def saveMetadata(self, metadata):
        """
        Saves the metadata.
        
        Args:
            metadata (dict): A dictionary with the metadata.
        Returns:
            None
        """
        with open(METADATA_FILE, 'wb') as f:
            pickle.dump(metadata, f)