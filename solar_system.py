import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Dữ liệu hành tinh (bán trục lớn, độ lệch tâm, chu kỳ quỹ đạo)
planets_data = {
    "Mercury": (0.39, 0.206, 0.24),
    "Venus": (0.72, 0.007, 0.62),
    "Earth": (1.00, 0.017, 1.00),
    "Mars": (1.52, 0.093, 1.88),
    "Jupiter": (5.20, 0.048, 11.86),
    "Saturn": (9.58, 0.056, 29.45),
    "Uranus": (19.22, 0.047, 84.02),
    "Neptune": (30.05, 0.009, 164.8),
}

# Số bước thời gian
num_frames = 365

# Hàm tính toán vị trí hành tinh tại một thời điểm
def calculate_planet_position(a, e, T, t):
    M = 2 * np.pi * t / T  # Trung bình dị thường
    E = M  # Bắt đầu với phỏng đoán đầu tiên cho dị thường lệch tâm
    for _ in range(10):  # Lặp lại để tinh chỉnh E
        E = E - (E - e * np.sin(E) - M) / (1 - e * np.cos(E))
    x = a * (np.cos(E) - e)
    y = a * np.sqrt(1 - e**2) * np.sin(E)
    return x, y

# Tạo hình và trục
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-35, 35)
ax.set_ylim(-35, 35)
ax.set_aspect("equal")
ax.set_facecolor("black")

# Vẽ Mặt trời
sun = plt.Circle((0, 0), 0.5, color="yellow")
ax.add_patch(sun)

# Tạo các đường quỹ đạo và điểm hành tinh
planet_paths = {}
planet_points = {}
for planet, (a, e, T) in planets_data.items():
    theta = np.linspace(0, 2 * np.pi, 100)
    x_orbit = a * np.cos(theta)
    y_orbit = a * np.sqrt(1 - e**2) * np.sin(theta)
    planet_paths[planet], = ax.plot(x_orbit, y_orbit, linestyle="--", alpha=0.5, color="gray")
    planet_points[planet], = ax.plot([], [], "o", markersize=5)

# Hàm cập nhật cho hoạt ảnh
def update(frame):
    for planet, (a, e, T) in planets_data.items():
        x, y = calculate_planet_position(a, e, T, frame)
        planet_points[planet].set_data(x, y)
    return [point for point in planet_points.values()]

# Tạo hoạt ảnh
animation = FuncAnimation(fig, update, frames=num_frames, interval=20, blit=True)

# Hiển thị hoạt ảnh
plt.show()
