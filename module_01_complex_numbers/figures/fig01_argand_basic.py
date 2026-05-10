"""fig01 — basic Argand diagram with labeled points."""
from _helpers import new_axes, point, save_and_show

fig, ax = new_axes((-4, 4), (-4, 4), "The complex plane — basic points")

points = {
    "0":        0 + 0j,
    "1":        1 + 0j,
    "i":        0 + 1j,
    "-1":      -1 + 0j,
    "-i":       0 - 1j,
    "2 + 3i":   2 + 3j,
    "-1 + 2i": -1 + 2j,
    "3 - i":    3 - 1j,
}
for label, z in points.items():
    point(ax, z, label=label)

save_and_show(fig, "fig01_argand_basic.png")
