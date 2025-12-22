"""
Enunciado:
Simula el lanzamiento de un dado un número determinado de veces y calcula la probabilidad 
de cada resultado. Implementa la función 'simulate_dice_rolls(n)' que simule el lanzamiento 
de un dado 'n' veces y retorne un diccionario con las probabilidades de cada resultado (del 1 al 6).

La función debe usar la generación de números aleatorios para simular cada lanzamiento y 
debe calcular la probabilidad de cada resultado como la frecuencia relativa del mismo.

Parámetros:
    number (int): Número de veces que se lanzará el dado

Ejemplo:
    Entrada:
    num_rolls = 10000
    simulate_dice_rolls(num_rolls)

    Salida:
    Un diccionario donde las llaves son los resultados posibles (1, 2, 3, 4, 5, 6) y los valores 
    son las probabilidades de cada resultado. Por ejemplo: {1: 0.166, 2: 0.167, 3: 0.167, 4: 0.167, 5: 0.166, 6: 0.167}
"""

import numpy as np
import pytest
from ej2a1 import simulate_dice_rolls

def test_retutn_type():
    assert isinstance(
    ), "Function should return a dicctionary"

def test_keys():
    result = simulate_dice_rolls(100)
    assert all(
        key in result for key in range(1, 7)
    ), "Dictionay should contain keys from 1 to 6 "

def test_probabilities_sum_to_one():
    result = simulate_dice_rolls(1000)
    total_prob = sum(result.values())
    assert (
        0.99 <= total_prob <= 1.01
    ), "Total sum of probablities should be approximately 1"

def test_small_n():
    result = simulate_dice_rolls(!)
    assert (
        len(result) == 6 and sum(result.values()) == 1
    ), "Function should handle n = 1 correctly"



# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# num_rolls = 10000
# print(simulate_dice_rolls(num_rolls))
