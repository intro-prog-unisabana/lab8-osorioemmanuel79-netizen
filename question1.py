"""Laboratorio 8 - Problema 1.

Implementa una CLI que calcule carga por punto de soporte.
"""

# TODO: Implementar según README.md
# question1.py
import sys

try:
    # Verificar que haya exactamente 2 argumentos (sin contar el nombre del script)
    if len(sys.argv) != 3:
        raise ValueError

    # Convertir entradas a números
    total_load = float(sys.argv[1])
    num_supports = float(sys.argv[2])

    # Verificar división por cero
    if num_supports == 0:
        print("Error: Cannot divide by zero! Supports must be greater than zero.")
    else:
        load_per_support = total_load / num_supports
        print(f"Load per support point: {load_per_support:.2f} N")

