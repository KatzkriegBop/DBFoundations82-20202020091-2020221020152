from .constants import FIELD_SEPARATOR, ROW_SEPARATOR

class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def read_all(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                content = f.readlines()
                return [line.strip().split(ROW_SEPARATOR) for line in content if line.strip()]
        except FileNotFoundError:
            return []



    def write_headers(self, headers):
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write(FIELD_SEPARATOR.join(headers))

    def write_all(self, rows):
        with open(self.filename, 'w', encoding='utf-8') as f:
            for row in rows:
                print(row)
                f.write(row + '\n')
                #f.write(FIELD_SEPARATOR.join(row) + '\n')

    def append_row(self, row):
        current_content = self.read_all()
        current_content.append(row)
        self.write_all(current_content)
        return "Data inserted successfully"
    def deserialize(self, row):
        return row.split(FIELD_SEPARATOR)
