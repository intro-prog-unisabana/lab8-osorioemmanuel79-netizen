"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md
import sys
from todo_manager import read_todo_file, write_todo_file

def main():
    try:
        if len(sys.argv) < 2:
            raise IndexError("Insufficient arguments provided!")

        # HELP
        if sys.argv[1] == "--help":
            print("""Usage: python main.py <file_path> <command> [arguments]...

Commands:
  add "task"    - Add a task to the list.
  remove "task" - Remove a task from the list.
  view          - Display all tasks.

Examples:
  python main.py tasks.txt add "Buy groceries"
  python main.py tasks.txt remove "Do laundry"
  python main.py tasks.txt view
  python main.py tasks.txt add "Call mom" remove "Take out trash" view""")
            return

        file_path = sys.argv[1]
        tasks = read_todo_file(file_path)

        i = 2  # empezar desde el comando

        while i < len(sys.argv):
            command = sys.argv[i]

            if command == "add":
                if i + 1 >= len(sys.argv):
                    raise IndexError('Task description required for "add".')

                task = sys.argv[i + 1]
                tasks.append(task)
                print(f'Task "{task}" added.')
                i += 2

            elif command == "remove":
                if i + 1 >= len(sys.argv):
                    raise IndexError('Task description required for "remove".')

                task = sys.argv[i + 1]
                try:
                    tasks.remove(task)
                    print(f'Task "{task}" removed.')
                except ValueError:
                    print(f'Task "{task}" not found.')
                i += 2

            elif command == "view":
                print("Tasks:")
                for task in tasks:
                    print(task)
                i += 1

            else:
                raise ValueError("Command not found!")

        # Guardar SOLO una vez
        write_todo_file(file_path, tasks)

    except (IndexError, ValueError) as e:
        print(e)

if __name__== "_main_":
    main()