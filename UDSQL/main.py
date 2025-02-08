"""
Main menu module for UDSQL.

This module contains the necessary functions to display an interactive menu and manage user selections for a Game Console.
and manage user selections for a Game Console.

AUTHORS: Kevin Estiven Lozano Duarte <kelozanod@udistrital.edu.co>
            Juan David Quiroga <jdquirogag@udistrital.edu.co>
            Juan Pablo Borja Espitia <jpborjae@udistrital.edu.co>


This file is part of WORKSHOPNo3.

WORKSHOPNo3 is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation,
either version 3 of the License, or (at your option) any later version.

WORKSHOPNo3 is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with WORKSHOPNo1. If not, see <https://www.gnu.org/licenses/>.

"""
import cmd
from core.database import database
from operations.create import CreateOperation
from operations.insert import InsertOperation
from operations.select import SelectOperation
from operations.update import UpdateOperation
from operations.delete import DeleteOperation

class UDSQLShell(cmd.Cmd):
    
    """UDSQL Shell Class to manage the shell commands

    Attributes: 
        intro (str): Welcome message
        prompt (str): Command prompt
        db (database): Database object
    Methods:
        do_exit: Exit program
        do_create: Create a new table
        do_insert: Insert data
        do_select: Select data
        do_update: Update data
        do_delete: Delete data
    """
    intro = 'Welcome to UDSQL. Type help or "?" to list the commands.\n'
    prompt = 'UDSQL> '

    
    def __init__(self):
        """Constructor"""
        super().__init__()
        self.db = database()

    def do_exit(self, _):
        """Exit program
        
        Usage: exit
        Output: Goodbye message
        """
        print("¡See you next time!")
        return True

    def do_create(self, arg):
        """Create a new table.

        Args:
            arg (str): Table name and columns
            arg format: table_name col1:type col2:type ...
        Returns:
            str: Success message
        Usage: CREATE table_name col1:type col2:type ...
        """
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
        """Insert data into a table.

        Usage: INSERT table_name col1=value1 col2=value2 ...
            arg (str): Table name and values
            arg format: table_name col1=value1 col2=value2 ...
        Returns:
            str: Success message
        """
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
        """Retrieve data from a table.

        Usage: SELECT table_name [col1 col2 ...] [WHERE col=val]
        Args:
            arg (str): Table name and columns
            arg format: table_name [col1 col2 ...] [WHERE col=val]
            arg example: logs timestamp message WHERE level=INFO
        Returns:
            str: Success message
            str: Error message
        """
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
                if result:  # Verifies if list is not empty
                    for row in result:
                        print(row)
                else:
                    print("No logs found.")
            else:
                print(result)  # Prints result message
        except ValueError as e:
            print(f"Value Error: {str(e)}")
                
    def do_update(self, arg):
        """Update data: UPDATE table_name col1=value1 col2=value2 ... [WHERE col=val]

        Args:
            arg (str): Table name and values
            arg format: table_name col1=value1 col2=value2 ... [WHERE col=val]
            arg example: logs message=NewMessage WHERE level=INFO
        Returns:
            str: Success message
            str: Error message
        """
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
        """Delete data from a table.

        Usage: DELETE table_name [WHERE col=val]
        Args:
            arg (str): Table name and values
            arg format: table_name [WHERE col=val]
            arg example: logs WHERE level=INFO
        Returns:
            str: Success message
            str: Error message
        """
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