from .constants import FIELD_SEPARATOR, ROW_SEPARATOR

class FileHandler:
    def __init__(self, filename):
        self.filename = filename

def read_all(self):
    try:
        with open(self.filename, 'r', encoding='utf-8') as f:
            content = f.read().strip()  # Asegurar que es string y sin espacios extras
            if not content:
                return []
            
            # Si el archivo no está vacío, dividir por ROW_SEPARATOR
            rows = content.split(ROW_SEPARATOR)
            deserialized_rows = [self.deserialize(row) for row in rows]
            
            print(f"Datos leídos desde {self.filename}: {deserialized_rows}")  # Debug
            return deserialized_rows
    except FileNotFoundError:
        return []


    def write_headers(self, headers):
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write(FIELD_SEPARATOR.join(headers))

    def write_all(self, rows):
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write(ROW_SEPARATOR.join(rows))

    def append_row(self, row):
        current_content = self.read_all()
        current_content.append(row)
        self.write_all(current_content)
        return "Data inserted successfully"
