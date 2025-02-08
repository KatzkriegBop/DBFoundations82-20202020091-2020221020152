import cmd
from core.database import database
from operations.create import CreateOperation
from operations.insert import InsertOperation
from operations.select import SelectOperation
from operations.update import UpdateOperation
from operations.delete import DeleteOperation

class UDSQLShell(cmd.Cmd):
    intro = 'Bienvenido a UDSQL. Escribe help o ? para listar los comandos.\n'
    prompt = 'UDSQL> '

    def __init__(self):
        super().__init__()
        self.db = database()

    def do_exit(self, _):
        """Salir del programa."""
        print("¡Hasta luego!")
        return True

    def do_create(self, arg):
        """Crear una nueva tabla: CREATE nombre_tabla col1:tipo col2:tipo ..."""
        try:
            if not arg:
                print("Error: Must specify table name and columns")
                print("Usage: CREATE table_name col1:type col2:type ...")
                return
            parts = arg.split()
            if len(parts) < 2:
                print("Error: Must specify table name and columns")
                print("Usage: CREATE table_name col1:type col2:type ...")
                return
            table_name = parts[0]
            columns = {}
            for col in parts[1:]:
                try:
                    name, type_ = col.split(':')
                    if type_ not in ('int', 'str', 'float', 'bool'):
                        print(f"Error: Invalid type '{type_}'")
                        return
                    columns[name] = type_
                except ValueError:
                    print(f"Error: Invalid column definition '{col}'")
                    return
            print(CreateOperation.execute(self.db, table_name, columns))
        except ValueError as e:
            print(f"Value Error: {str(e)}")
            
    def do_insert(self, arg):
        """Insertar datos: INSERT nombre_tabla col1=valor1 col2=valor2 ..."""
        try:
            if not arg:
                print("Error: Must specify table name and values")
                print("Usage: INSERT table_name col1=value1 col2=value2 ...")
                return
            parts = arg.split()
            if len(parts) < 2:
                print("Error: Must specify table name and values")
                print("Usage: INSERT table_name col1=value1 col2=value2 ...")
                return
            table_name = parts[0]
            values = {}
            for pair in parts[1:]:
                try:
                    col, val = pair.split('=')
                    values[col] = val
                except ValueError:
                    print(f"Error: Invalid value pair '{pair}'")
                    return
            print(InsertOperation.execute(self.db, table_name, values))
        except ValueError as e:
            print(f"Value Error: {str(e)}")

    def do_select(self, arg):
        """Seleccionar datos: SELECT nombre_tabla [col1 col2 ...] [WHERE col=val]"""
        try:
            if not arg:
                print("Error: Must specify table name")
                print("Usage: SELECT table_name [col1 col2 ...] [WHERE col=val]")
                return
            parts = arg.split()
            table_name = parts[0]
            columns = []
            where_index = -1
            for i, part in enumerate(parts[1:],1):
                if part.upper() == 'WHERE':
                    where_index = i
                    break
            if where_index > 0:
                columns = parts[1:where_index]
            elif len(part) > 1:
                columns[part] = parts[1:]
            condition = None
            if where_index > 0 and where_index < len(parts) - 1:
                try:
                    where_expr = parts[where_index + 1]
                    col, val = where_expr.split('=')
                    condition = lambda row: str(row.get(col, '')) == val
                except ValueError:
                    print(f"Error: Invalid WHERE expression. Use 'WHERE col=val'")
                    return
            result = SelectOperation.execute(self.db, table_name, columns, condition)
            if isinstance(result, list):
                if result:  # Verifica si la lista no está vacía
                    for row in result:
                        print(row)
                else:
                    print("No se encontraron registros.")
            else:
                print(result)  # Imprime mensaje de error si `result` es un string
        except ValueError as e:
            print(f"Value Error: {str(e)}")
                
    def do_update(self, arg):
        """Actualizar datos: UPDATE nombre_tabla col1=valor1 col2=valor2 ... [WHERE col=val]"""
        try:
            if not arg:
                print("Error: Must specify table name and values")
                print("Usage: UPDATE table_name col1=value1 col2=value2 ... [WHERE col=val]")
                return
            parts = arg.split()
            if len(parts) < 2:
                print("Error: Must specify table name and values")
                print("Usage: UPDATE table_name col1=value1 col2=value2 ... [WHERE col=val]")
                return
            table_name = parts[0]
            values = {}
            where_index = -1
            for i, part in enumerate(parts[1:],1):
                if part.upper() == 'WHERE':
                    where_index = i
                    break
            for pair in parts[1:where_index] if where_index > 0 else parts[1:]:
                try:
                    col, val = pair.split('=')
                    values[col] = val
                except ValueError:
                    print(f"Error: Invalid value pair '{pair}'. Use 'col=val'")
                    return
            condition = None
            if where_index > 0 and where_index < len(parts) - 1:
                try:
                    where_expr = parts[where_index + 1]
                    col, val = where_expr.split('=')
                    condition = lambda row: str(row.get(col, '')) == val
                except ValueError:
                    print(f"Error: Invalid WHERE expression. Use 'WHERE col=val'")
                    return
                print(UpdateOperation.execute(self.db, table_name, values, condition))
        except ValueError as e:
            print(f"Value Error: {str(e)}")
    def do_delete(self, arg):
        """Eliminar datos: DELETE nombre_tabla [WHERE col=val]"""
        try:
            if not arg:
                print("Error: Must specify table name")
                print("Usage: DELETE table_name [WHERE col=val]")
                return
            parts = arg.split()
            table_name = parts[0]
            condition = None
            if len(parts) > 1:
                if parts[1].upper() == 'WHERE' and len(parts) > 2:
                    try:
                        where_expr = parts[2]
                        col, val = where_expr.split('=')
                        condition = lambda row: str(row.get(col, '')) == val
                    except ValueError:
                        print(f"Error: Invalid WHERE expression. Use 'WHERE col=val'")
                        return
                else:
                    print("Error: Invalid WHERE expression. Use 'WHERE col=val'")
                    return
            print(DeleteOperation.execute(self.db, table_name, condition))
        except ValueError as e:
            print(f"Value Error: {str(e)}")
if __name__ == '__main__':
    UDSQLShell().cmdloop()