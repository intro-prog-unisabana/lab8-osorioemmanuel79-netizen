"""Laboratorio 8 - Módulo de persistencia para lista de tareas."""


def read_todo_file(file_path):
    """Reads tasks from a file. Returns a list of tasks."""
    # TODO: Implementar manejo de FileNotFoundError según README.md
    raise NotImplementedError


def write_todo_file(file_path, tasks):
    """Writes tasks to a file, one per line."""
    # TODO: Implementar escritura de tareas según README.md
    raise NotImplementedError

# todo_manager.py

def read_todo_file(filename):
    try:
        with open(filename, "r") as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []
    except Exception:
        print("Error: Could not read file.")
        return []


def write_todo_file(filename, tasks):
    try:
        with open(filename, "w") as file:
            for task in tasks:
                file.write(task + "\n")
    except Exception:
        print("Error: Could not write to file.")