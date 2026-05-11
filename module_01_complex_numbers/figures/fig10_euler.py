"""fig10 — the unit circle traced by e^(iθ) as θ runs 0 → 2π."""
import numpy as np
from _helpers import new_axes, save_and_show

fig, ax = new_axes(xlim=(-1.5, 1.5), ylim=(-1.5, 1.5),
                   title=r"Euler: $e^{i\theta} = \cos\theta + i\sin\theta$ on the unit circle")

t = np.linspace(0, 2 * np.pi, 400)
ax.plot(np.cos(t), np.sin(t), color="C0", lw=2)

# mark canonical angles
specials = {0: "1",
            np.pi / 4: r"$e^{i\pi/4}$",
            np.pi / 2: r"$i$",
            np.pi: r"$-1$",
            3 * np.pi / 2: r"$-i$"}

for th, lab in specials.items():
    x, y = np.cos(th), np.sin(th)
    ax.plot(x, y, "o", color="C3", markersize=7)
    ax.text(1.15 * x, 1.15 * y, lab, color="C3", fontsize=12,
            ha="center", va="center")

save_and_show(fig, "fig10_euler.png")
