"""
benchmarks/test_hotpaths.py
THE TRIPWIRE BASELINE (Tier 1 Enforcement)
"""
import pytest
import math
import random
from array import array

N_ITEMS = 100_000

# 🔴 BAD: Tier 3 OOP (Forbidden in Hot Paths)
class Point:
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

def process_oop(points: list[Point]) -> list[float]:
    results = []
    for p in points:
        results.append(math.sqrt(p.x**2 + p.y**2))
    return results

# 🟢 GOOD: Tier 1 SoA (Mandatory)
def process_soa(data: dict[str, array]) -> array:
    xs = data['x']
    ys = data['y']
    results = array('f', [])
    for i in range(len(xs)):
        results.append(math.sqrt(xs[i]**2 + ys[i]**2))
    return results

# ⚡ FIXTURES
@pytest.fixture
def oop_dataset():
    return [Point(random.random(), random.random()) for _ in range(N_ITEMS)]

@pytest.fixture
def soa_dataset():
    return {
        'x': array('f', [random.random() for _ in range(N_ITEMS)]),
        'y': array('f', [random.random() for _ in range(N_ITEMS)])
    }

# ⏱️ BENCHMARKS
def test_hotpath_oop_baseline(benchmark, oop_dataset):
    benchmark(process_oop, oop_dataset)

def test_hotpath_soa_optimized(benchmark, soa_dataset):
    benchmark(process_soa, soa_dataset)
