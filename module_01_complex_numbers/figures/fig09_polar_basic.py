"""fig09 — a point shown with both cartesian (a, b) and polar (r, θ) labels."""
import numpy as np
import matplotlib.pyplot as plt
from _helpers import new_axes, point, save_and_show

z = 1 + 1j * np.sqrt(3)        # r = 2, θ = π/3
r = abs(z)
theta = np.angle(z)

fig, ax = new_axes(xlim=(-1, 3), ylim=(-1, 3),
                   title=r"Polar form: $z = 1 + i\sqrt{3} = 2\,e^{i\pi/3}$")

# arrow from origin to z
ax.annotate("", xy=(z.real, z.imag), xytext=(0, 0),
            arrowprops=dict(arrowstyle="->", color="C0", lw=2))

# radius label
ax.text(z.real / 2 - 0.25, z.imag / 2 + 0.1, f"r = {r:.2f}",
        color="C0", fontsize=12)

# arc showing θ
arc_t = np.linspace(0, theta, 60)
ax.plot(0.5 * np.cos(arc_t), 0.5 * np.sin(arc_t), color="C3", lw=2)
ax.text(0.55, 0.25, r"$\theta = \pi/3$", color="C3", fontsize=12)

# cartesian dashed projections
ax.plot([z.real, z.real], [0, z.imag], "k--", lw=0.8)
ax.plot([0, z.real], [z.imag, z.imag], "k--", lw=0.8)
ax.text(z.real + 0.05, -0.3, f"a = {z.real:.2f}", fontsize=11)
ax.text(-0.7, z.imag, f"b = {z.imag:.2f}", fontsize=11)

point(ax, z, label="z", color="C0")
save_and_show(fig, "fig09_polar_basic.png")
