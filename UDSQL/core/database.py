from UDSQL.core.metadata import metadataManager
from UDSQL.core.table import table

class database:
    def __init__(self):
        self.metadata = metadataManager.loadMetadata()
        self.tables = {}
        self.load_tables()
    def load_tables(self):
        for table_name,columns in self.metadata.items():
            self.tables[table_name] = table(table_name,columns)
    def save_metadata(self):
        metadataManager().saveMetadata(self.metadata)
