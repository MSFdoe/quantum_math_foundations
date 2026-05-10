"""fig_ex01 — Exercise 1: plot the six given points and show their moduli."""
from _helpers import new_axes, point, save_and_show

fig, ax = new_axes((-6, 6), (-4, 4), "E1 — six points and their moduli")

points = [
    (2 + 1j,   "2 + i",    "√5"),
    (-3 + 2j,  "−3 + 2i",  "√13"),
    (-1 - 1j,  "−1 − i",   "√2"),
    (4 - 3j,   "4 − 3i",   "5"),
    (0 + 2j,   "2i",       "2"),
    (-5 + 0j,  "−5",       "5"),
]
for z, lab, modulus in points:
    point(ax, z, label=f"{lab}  |z|={modulus}")

save_and_show(fig, "fig_ex01.png")
