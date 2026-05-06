import json
import pandas as pd
import matplotlib.pyplot as plt

with open("../data/results.json") as f:
    data = json.load(f)

df = pd.DataFrame(data)

# ===== AVERAGE TIME =====
avg_time = df.groupby("algorithm")["time_ms"].mean()

plt.figure()
avg_time.plot(kind="line")
plt.title("Average Runtime per Algorithm")
plt.ylabel("Time (ms)")
plt.show()

# ===== PATH LENGTH =====
avg_path = df.groupby("algorithm")["path_length"].mean()

plt.figure()
avg_path.plot(kind="line")
plt.title("Average Path Length")
plt.ylabel("Steps")
plt.show()

# ===== SUCCESS RATE =====
success_rate = df.groupby("algorithm")["success"].mean()

plt.figure()
success_rate.plot(kind="line")
plt.title("Success Rate per Algorithm")
plt.ylabel("Ratio")
plt.show()