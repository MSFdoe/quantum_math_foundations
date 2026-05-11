# Equations Cheatsheet — Quantum Math Foundations

Quick reference for exercises. Grows as we go.

---

## Module 01 — Complex Numbers

### L01 — The Problem with Real Numbers

**Defining property of `i`:**
$$i^2 = -1$$

**Standard form of a complex number:**
$$z = a + bi, \quad a, b \in \mathbb{R}$$

- `a` = real part = `Re(z)`
- `b` = imaginary part = `Im(z)`

**Set of complex numbers:**
$$\mathbb{C} = \{a + bi : a, b \in \mathbb{R}\}$$

**Equality:**
$$a + bi = c + di \iff a = c \text{ and } b = d$$

**Powers of `i` (cycle of 4):**
$$i^1 = i, \quad i^2 = -1, \quad i^3 = -i, \quad i^4 = 1$$
$$i^n = i^{n \bmod 4}$$

---

### L02 — Arithmetic of Complex Numbers

**Addition:**
$$(a + bi) + (c + di) = (a + c) + (b + d)i$$

**Subtraction:**
$$(a + bi) - (c + di) = (a - c) + (b - d)i$$

**Multiplication:**
$$(a + bi)(c + di) = (ac - bd) + (ad + bc)i$$

**Complex conjugate:**
$$\overline{z} = \overline{a + bi} = a - bi$$

**Key conjugate identity (always real, ≥ 0):**
$$z \cdot \overline{z} = a^2 + b^2$$

**Conjugate properties:**
$$\overline{z + w} = \overline{z} + \overline{w}$$
$$\overline{z \cdot w} = \overline{z} \cdot \overline{w}$$
$$\overline{\overline{z}} = z$$

**Division (multiply top and bottom by conjugate of denominator):**
$$\frac{a + bi}{c + di} = \frac{(a + bi)(c - di)}{c^2 + d^2} = \frac{ac + bd}{c^2 + d^2} + \frac{bc - ad}{c^2 + d^2}\,i$$

**Reciprocal:**
$$\frac{1}{z} = \frac{\overline{z}}{z \cdot \overline{z}} = \frac{a - bi}{a^2 + b^2}$$

---

### L03 — The Complex Plane and Geometric Interpretation

**Argand diagram:** `z = a + bi` plotted as point `(a, b)` in the plane (real axis horizontal, imaginary axis vertical).

**Modulus (absolute value, length):**
$$|z| = \sqrt{a^2 + b^2}$$

**Modulus via conjugate:**
$$|z|^2 = z \cdot \overline{z}$$

**Modulus properties:**
$$|z \cdot w| = |z| \cdot |w|$$
$$\left|\frac{z}{w}\right| = \frac{|z|}{|w|} \quad (w \neq 0)$$
$$|\overline{z}| = |z|$$
$$|z + w| \leq |z| + |w| \quad \text{(triangle inequality)}$$

**Argument (angle from positive real axis, principal value in `(−π, π]`):**
$$\arg(z) = \theta \quad \text{such that} \quad \tan\theta = \frac{b}{a}$$

**Quadrant-aware argument** (use `atan2(b, a)`, NOT plain `atan(b/a)`):
- Q1 (`a > 0, b > 0`): `arg = atan(b/a)`
- Q2 (`a < 0, b > 0`): `arg = atan(b/a) + π`
- Q3 (`a < 0, b < 0`): `arg = atan(b/a) − π`
- Q4 (`a > 0, b < 0`): `arg = atan(b/a)`

**Argument of conjugate:**
$$\arg(\overline{z}) = -\arg(z)$$

**Addition = parallelogram rule:** `z + w` is the diagonal of the parallelogram spanned by `z` and `w` from the origin.

**Distance between two points:**
$$\text{dist}(z, w) = |z - w|$$

**Conjugation = reflection across the real axis.**

**Multiplication = rotation + scaling:**
- Multiplying by `i` rotates by `+90°` (π/2).
- Multiplying by real `r > 0` scales by `r`.
- Multiplying by general `w`: rotates by `arg(w)` and scales by `|w|`.

**Unit circle:** set of all `z` with `|z| = 1`. Multiplying by a unit-circle point is pure rotation, no scaling. (Polar form / Euler comes in L04.)

---

### L04 — Polar Form and Euler's Formula

**Polar form (cartesian ↔ polar):**
$$a = r\cos\theta, \qquad b = r\sin\theta$$
$$z = r(\cos\theta + i\sin\theta)$$

**Euler's formula:**
$$e^{i\theta} = \cos\theta + i\sin\theta$$

**Polar form (compact):**
$$z = r\,e^{i\theta}, \quad r = |z|, \quad \theta = \arg(z)$$

**Euler's identity (`θ = π`):**
$$e^{i\pi} + 1 = 0$$

**Multiplication (moduli multiply, arguments add):**
$$z\,w = r_1 r_2 \, e^{i(\theta_1 + \theta_2)}$$
$$|zw| = |z|\cdot|w|, \qquad \arg(zw) = \arg(z) + \arg(w)$$

**Division:**
$$\frac{z}{w} = \frac{r_1}{r_2}\, e^{i(\theta_1 - \theta_2)}$$

**Conjugation in polar form:**
$$\overline{r\,e^{i\theta}} = r\,e^{-i\theta}$$

**De Moivre's theorem (integer powers):**
$$z^n = r^n\, e^{i\,n\theta}$$
$$\big(r(\cos\theta + i\sin\theta)\big)^n = r^n(\cos n\theta + i\sin n\theta)$$

**`n`-th roots of `w = R·e^(iφ)`:**
$$z_k = R^{1/n}\, e^{i(\varphi + 2\pi k)/n}, \qquad k = 0, 1, \ldots, n-1$$

**`n`-th roots of unity:**
$$z_k = e^{i\,2\pi k / n}, \qquad k = 0, 1, \ldots, n-1$$
$$\sum_{k=0}^{n-1} z_k = 0 \quad (n \geq 2)$$

**Note:** all angles in **radians**. Principal value of `arg(z)` lives in `(−π, π]`. Polar form requires `z ≠ 0`.

---

*Last updated: 2026-05-11 — covers L01, L02, L03, L04.*
