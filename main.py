"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md

# main.py
import sys
from todo_manager import read_todo_file, write_todo_file

def main():
    try:
        if len(sys.argv) < 3:
            raise ValueError

        filename = sys.argv[1]
        command = sys.argv[2]

        tasks = read_todo_file(filename)

        # VER TAREAS
        if command == "view":
            if not tasks:
                print("No tasks found.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")

        # AGREGAR TAREA
        elif command == "add":
            if len(sys.argv) < 4:
                raise ValueError

            new_task = " ".join(sys.argv[3:])
            tasks.append(new_task)
            write_todo_file(filename, tasks)
            print("Task added.")

        # ELIMINAR TAREA
        elif command == "remove":
            if len(sys.argv) < 4:
                raise ValueError

            index = int(sys.argv[3]) - 1

            if index < 0 or index >= len(tasks):
                print("Error: Invalid task number.")
            else:
                removed = tasks.pop(index)
                write_todo_file(filename, tasks)
                print(f"Removed task: {removed}")

        else:
            print("Error: Invalid command.")

    except ValueError:
        print("Error: Invalid input.")

    except Exception:
        print("Error: Something went wrong.")

if __name__ == "__main__":
    main()