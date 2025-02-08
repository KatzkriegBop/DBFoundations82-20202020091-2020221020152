class DeleteOperation:
    @staticmethod
    def execute(database, table_name, condition=None):
        if table_name not in database.metadata:
            return "Error: Table doesn't exist"

        table = database.tables[table_name]
        rows = table.file_headler.read_all()
        kept_rows = []
        deleted_count = 0

        for row in filter(None, rows):
            row_dict = table.row_to_dict(row)
            
            if condition is None or not condition(row_dict):
                kept_rows.append(table.dict_to_row(row_dict))
            else:
                deleted_count += 1
        if kept_rows:
            table.file_headler.write_all(kept_rows)
            return f"{deleted_count} logs deleted."
        else:
            return "No logs to delete."