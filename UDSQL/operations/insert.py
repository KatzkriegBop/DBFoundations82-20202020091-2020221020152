from core.database import table

class InsertOperation:
    @staticmethod
    def execute(database, table_name, columns=None, condition=None):
        if table_name not in database.metadata:
            return "Error: Table doesn't exist"

        table = database.tables[table_name]
        rows = table.read_all_rows()
        result = []

        for row in filter(None, rows):
            row_dict = table.row_to_dict(row)
            
            if condition is None or condition(row_dict):
                if columns is None:
                    result.append(row_dict)
                else:
                    result.append({col: row_dict[col] for col in columns if col in row_dict})

        return result