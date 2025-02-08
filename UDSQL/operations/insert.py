from core.database import table

class InsertOperation:
    @staticmethod
    def execute(database, table_name, values):
        if table_name not in database.tables:
            return "Error: Table doesn't exist"

        table = database.tables[table_name]

        # Check if the columns exist in the table
        table_columns = table.columns  # Asuming that the table has a property columns
        for col in values.keys():
            if col not in table_columns:
                return f"Error: Column '{col}' does not exist in table '{table_name}'"

        # Insert the values into the table
        success = table.insert(values)  # Asuming that the table has a method insert
        if success:
            return "Insert successful"
        return "Error: Insert failed"
