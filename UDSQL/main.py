import cmd
from UDSQL.core.database import database
from UDSQL.operations.create import CreateOperation
from UDSQL.operations.insert import InsertOperation
from UDSQL.operations.select import SelectOperation
from UDSQL.operations.update import UpdateOperation
from UDSQL.operations.delete import DeleteOperation

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
            parts = arg.split()
            table_name = parts[0]
            columns = dict(col.split(':') for col in parts[1:])
            print(CreateOperation.execute(self.db, table_name, columns))
        except ValueError as e:
            print(f"Value Error: {str(e)}")
        except KeyError as e:
            print(f"Key Error: {str(e)}")
        except TypeError as e:
            print(f"Type Error: {str(e)}")
        except (AttributeError, IndexError) as e:
            print(f"Specific Error: {str(e)}")

    def do_insert(self, arg):
        """Insertar datos: INSERT nombre_tabla col1=valor1 col2=valor2 ..."""
        try:
            parts = arg.split()
            table_name = parts[0]
            values = dict(pair.split('=') for pair in parts[1:])
            print(InsertOperation.execute(self.db, table_name, values))
        except ValueError as e:
            print(f"Value Error: {str(e)}")
        except KeyError as e:
            print(f"Key Error: {str(e)}")
        except TypeError as e:
            print(f"Type Error: {str(e)}")
        except (AttributeError, IndexError) as e:
            print(f"Specific Error: {str(e)}")

    def do_select(self, arg):
        """Seleccionar datos: SELECT nombre_tabla [col1 col2 ...] [WHERE col=val]"""
        try:
            parts = arg.split()
            table_name = parts[0]
            columns = parts[1].split() if len(parts) > 1 else None
            condition = None
            if len(parts) > 2:
                col, val = parts[2].split('=')
                condition = lambda row: row[col] == val
            print(SelectOperation.execute(self.db, table_name, columns, condition))
        except ValueError as e:
            print(f"Value Error: {str(e)}")
        except KeyError as e:
            print(f"Key Error: {str(e)}")
        except TypeError as e:
            print(f"Type Error: {str(e)}")
        except (AttributeError, IndexError) as e:
            print(f"Specific Error: {str(e)}")
    def do_update(self, arg):
        """Actualizar datos: UPDATE nombre_tabla col1=valor1 col2=valor2 ... [WHERE col=val]"""
        try:
            parts = arg.split()
            table_name = parts[0]
            values = dict(pair.split('=') for pair in parts[1:])
            condition = None
            if len(parts) > 2:
                col, val = parts[2].split('=')
                condition = lambda row: row[col] == val
            print(UpdateOperation.execute(self.db, table_name, values, condition))
        except ValueError as e:
            print(f"Value Error: {str(e)}")
        except KeyError as e:
            print(f"Key Error: {str(e)}")
        except TypeError as e:
            print(f"Type Error: {str(e)}")
        except (AttributeError, IndexError) as e:
            print(f"Specific Error: {str(e)}")
    def do_delete(self, arg):
        """Eliminar datos: DELETE nombre_tabla [WHERE col=val]"""
        try:
            parts = arg.split()
            table_name = parts[0]
            condition = None
            if len(parts) > 1:
                col, val = parts[1].split('=')
                condition = lambda row: row[col] == val
            print(DeleteOperation.execute(self.db, table_name, condition))
        except ValueError as e:
            print(f"Value Error: {str(e)}")
        except KeyError as e:
            print(f"Key Error: {str(e)}")
        except TypeError as e:
            print(f"Type Error: {str(e)}")
        except (AttributeError, IndexError) as e:
            print(f"Specific Error: {str(e)}")
if __name__ == '__main__':
    UDSQLShell().cmdloop()