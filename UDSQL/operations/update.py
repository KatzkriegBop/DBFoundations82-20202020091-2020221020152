class UpdateOperation:
    @staticmethod
    def execute(database, table_name, values, condition=None):
        if table_name not in database.metadata:
            return "Error: La tabla no existe"

        table = database.tables[table_name]
        rows = table.file_headler.read_all()
        updated_rows = []
        updates_count = 0

        for row in filter(None, rows):
            row_dict = table.row_to_dict(row)
            
            if condition is None or condition(row_dict):
                row_dict.update(values)
                updates_count += 1
            
            updated_rows.append(table.dict_to_row(row_dict))

        table.file_headler.write_all(updated_rows)
        return f"Actualizados {updates_count} registros"