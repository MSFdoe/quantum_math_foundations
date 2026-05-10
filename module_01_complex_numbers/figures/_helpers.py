"""Shared plotting helpers for Module 01 figures."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


def new_axes(xlim=(-5, 5), ylim=(-5, 5), title=""):
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.grid(True, linestyle=":", alpha=0.5)
    ax.axhline(0, color="black", linewidth=0.8)
    ax.axvline(0, color="black", linewidth=0.8)
    ax.set_xlabel("Re")
    ax.set_ylabel("Im")
    if title:
        ax.set_title(title)
    return fig, ax


def arrow(ax, z_from, z_to, color="C0", label=None, lw=2):
    """Draw an arrow from z_from to z_to (both complex numbers)."""
    dx = z_to.real - z_from.real
    dy = z_to.imag - z_from.imag
    ax.annotate(
        "",
        xy=(z_to.real, z_to.imag),
        xytext=(z_from.real, z_from.imag),
        arrowprops=dict(arrowstyle="->", color=color, lw=lw),
    )
    if label:
        mx = z_from.real + dx * 0.5
        my = z_from.imag + dy * 0.5
        ax.text(mx, my, label, color=color, fontsize=12,
                ha="center", va="bottom")


def point(ax, z, label=None, color="C0", offset=(0.15, 0.15)):
    ax.plot(z.real, z.imag, "o", color=color, markersize=7)
    if label:
        ax.text(z.real + offset[0], z.imag + offset[1], label,
                color=color, fontsize=12)


def save_and_show(fig, filename):
    out = Path(__file__).parent / filename
    fig.savefig(out, dpi=120, bbox_inches="tight")
    print(f"saved → {out}")
    plt.show()
