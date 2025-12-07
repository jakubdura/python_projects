"""Obliczanie błędów modelu regresji na małym zbiorze danych.

Skrypt korzysta z klasy `QuadraticModel` z zadania 1, ale rozdzielamy
logikę do osobnego pliku, aby móc ją uruchamiać samodzielnie.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Iterable, List

# Umożliwia importowanie modułu z sąsiedniego pliku przy uruchamianiu bezpośrednim
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from zadania3.zadanie1_regresja_kwadratowa import QuadraticModel, fit_quadratic


def mean_absolute_error(model: QuadraticModel, xs: Iterable[float], ys: Iterable[float]) -> float:
    """Liczy średni błąd bezwzględny (MAE) między predykcją a pomiarem."""
    x_list: List[float] = list(xs)
    y_list: List[float] = list(ys)

    if len(x_list) != len(y_list):
        raise ValueError("Listy x i y muszą mieć taką samą długość")
    if not x_list:
        raise ValueError("Listy nie mogą być puste")

    errors = [abs(model.predict(x) - y) for x, y in zip(x_list, y_list)]
    return sum(errors) / len(errors)


def demo() -> None:
    # Dane testowe - można je zamienić na własne pomiary
    xs = [0, 1, 2, 3, 4]
    ys = [1, 1.8, 3.2, 5.1, 7.6]

    model = fit_quadratic(xs, ys)

    mae = mean_absolute_error(model, xs, ys)
    print("Średni błąd bezwzględny dla zbioru uczącego:", round(mae, 4))

    # Sprawdzenie na nowym punkcie
    test_x = 5
    print(f"Przewidywana wartość dla x={test_x}: {model.predict(test_x):.3f}")


if __name__ == "__main__":
    demo()
