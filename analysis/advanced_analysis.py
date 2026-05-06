import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

with open("../data/results.json") as f:
    data = json.load(f)

df = pd.DataFrame(data)

print("=" * 60)
print("ALGORITHM BENCHMARKING ANALYSIS")
print("=" * 60)

# ===== OVERALL STATISTICS =====
print("\n📊 OVERALL PERFORMANCE (Average across all tests):")
print(df.groupby("algorithm")[["time_ms", "time_us"]].agg({
    "time_ms": ["mean", "min", "max"],
    "time_us": ["mean"]
}).round(4))

# ===== BY SIZE SCALING =====
print("\n📈 PERFORMANCE BY GRID SIZE (20% density):")
size_scaling = df[df["category"] == "size_scaling"].groupby(["size", "algorithm"])["time_ms"].mean().unstack()
print(size_scaling.round(4))

fig, ax = plt.subplots(figsize=(10, 6))
for algo in ["bfs", "dfs", "dijkstra", "astar"]:
    if algo in size_scaling.columns:
        ax.plot(size_scaling.index, size_scaling[algo], marker='o', label=algo, linewidth=2)
ax.set_xlabel("Grid Size")
ax.set_ylabel("Time (ms)")
ax.set_title("Performance Scaling by Grid Size (20% Density)")
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("./scaling_by_size.png", dpi=150)
print("✓ Saved: scaling_by_size.png")

# ===== BY DENSITY =====
print("\n🔥 PERFORMANCE BY OBSTACLE DENSITY (100x100 grid):")
density_scaling = df[df["category"] == "density_scaling"].groupby(["density", "algorithm"])["time_ms"].mean().unstack()
print(density_scaling.round(4))

fig, ax = plt.subplots(figsize=(10, 6))
for algo in ["bfs", "dfs", "dijkstra", "astar"]:
    if algo in density_scaling.columns:
        ax.plot(density_scaling.index, density_scaling[algo], marker='s', label=algo, linewidth=2)
ax.set_xlabel("Obstacle Density")
ax.set_ylabel("Time (ms)")
ax.set_title("Performance Scaling by Obstacle Density (100x100 Grid)")
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("./scaling_by_density.png", dpi=150)
print("✓ Saved: scaling_by_density.png")

# ===== SUCCESS RATES =====
print("\n✅ SUCCESS RATE BY CATEGORY:")
success_by_cat = df.groupby(["category", "algorithm"])["success"].mean().unstack() * 100
print(success_by_cat.round(2))

# ===== WORST CASE ANALYSIS =====
print("\n⚠️  WORST CASE SCENARIOS:")
worst_df = df[df["category"].str.contains("worst_case|impossible|trivial", na=False)]
if len(worst_df) > 0:
    print(worst_df.groupby(["category", "algorithm"])[["time_ms", "success", "path_length"]].agg({
        "time_ms": "mean",
        "success": "mean",
        "path_length": "mean"
    }).round(4))

# ===== COMPARISON CHART =====
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# By size
size_data = df[df["category"] == "size_scaling"].groupby(["size", "algorithm"])["time_ms"].mean().unstack()
size_data.plot(ax=axes[0], marker='o')
axes[0].set_title("Time vs Grid Size")
axes[0].set_xlabel("Grid Size")
axes[0].set_ylabel("Time (ms)")
axes[0].grid(True, alpha=0.3)

# By density
density_data = df[df["category"] == "density_scaling"].groupby(["density", "algorithm"])["time_ms"].mean().unstack()
density_data.plot(ax=axes[1], marker='s')
axes[1].set_title("Time vs Obstacle Density")
axes[1].set_xlabel("Density")
axes[1].set_ylabel("Time (ms)")
axes[1].grid(True, alpha=0.3)

# Average comparison
avg_by_algo = df.groupby("algorithm")["time_ms"].mean()
avg_by_algo.plot(kind="bar", ax=axes[2], color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
axes[2].set_title("Average Runtime by Algorithm")
axes[2].set_ylabel("Time (ms)")
axes[2].set_xlabel("Algorithm")
axes[2].tick_params(axis='x', rotation=45)
axes[2].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig("./complete_analysis.png", dpi=150)
print("✓ Saved: complete_analysis.png")

print("\n" + "=" * 60)
print("✓ Analysis complete! Check PNG files for visualizations.")
print("=" * 60)
