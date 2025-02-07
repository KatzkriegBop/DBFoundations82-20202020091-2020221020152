import pickle
import os
from UDSQL.utils.constants import METADATA_FILE

class metadataManager:
    @staticmethod
    def loadMetadata():
        if os.path.exists(METADATA_FILE):
            with open(METADATA_FILE, 'rb') as f:
                return pickle.load(f)
        return {}
    def saveMetadata(self, metadata):
        with open(metadata, 'wb') as f:
            pickle.dump(metadata,f) 