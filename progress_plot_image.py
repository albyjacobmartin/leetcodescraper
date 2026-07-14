import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

def plot_leetcode_curve(data):
    """
    Plots a smooth, continuous curve through daily LeetCode completion points
    and saves it directly as an image file.
    """
    days = np.array(list(range(1, len(data) + 1)))
    x_smooth = np.linspace(days.min(), days.max(), 300)
    spl = make_interp_spline(days, data, k=3)
    y_smooth = np.clip(spl(x_smooth), 0, None)
    plt.figure(figsize=(9, 5))
    plt.plot(x_smooth, y_smooth, color='darkorange', linewidth=2.5, label='Activity Curve')
    plt.scatter(days, data, color='teal', s=50, zorder=5, label='Daily Count')
    plt.title('LeetCode Daily Progress Curve', fontsize=14, pad=15)
    plt.xlabel('Day', fontsize=12)
    plt.ylabel('Questions Completed', fontsize=12)
    plt.xticks(days)
    plt.grid(True, linestyle='-', alpha=0.3)
    plt.legend()
    plt.tight_layout()
    filename = 'leetcode_progress.png'
    plt.savefig(filename, dpi=300)
    plt.close()
    print(f"Success! Image saved as '{filename}' in the current folder.")
leetcode_data = [2, 2, 2, 2, 5, 10, 7, 3, 18, 19, 41, 26, 26, 3, 3, 2, 7, 2]
plot_leetcode_curve(leetcode_data)