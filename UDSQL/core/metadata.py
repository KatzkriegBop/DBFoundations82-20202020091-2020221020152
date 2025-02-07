import pickle
import os
from utils.constants import METADATA_FILE

class metadataManager:
    @staticmethod
    def loadMetadata():
        if os.path.exists(METADATA_FILE):
            with open(METADATA_FILE, 'rb') as f:
                return pickle.load(f)
        return {}
    def saveMetadata(metadata):
        with open(metadata, 'wb') as f:
            pickle.dump(metadata,f) 