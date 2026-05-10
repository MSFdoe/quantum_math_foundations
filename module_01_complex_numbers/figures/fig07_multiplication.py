"""fig07 — multiplication as rotation + scaling.

Three panels:
  (a) z · i        — pure rotation by 90°
  (b) z · 2        — pure scaling by 2
  (c) z · (1 + i)  — rotation by 45° and scaling by √2
"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


def setup(ax, title, lim=4):
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_aspect("equal")
    ax.grid(True, linestyle=":", alpha=0.5)
    ax.axhline(0, color="black", lw=0.8)
    ax.axvline(0, color="black", lw=0.8)
    ax.set_title(title)
    ax.set_xlabel("Re")
    ax.set_ylabel("Im")


def arrow(ax, z_from, z_to, color, lw=2):
    ax.annotate("", xy=(z_to.real, z_to.imag),
                xytext=(z_from.real, z_from.imag),
                arrowprops=dict(arrowstyle="->", color=color, lw=lw))


def label(ax, z, text, color):
    ax.plot(z.real, z.imag, "o", color=color, markersize=6)
    ax.text(z.real + 0.15, z.imag + 0.15, text, color=color, fontsize=10)


fig, axes = plt.subplots(1, 3, figsize=(15, 5))

z = 2 + 1j

# panel (a): z · i
ax = axes[0]
setup(ax, "z · i  →  rotate 90°")
zi = z * 1j
arrow(ax, 0+0j, z, "C0")
arrow(ax, 0+0j, zi, "C3")
label(ax, z, "z = 2 + i", "C0")
label(ax, zi, "iz = −1 + 2i", "C3")
# arc showing rotation
t = np.linspace(np.angle(z), np.angle(zi), 30)
r = abs(z) * 0.6
ax.plot(r*np.cos(t), r*np.sin(t), color="C3", lw=1.5)

# panel (b): z · 2
ax = axes[1]
setup(ax, "z · 2  →  scale by 2")
z2 = z * 2
arrow(ax, 0+0j, z, "C0")
arrow(ax, 0+0j, z2, "C3", lw=2)
label(ax, z, "z = 2 + i", "C0")
label(ax, z2, "2z = 4 + 2i", "C3")

# panel (c): z · (1 + i)
ax = axes[2]
setup(ax, "z · (1 + i)  →  rotate 45°, scale √2")
w = 1 + 1j
zw = z * w
arrow(ax, 0+0j, z, "C0")
arrow(ax, 0+0j, zw, "C3", lw=2)
label(ax, z, "z = 2 + i", "C0")
label(ax, zw, f"z·w = {int(zw.real)} + {int(zw.imag)}i", "C3")
# arc
t = np.linspace(np.angle(z), np.angle(zw), 30)
r = abs(z) * 0.7
ax.plot(r*np.cos(t), r*np.sin(t), color="C3", lw=1.5)

fig.suptitle("Multiplication = rotate by arg(w), scale by |w|",
             fontsize=13)
fig.tight_layout()

out = Path(__file__).parent / "fig07_multiplication.png"
fig.savefig(out, dpi=120, bbox_inches="tight")
print(f"saved → {out}")
plt.show()
