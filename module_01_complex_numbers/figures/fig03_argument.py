"""fig03 — arg(z) as the angle from the positive real axis (4 quadrants)."""
import numpy as np
from matplotlib.patches import Arc
from _helpers import new_axes, arrow, point, save_and_show

fig, ax = new_axes((-2.5, 2.5), (-2.5, 2.5),
                   "Argument  arg(z)  =  angle from +Re axis")

zs = [
    (1 + 1j,  "1 + i",   "π/4",     "C0"),
    (-1 + 1j, "−1 + i",  "3π/4",    "C1"),
    (-1 - 1j, "−1 − i",  "−3π/4",   "C2"),
    (1 - 1j,  "1 − i",   "−π/4",    "C3"),
]

for z, label, ang_label, color in zs:
    arrow(ax, 0+0j, z, color=color, lw=2)
    point(ax, z, label=f"{label}\narg = {ang_label}", color=color)

# draw arc for the first one (1 + i, angle 0 → π/4)
arc = Arc((0, 0), 0.8, 0.8, angle=0, theta1=0, theta2=45,
          color="C0", lw=2)
ax.add_patch(arc)
ax.text(0.55, 0.18, "θ", color="C0", fontsize=14)

# unit circle as reference
t = np.linspace(0, 2*np.pi, 200)
ax.plot(np.sqrt(2)*np.cos(t), np.sqrt(2)*np.sin(t),
        color="gray", linestyle=":", alpha=0.5)
ax.text(1.5, 1.5, "|z| = √2 circle", color="gray", fontsize=9)

save_and_show(fig, "fig03_argument.png")
