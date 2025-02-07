from core.table import table
# from metadata import metadataManager
class CreateOperation:
    @staticmethod
    def execute(database,table_name,columns):
        if table_name in database.metadata:
            return "Error: Table already exists"
        database.metadata[table_name] = columns
        database.tables[table_name] = table(table_name,columns)
        database.save_metadata()
        database.tables[table_name].File_headler.write_headers(columns.keys())
        return "Table created succesfully"