"""fig02 — |3 + 4i| = 5 as the hypotenuse of a 3-4-5 right triangle."""
from _helpers import new_axes, arrow, point, save_and_show

fig, ax = new_axes((-1, 5), (-1, 5), "Modulus  |z|  =  distance from 0")

z = 3 + 4j

# right triangle legs
ax.plot([0, 3], [0, 0], color="gray", lw=1.5)        # horizontal leg
ax.plot([3, 3], [0, 4], color="gray", lw=1.5)        # vertical leg
ax.text(1.5, -0.3, "a = 3", color="gray", ha="center")
ax.text(3.15, 2.0, "b = 4", color="gray")

# hypotenuse = arrow from 0 to z
arrow(ax, 0+0j, z, color="C3", label="|z| = 5", lw=2.5)
point(ax, z, label="z = 3 + 4i", color="C3")
point(ax, 0+0j, label="0")

ax.text(0.4, 4.2, "|z| = √(a² + b²) = √25 = 5",
        fontsize=11, color="C3")

save_and_show(fig, "fig02_modulus.png")
