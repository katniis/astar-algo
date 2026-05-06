import json
import random

def generate_grid(size, density):
    """Generate random grid with given obstacle density"""
    grid = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if random.random() < density:
                grid[i][j] = 1
    return grid

tests = []
test_id = 1

# ===== VARYING GRID SIZES WITH MEDIUM DENSITY =====
for size in [10, 20, 50, 100, 150, 200]:
    grid = generate_grid(size, 0.2)
    grid[0][0] = 0  # ensure start is passable
    grid[size-1][size-1] = 0  # ensure goal is passable
    tests.append({
        "metadata": {
            "test_name": f"test_{test_id}",
            "size": size,
            "density": 0.2,
            "category": "size_scaling"
        },
        "grid": {"rows": size, "cols": size, "cells": grid},
        "start": [0, 0],
        "goal": [size-1, size-1],
        "movement": {"allow_diagonal": False},
        "weights": {"enabled": False}
    })
    test_id += 1

# ===== VARYING DENSITY ON 100x100 GRID =====
for density in [0.05, 0.1, 0.2, 0.3, 0.4, 0.5]:
    grid = generate_grid(100, density)
    grid[0][0] = 0
    grid[99][99] = 0
    tests.append({
        "metadata": {
            "test_name": f"test_{test_id}",
            "size": 100,
            "density": density,
            "category": "density_scaling"
        },
        "grid": {"rows": 100, "cols": 100, "cells": grid},
        "start": [0, 0],
        "goal": [99, 99],
        "movement": {"allow_diagonal": False},
        "weights": {"enabled": False}
    })
    test_id += 1

# ===== WORST CASE: IMPOSSIBLE MAZE =====
grid = [[1 for _ in range(50)] for _ in range(50)]
grid[0][0] = 0
tests.append({
    "metadata": {
        "test_name": f"test_{test_id}",
        "size": 50,
        "density": 1.0,
        "category": "worst_case_impossible"
    },
    "grid": {"rows": 50, "cols": 50, "cells": grid},
    "start": [0, 0],
    "goal": [49, 49],
    "movement": {"allow_diagonal": False},
    "weights": {"enabled": False}
})
test_id += 1

# ===== TRIVIAL CASE: START == GOAL =====
grid = generate_grid(50, 0.2)
tests.append({
    "metadata": {
        "test_name": f"test_{test_id}",
        "size": 50,
        "density": 0.2,
        "category": "trivial_same_start_goal"
    },
    "grid": {"rows": 50, "cols": 50, "cells": grid},
    "start": [25, 25],
    "goal": [25, 25],
    "movement": {"allow_diagonal": False},
    "weights": {"enabled": False}
})
test_id += 1

# ===== SPARSE MAZE (EASY) =====
grid = generate_grid(100, 0.05)
grid[0][0] = 0
grid[99][99] = 0
tests.append({
    "metadata": {
        "test_name": f"test_{test_id}",
        "size": 100,
        "density": 0.05,
        "category": "easy_sparse"
    },
    "grid": {"rows": 100, "cols": 100, "cells": grid},
    "start": [0, 0],
    "goal": [99, 99],
    "movement": {"allow_diagonal": False},
    "weights": {"enabled": False}
})
test_id += 1

# ===== DENSE MAZE (HARD) =====
grid = generate_grid(100, 0.5)
grid[0][0] = 0
grid[99][99] = 0
tests.append({
    "metadata": {
        "test_name": f"test_{test_id}",
        "size": 100,
        "density": 0.5,
        "category": "hard_dense"
    },
    "grid": {"rows": 100, "cols": 100, "cells": grid},
    "start": [0, 0],
    "goal": [99, 99],
    "movement": {"allow_diagonal": False},
    "weights": {"enabled": False}
})

with open("../data/testcases.json", "w") as f:
    json.dump({"tests": tests}, f, indent=2)

print(f"Generated {len(tests)} comprehensive test cases")
