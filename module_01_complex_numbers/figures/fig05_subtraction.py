"""fig05 — z − w as the arrow from w to z."""
from _helpers import new_axes, arrow, point, save_and_show

fig, ax = new_axes((-2, 5), (-3, 5),
                   "Subtraction  z − w  =  arrow from w to z")

z = 2 + 3j
w = 1 - 1j
diff = z - w  # 1 + 4i

# arrows from origin
arrow(ax, 0+0j, z, color="C0", label="z", lw=2)
arrow(ax, 0+0j, w, color="C1", label="w", lw=2)

# z - w as displacement from w to z
arrow(ax, w, z, color="C3", label="z − w", lw=2.5)

# also drawn from origin (same vector, parallel)
arrow(ax, 0+0j, diff, color="C3", lw=1.5)

point(ax, z, label="z = 2 + 3i", color="C0")
point(ax, w, label="w = 1 − i", color="C1")
point(ax, diff, label="z − w = 1 + 4i", color="C3")

ax.text(0.5, -2.5, f"|z − w| = √17 ≈ {abs(diff):.3f}",
        fontsize=11, color="C3")

save_and_show(fig, "fig05_subtraction.png")
