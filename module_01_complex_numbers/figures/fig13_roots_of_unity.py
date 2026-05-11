"""fig13 — n-th roots of unity as regular n-gons for n = 3, 4, 5, 6."""
import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(10, 10))
fig.suptitle(r"$n$-th roots of unity: $z_k = e^{i \cdot 2\pi k / n}$", fontsize=14)

t = np.linspace(0, 2 * np.pi, 400)

for ax, n in zip(axes.flat, [3, 4, 5, 6]):
    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(-1.4, 1.4)
    ax.set_aspect("equal")
    ax.grid(True, linestyle=":", alpha=0.5)
    ax.axhline(0, color="black", lw=0.8)
    ax.axvline(0, color="black", lw=0.8)
    ax.plot(np.cos(t), np.sin(t), color="gray", lw=1, linestyle=":")
    ax.set_title(f"n = {n}")

    pts = [np.exp(1j * 2 * np.pi * k / n) for k in range(n)]
    xs = [p.real for p in pts] + [pts[0].real]
    ys = [p.imag for p in pts] + [pts[0].imag]
    ax.plot(xs, ys, color="C0", lw=2)
    for k, p in enumerate(pts):
        ax.plot(p.real, p.imag, "o", color="C3", markersize=7)
        ax.text(1.18 * p.real, 1.18 * p.imag, f"$z_{{{k}}}$",
                color="C3", fontsize=11, ha="center", va="center")

from pathlib import Path
out = Path(__file__).parent / "fig13_roots_of_unity.png"
fig.savefig(out, dpi=120, bbox_inches="tight")
print(f"saved → {out}")
plt.show()
