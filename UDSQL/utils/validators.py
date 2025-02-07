def validate_columns(columns):
    valid_types = ['int', 'float', 'str', 'bool']
    return all(isinstance(col, str) and typ in valid_types for col, typ in columns.items())

def validate_values(values, column_types):
    for col, val in values.items():
        if col not in column_types:
            return False
        try:
            if column_types[col] == 'int':
                int(val)
            elif column_types[col] == 'float':
                float(val)
            elif column_types[col] == 'bool':
                bool(val)
        except ValueError:
            return False
    return True