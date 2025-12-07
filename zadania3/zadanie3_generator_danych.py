"""Generator przykładowych danych do eksperymentów z regresją.

Tworzy prostą serię (x, y) z niewielkim szumem, zapisuje ją do pliku CSV
oraz wypisuje na ekran. Całość działa bez dodatkowych bibliotek.
"""
from __future__ import annotations

import csv
import random
from pathlib import Path
from typing import Iterable, Tuple


def generate_data(count: int = 20) -> Iterable[Tuple[float, float]]:
    """Tworzy losowe punkty zgodne w przybliżeniu z funkcją kwadratową."""
    for i in range(count):
        x = float(i)
        clean_y = 0.4 * x * x + 0.6 * x + 1.5
        noise = random.uniform(-0.5, 0.5)
        yield x, clean_y + noise


def save_csv(points: Iterable[Tuple[float, float]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["x", "y"])
        for x, y in points:
            writer.writerow([x, y])


def demo() -> None:
    data = list(generate_data(15))
    for x, y in data:
        print(f"x={x:>4.1f} | y={y:>6.2f}")

    save_csv(data, Path("zadania3/dane_przykladowe.csv"))
    print("Zapisano dane do zadania: zadania3/dane_przykladowe.csv")


if __name__ == "__main__":
    demo()
