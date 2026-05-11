"""fig11 — multiplication in polar form: angles add, moduli multiply."""
import numpy as np
from _helpers import new_axes, point, save_and_show

z = 1.2 * np.exp(1j * np.pi / 6)     # r=1.2, θ=30°
w = 1.5 * np.exp(1j * np.pi / 3)     # r=1.5, θ=60°
zw = z * w                            # r=1.8, θ=90°

fig, ax = new_axes(xlim=(-1, 3), ylim=(-0.5, 3),
                   title=r"$z \cdot w$:  multiply moduli, add angles")

for v, lab, col in [(z, "z", "C0"), (w, "w", "C2"), (zw, r"$z \cdot w$", "C3")]:
    ax.annotate("", xy=(v.real, v.imag), xytext=(0, 0),
                arrowprops=dict(arrowstyle="->", color=col, lw=2))
    point(ax, v, label=lab, color=col)

info = (f"|z| = {abs(z):.2f},  arg z = 30°\n"
        f"|w| = {abs(w):.2f},  arg w = 60°\n"
        f"|zw| = {abs(zw):.2f},  arg(zw) = 90°")
ax.text(-0.9, 2.6, info, fontsize=10,
        bbox=dict(facecolor="white", edgecolor="gray"))

save_and_show(fig, "fig11_polar_multiplication.png")
