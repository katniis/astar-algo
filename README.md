# Pathfinding Algorithm Benchmarker

A C++ benchmarking suite that measures and compares the performance of four classic grid-based pathfinding algorithms: **BFS**, **DFS**, **Dijkstra**, and **A\***. Results are exported to JSON and visualized using Python.

---

## Algorithms

All four algorithms operate on 2D grids where `0` is a passable cell and `1` is an obstacle. Movement is 4-directional (no diagonals).

| Algorithm | Optimal Path? | Strategy |
|-----------|--------------|----------|
| BFS | ✅ Yes | Breadth-first, unweighted |
| DFS | ❌ No | Depth-first, recursive |
| Dijkstra | ✅ Yes | Priority queue, uniform cost |
| A\* | ✅ Yes | Priority queue + Manhattan heuristic |

---

## Project Structure

```
src/
├── algorithms/
│   ├── astar.h            # A* implementation
│   ├── bfs.h              # BFS implementation
│   ├── dfs.h              # DFS implementation (recursive)
│   └── dijkstra.h         # Dijkstra implementation
├── benchmarks/
│   ├── benchmark_runner.cpp   # Main C++ benchmark runner
│   └── gen_testcases.py       # Test case generator
├── analysis/
│   ├── analyze.py             # Basic analysis & plots
│   └── advanced_analysis.py   # Full analysis with scaling charts
├── data/
│   ├── testcases.json     # Generated test cases (input)
│   └── results.json       # Benchmark results (output)
└── lib/
    └── json.hpp           # nlohmann/json (single-header)
```

---

## Getting Started

### Prerequisites

- A C++17-compatible compiler (g++ recommended)
- Python 3.x with `pandas` and `matplotlib`

### 1. Generate Test Cases

```bash
cd src/benchmarks
python gen_testcases.py
```

This writes `src/data/testcases.json` with a comprehensive set of test scenarios (see [Test Categories](#test-categories) below).

### 2. Compile and Run the Benchmark

```bash
cd src/benchmarks
g++ -O2 -std=c++17 benchmark_runner.cpp -o benchmark_runner
./benchmark_runner
```

Results are written to `src/data/results.json`.

### 3. Analyze Results

For a quick look:
```bash
cd src/analysis
python analyze.py
```

For the full breakdown with saved charts:
```bash
python advanced_analysis.py
```

This generates three PNG files in `src/analysis/`:
- `scaling_by_size.png` — runtime vs. grid size
- `scaling_by_density.png` — runtime vs. obstacle density
- `complete_analysis.png` — side-by-side comparison dashboard

---

## Test Categories

| Category | Description |
|----------|-------------|
| `size_scaling` | Grids from 10×10 to 200×200 at 20% obstacle density |
| `density_scaling` | 100×100 grid with density from 5% to 50% |
| `worst_case_impossible` | Fully blocked 50×50 grid (no path exists) |
| `trivial_same_start_goal` | Start and goal are the same cell |
| `easy_sparse` | 100×100 grid at 5% density |
| `hard_dense` | 100×100 grid at 50% density |

---

## Results Format

Each entry in `results.json` looks like:

```json
{
  "algorithm": "astar",
  "category": "size_scaling",
  "size": 100,
  "density": 0.2,
  "test": "test_5",
  "time_us": 1240,
  "time_ms": 1.24,
  "path_length": 199,
  "success": true
}
```

---

## Key Findings

- **DFS** is consistently the fastest in raw time, but does **not** guarantee shortest paths.
- **BFS** and **Dijkstra** always return optimal paths on uniform-cost grids; Dijkstra has higher constant overhead.
- **A\*** uses the Manhattan distance heuristic to reduce explored nodes, making it the best balance of speed and optimality.
- All algorithms handle impossible mazes gracefully, returning an empty path.

---

## Dependencies

- [`nlohmann/json`](https://github.com/nlohmann/json) — included as a single header in `src/lib/json.hpp`
- `pandas`, `matplotlib` — for analysis scripts (`pip install pandas matplotlib`)
