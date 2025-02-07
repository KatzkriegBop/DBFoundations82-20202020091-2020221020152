from core.database import table

class InsertOperation:
    @staticmethod
    def execute(database, table_name, values):
        if table_name not in database.tables:
            return "Error: Table doesn't exist"

        table = database.tables[table_name]

        # Validar que las columnas existen en la tabla
        table_columns = table.columns  # Asumiendo que la tabla tiene un atributo 'columns'
        for col in values.keys():
            if col not in table_columns:
                return f"Error: Column '{col}' does not exist in table '{table_name}'"

        # Insertar la nueva fila
        success = table.insert(values)  # Asumiendo que la tabla tiene un método insert()
        if success:
            return "Insert successful"
        return "Error: Insert failed"
