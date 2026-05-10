"""fig08 — the unit circle with marked complex numbers."""
import numpy as np
from _helpers import new_axes, point, save_and_show

fig, ax = new_axes((-1.5, 1.5), (-1.5, 1.5),
                   "The unit circle  { z ∈ ℂ : |z| = 1 }")

t = np.linspace(0, 2*np.pi, 400)
ax.plot(np.cos(t), np.sin(t), color="C0", lw=2)

marks = [
    (1 + 0j,                  "1",            "θ = 0"),
    (0 + 1j,                  "i",            "θ = π/2"),
    (-1 + 0j,                 "−1",           "θ = π"),
    (0 - 1j,                  "−i",           "θ = 3π/2"),
    (np.cos(np.pi/4) + 1j*np.sin(np.pi/4), "e^(iπ/4)", "θ = π/4"),
    (np.cos(np.pi/3) + 1j*np.sin(np.pi/3), "e^(iπ/3)", "θ = π/3"),
]
for z, label, ang in marks:
    point(ax, z, label=f"{label}\n{ang}", color="C3")

save_and_show(fig, "fig08_unit_circle.png")
