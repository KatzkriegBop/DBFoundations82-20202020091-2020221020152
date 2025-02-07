from ..utils.constants import FIELD_SEPARATOR
from ..utils.file_headler import FileHandler

class table:
    def __init__(self, name, columns):
        self.name = name
        self.columns = columns
        self.File_headler = FileHandler(f"{name}.txt")
    def get_Headers(self):
        return list(self.columns.keys())
    def row_to_dict(self, row):
        values = row.split("FILE_SEPARATOR")
        return dict(zip(self.get_Headers(),values))
    def dict_to_row(self, row_dict):
        return FIELD_SEPARATOR.join(str(row_dict.get(col,'')) for col in self.get_Headers())
    def insert(self, values):
        row = self.dict_to_row(values)
        self.File_headler.append_row(row)
        return "Datos insertados exitosamente"
    def select(self, columns=None, condition=None):
        rows = self.File_headler.read_all()
        result = []
        for row in filter(None, rows):
            row_dict = self.row_to_dict(row)
            if condition is None or condition(row_dict):
                if columns is None:
                    result.append(row_dict)
                else:
                    result.append({col: row_dict[col] for col in columns if col in row_dict})
        return result
    def update(self, values, condition=None):
        rows = self.File_headler.read_all()
        updated_rows = []
        updates_count = 0
        for row in filter(None, rows):
            row_dict = self.row_to_dict(row)
            if condition is None or condition(row_dict):
                row_dict.update(values)
                updates_count += 1
            updated_rows.append(self.dict_to_row(row_dict))
        self.File_headler.write_all(updated_rows)
        return f"Actualizados {updates_count} registros"
    def delete(self, condition=None):
        rows = self.File_headler.read_all()
        kept_rows = []
        deleted_count = 0
        for row in filter(None, rows):
            row_dict = self.row_to_dict(row)
            if condition is None or not condition(row_dict):
                kept_rows.append(row)
            else:
                deleted_count += 1
        self.File_headler.write_all(kept_rows)
        return f"Eliminados {deleted_count} registros"
    