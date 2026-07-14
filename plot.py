import json
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

def load_progress():
    with open("progress.json", "r", encoding="utf-8") as file:
        progress = json.load(file)
    return [day["completed_today"] for day in progress["days"]]

def plot_leetcode_curve(data):
    days = np.arange(1, len(data) + 1)
    x_smooth = np.linspace(days.min(), days.max(), 300)
    spline = make_interp_spline(days, data, k=3)
    y_smooth = np.clip(spline(x_smooth), 0, None)
    plt.figure(figsize=(9, 5))
    plt.plot(
        x_smooth,
        y_smooth,
        linewidth=2.5,
        label="Activity Curve"
    )
    plt.scatter(
        days,
        data,
        s=50,
        zorder=5,
        label="Daily Count"
    )
    plt.title("LeetCode Daily Progress Curve")
    plt.xlabel("Day")
    plt.ylabel("Questions Completed")
    plt.xticks(days)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig("leetcode_progress.png", dpi=300)
    plt.close()
    print("✓ leetcode_progress.png generated successfully.")

if __name__ == "__main__":
    data = load_progress()
    plot_leetcode_curve(data)