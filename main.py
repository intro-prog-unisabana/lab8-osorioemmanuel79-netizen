"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md
import sys
from todo_manager import read_todo_file, write_todo_file

try:
    
    if len(sys.argv) < 2:
        raise IndexError("Insufficient arguments provided!")

    if sys.argv[1] == "--help":
        print("""Usage: python main.py <file_path> <command> [arguments]...

Commands:
  add "task"    - Add a task to the list.
  remove "task" - Remove a task from the list.
  view          - Display all tasks.
""")
        sys.exit()

    file_path = sys.argv[1]
    tasks = read_todo_file(file_path)

    i = 2
    modified = False  

    while i < len(sys.argv):
        command = sys.argv[i]

    
        if command == "add":
            if i + 1 >= len(sys.argv):
                raise IndexError('Task description required for "add".')

            task = sys.argv[i + 1]
            tasks.append(task)
            print(f'Task "{task}" added.')
            modified = True
            i += 2

        elif command == "remove":
            if i + 1 >= len(sys.argv):
                raise IndexError('Task description required for "remove".')

            task = sys.argv[i + 1]
            try:
                tasks.remove(task)
                print(f'Task "{task}" removed.')
                modified = True
            except ValueError:
                print(f'Task "{task}" not found.')
            i += 2

        elif command == "view":
            if not tasks:
                print("No tasks found.")
            else:
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. {task}")
            i += 1

        else:
            raise ValueError("Command not found!")

    if modified:
        write_todo_file(file_path, tasks)

except IndexError as e:
    print(e)
except ValueError as e:
    print(e)