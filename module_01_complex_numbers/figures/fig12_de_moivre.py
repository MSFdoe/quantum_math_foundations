"""fig12 — De Moivre: powers of z = e^(iπ/6) trace 12 equally-spaced points."""
import numpy as np
from _helpers import new_axes, save_and_show

fig, ax = new_axes(xlim=(-1.5, 1.5), ylim=(-1.5, 1.5),
                   title=r"De Moivre: $z^n$ for $z = e^{i\pi/6}$, $n = 0..11$")

t = np.linspace(0, 2 * np.pi, 400)
ax.plot(np.cos(t), np.sin(t), color="gray", lw=1, linestyle=":")

theta0 = np.pi / 6
for n in range(12):
    zn = np.exp(1j * n * theta0)
    ax.plot(zn.real, zn.imag, "o", color="C3", markersize=7)
    ax.text(1.18 * zn.real, 1.18 * zn.imag, f"$z^{{{n}}}$",
            color="C3", fontsize=10, ha="center", va="center")

save_and_show(fig, "fig12_de_moivre.png")
