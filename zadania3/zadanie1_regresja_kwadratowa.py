"""Prosty przykład regresji kwadratowej bez dodatkowych bibliotek.

Skrypt zakłada, że dysponujemy parą wektorów `x` i `y` (np. wyniki
pomiarów) i chcemy dopasować do nich funkcję postaci:
    f(x) = a*x**2 + b*x + c
Wszystkie obliczenia wykonujemy ręcznie (Cramera) tak, aby kod działał
na czystym Pythonie.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Tuple


def _det3(m: List[List[float]]) -> float:
    """Zwraca wyznacznik macierzy 3x3 (pomoc do Cramera)."""
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )


def _solve_3x3(a: List[List[float]], b: List[float]) -> Tuple[float, float, float]:
    """Rozwiązuje układ równań A*x = b metodą Cramera."""
    det_a = _det3(a)
    if abs(det_a) < 1e-9:
        raise ValueError("Macierz osobliwa - nie da się wyliczyć współczynników")

    def replace(col: int) -> List[List[float]]:
        new = [row[:] for row in a]
        for i in range(3):
            new[i][col] = b[i]
        return new

    return (
        _det3(replace(0)) / det_a,
        _det3(replace(1)) / det_a,
        _det3(replace(2)) / det_a,
    )


@dataclass
class QuadraticModel:
    a: float
    b: float
    c: float

    def predict(self, x: float) -> float:
        return self.a * x * x + self.b * x + self.c


def fit_quadratic(xs: Iterable[float], ys: Iterable[float]) -> QuadraticModel:
    """Dopasowuje model kwadratowy do podanych punktów."""
    x_list = list(xs)
    y_list = list(ys)

    if len(x_list) != len(y_list):
        raise ValueError("Listy x i y muszą mieć taką samą długość")
    if len(x_list) < 3:
        raise ValueError("Potrzebne są co najmniej 3 punkty do wyznaczenia a,b,c")

    # Przygotowanie sum występujących w równaniach normalnych (metoda najmniejszych kwadratów)
    n = float(len(x_list))
    sum_x = sum(x_list)
    sum_x2 = sum(x * x for x in x_list)
    sum_x3 = sum(x * x * x for x in x_list)
    sum_x4 = sum(x * x * x * x for x in x_list)
    sum_y = sum(y_list)
    sum_xy = sum(x * y for x, y in zip(x_list, y_list))
    sum_x2y = sum((x * x) * y for x, y in zip(x_list, y_list))

    # Macierz 3x3 dla współczynników a, b, c
    A = [
        [sum_x4, sum_x3, sum_x2],
        [sum_x3, sum_x2, sum_x],
        [sum_x2, sum_x, n],
    ]

    B = [sum_x2y, sum_xy, sum_y]

    a, b, c = _solve_3x3(A, B)
    return QuadraticModel(a=a, b=b, c=c)


def demo() -> None:
    """Mała demonstracja działania na sztucznych danych."""
    # Dane można podmienić na własne pomiary (listy długości >= 3)
    xs = [0, 1, 2, 3, 4]
    ys = [1, 1.8, 3.2, 5.1, 7.6]

    model = fit_quadratic(xs, ys)
    print("Wyznaczone współczynniki:")
    print(f"  a = {model.a:.4f}, b = {model.b:.4f}, c = {model.c:.4f}")

    # Przykładowa prognoza
    test_x = 5
    print(f"f({test_x}) = {model.predict(test_x):.3f}")


if __name__ == "__main__":
    demo()
