"""fig04 — addition as the parallelogram rule."""
from _helpers import new_axes, arrow, point, save_and_show

fig, ax = new_axes((-1, 6), (-1, 5),
                   "Addition  =  parallelogram rule")

z = 3 + 1j
w = 1 + 2j
s = z + w  # 4 + 3i

# arrows from origin
arrow(ax, 0+0j, z, color="C0", label="z", lw=2)
arrow(ax, 0+0j, w, color="C1", label="w", lw=2)

# z + w as diagonal
arrow(ax, 0+0j, s, color="C3", label="z + w", lw=2.5)

# parallelogram completion (dashed)
ax.plot([z.real, s.real], [z.imag, s.imag],
        color="C1", linestyle="--", lw=1.5)
ax.plot([w.real, s.real], [w.imag, s.imag],
        color="C0", linestyle="--", lw=1.5)

point(ax, z, label="z = 3 + i", color="C0")
point(ax, w, label="w = 1 + 2i", color="C1")
point(ax, s, label="z + w = 4 + 3i", color="C3")

save_and_show(fig, "fig04_addition.png")
