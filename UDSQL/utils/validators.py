"""
This module implements a  UDSQL validator for UDSQLshell
it is used to validate the columns and values of a table.
"""
def validate_columns(columns):
    """
    Validates the columns of a table.
    Args:
        columns (dict): A dictionary with the columns of a table.
    Returns:
        bool: True if the columns are valid, False otherwise.
    """
    valid_types = {'int', 'float', 'str', 'bool'}
    return all(isinstance(col, str) and typ in valid_types for col, typ in columns.items())

def validate_values(values, column_types):
    """
    Validates the values of a table.
    Args:
        values (dict): A dictionary with the values of a table.
        column_types (dict): A dictionary with the types of the columns.
    Returns:
        bool: True if the values are valid, False otherwise.
    """
    for col, val in values.items():
        if col not in column_types:
            return False
        try:
            expected_type = column_types[col]
            if expected_type == 'int':
                int(val)  # Tries to convert it to integer
            elif expected_type == 'float':
                float(val)  # Tried to convert it to float
            elif expected_type == 'bool':
                if str(val).lower() not in {"true", "false", "1", "0"}:
                    return False
            elif expected_type == 'str':
                if not isinstance(val, str):  # Must be a string
                    return False
        except ValueError:
            return False
    return True
