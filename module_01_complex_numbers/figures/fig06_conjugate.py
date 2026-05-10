"""fig06 — conjugation as reflection across the real axis."""
from _helpers import new_axes, arrow, point, save_and_show

fig, ax = new_axes((-1, 4), (-4, 4),
                   "Conjugation  =  reflection across the real axis")

z = 2 + 3j
zbar = z.conjugate()  # 2 - 3i

arrow(ax, 0+0j, z, color="C0", lw=2)
arrow(ax, 0+0j, zbar, color="C2", lw=2)

# vertical dashed line connecting z and z̄
ax.plot([z.real, zbar.real], [z.imag, zbar.imag],
        color="gray", linestyle="--", lw=1.5)

# emphasize the real axis as the mirror line
ax.axhline(0, color="red", linewidth=1.5, alpha=0.6)
ax.text(3.2, 0.1, "mirror", color="red", fontsize=10)

point(ax, z, label="z = 2 + 3i", color="C0")
point(ax, zbar, label="z̄ = 2 − 3i", color="C2")

ax.text(0.2, 3.5, "|z̄| = |z|       arg(z̄) = −arg(z)",
        fontsize=11)

save_and_show(fig, "fig06_conjugate.png")
