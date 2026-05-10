# L03 — The Complex Plane and Geometric Interpretation

**Module**: 01 — Complex Numbers  
**Prerequisite**: L02 (addition, multiplication, conjugate, division on ℂ)  
**Feeds into**: L04 — Polar Form and Euler's Formula

---

## 1. MOTIVATION — why a picture at all

L01 defined `z = a + bi`. L02 made it an algebraic system: you can add, multiply, conjugate, divide.

But everything so far has been *symbolic*. You manipulated `a + bi` like a polynomial. You never asked: **where does `z` live?** Is `z = 3 + 4i` "near" `z = 3 + 5i`? Is `i` "between" `0` and `1`? Symbolically these questions have no meaning — `ℂ` is not ordered (L02, Trap 5).

The fix is to stop treating `z = a + bi` as a string of symbols and start treating it as a **point in a plane**:

```
z = a + bi   ↔   the point (a, b) ∈ ℝ²
```

Once you do this, three things happen at once:

1. Every complex number has a **location**.
2. Addition becomes **vector addition** (a picture you already know).
3. Multiplication becomes **rotation + scaling** — and *this* is the geometric fact that powers everything from AC circuits to quantum mechanics.

This lesson builds the picture. L04 uses the picture to derive polar form and Euler's formula.

> **Why this matters for QM:** quantum states are unit complex numbers (and later, unit vectors with complex entries). "Phase" is the *angle* in this plane. You cannot understand interference, superposition, or the Bloch sphere without first seeing complex numbers as points and arrows.

---

## 2. THE COMPLEX PLANE (ARGAND DIAGRAM)

**Definition.** The **complex plane** is `ℝ²` with the following labeling convention:

- horizontal axis = **real axis** (real part `Re(z) = a`)
- vertical axis  = **imaginary axis** (imaginary part `Im(z) = b`)

A complex number `z = a + bi` is plotted as the point `(a, b)`.

```
         Im
          │
        3 ┤        • z = 2 + 3i
        2 ┤
        1 ┤   • i
        0 ┼───•──•────── Re
       -1 ┤   1  2
       -2 ┤
              • z̄ = 2 − 3i
```

**Special points:**

| Symbol | Cartesian | Where |
|---|---|---|
| `0` | `(0, 0)` | origin |
| `1` | `(1, 0)` | unit on real axis |
| `i` | `(0, 1)` | unit on imaginary axis |
| `−1` | `(−1, 0)` | |
| `−i` | `(0, −1)` | |

**Visualize it:** run `figures/fig01_argand_basic.py`. It plots `0, 1, i, −1, −i, 2+3i, −1+2i, 3−i` on the plane with labels.

> **Note on terminology.** "Complex plane", "Argand diagram", and "Gauss plane" all mean the same thing. "Argand" is the most common name in physics texts.

---

## 3. MODULUS — `|z|` as DISTANCE

**Definition.** The **modulus** (or **absolute value**, or **magnitude**) of `z = a + bi` is

```
|z| = √(a² + b²)
```

Geometrically, `|z|` is the **Euclidean distance from `0` to the point `(a, b)`**. By Pythagoras, this is exactly the length of the arrow from the origin to `z`.

**Examples.**

- `|3 + 4i| = √(9 + 16) = √25 = 5`
- `|i| = √(0 + 1) = 1`
- `|−1| = √(1 + 0) = 1` (same as the real absolute value)
- `|0| = 0`

**Connection to the conjugate (from L02):**

```
|z|² = a² + b² = z · z̄
```

So `|z| = √(z · z̄)`. This identity is what makes division work — multiplying by `z̄/|z|²` is dividing by `z`.

**Properties.**

| Property | Statement |
|---|---|
| Non-negativity | `|z| ≥ 0`, with `|z| = 0 ⇔ z = 0` |
| Multiplicativity | `|zw| = |z|·|w|` |
| Triangle inequality | `|z + w| ≤ |z| + |w|` |
| Conjugate preserves modulus | `|z̄| = |z|` |

**Visualize it:** run `figures/fig02_modulus.py`. It draws the arrow from `0` to `z = 3 + 4i`, the right triangle with legs `3` and `4`, and labels the hypotenuse `|z| = 5`.

---

## 4. ARGUMENT — `arg(z)` as ANGLE

**Definition.** The **argument** of `z ≠ 0`, written `arg(z)` or `θ`, is the angle (measured counterclockwise) from the positive real axis to the arrow from `0` to `z`.

```
arg(z) = the angle θ such that
         a = |z|·cos(θ)
         b = |z|·sin(θ)
```

Equivalently, `tan(θ) = b/a` — but you must look at which **quadrant** `(a, b)` is in to pick the right `θ`. (Pure `arctan(b/a)` only works in quadrants I and IV.)

**Standard values.**

| `z` | `(a, b)` | `arg(z)` |
|---|---|---|
| `1` | `(1, 0)` | `0` |
| `i` | `(0, 1)` | `π/2` |
| `−1` | `(−1, 0)` | `π` |
| `−i` | `(0, −1)` | `3π/2` (or `−π/2`) |
| `1 + i` | `(1, 1)` | `π/4` |
| `−1 + i` | `(−1, 1)` | `3π/4` |

**Branch convention.** `arg(z)` is only defined up to multiples of `2π` (rotating by a full turn brings you back). To get a unique value, fix a range:

- **principal value** `Arg(z) ∈ (−π, π]` — most common in math/physics
- some texts use `[0, 2π)` instead

We'll use `Arg(z) ∈ (−π, π]` throughout this course unless stated otherwise.

**Why `arg(0)` is undefined.** The point `0` has no direction — there is no arrow to measure an angle from.

**Visualize it:** run `figures/fig03_argument.py`. It plots `1+i`, `−1+i`, `−1−i`, `1−i` and draws the angle arc from the positive real axis for each.

---

## 5. ADDITION = VECTOR ADDITION (the parallelogram rule)

**Claim.** If `z = a + bi` and `w = c + di`, then

```
z + w = (a + c) + (b + d)i
```

is the same as adding the position vectors `(a, b)` and `(c, d)` in `ℝ²`.

**Geometry — the parallelogram rule.** Draw the arrow from `0` to `z`. Then, starting at `z`, draw an arrow with the same length and direction as the arrow from `0` to `w`. The tip lands at `z + w`. The four points `0, z, z + w, w` form a parallelogram.

**Worked example.** `z = 3 + i`, `w = 1 + 2i`.

```
z + w = (3 + 1) + (1 + 2)i = 4 + 3i

Arrow from 0 to z:     →→→↑
Arrow from z to z+w:    ↑↑   (same as 0 → w)
Resulting arrow 0 → z+w: diagonal of the parallelogram
```

**Subtraction.** `z − w` is the arrow **from `w` to `z`**:

```
z − w = z + (−w)
```

`−w` is `w` rotated by `180°` (reflected through the origin), then added head-to-tail.

**Why this matters.** `|z − w|` is the **distance between the two points** `z` and `w` in the plane. This is the bridge between algebra and geometry: distances in `ℂ` are just moduli of differences, exactly as in `ℝ²`.

**Visualize it:** run `figures/fig04_addition.py` (parallelogram for `z + w`) and `figures/fig05_subtraction.py` (`z − w` as the arrow from `w` to `z`).

---

## 6. CONJUGATION = REFLECTION ACROSS THE REAL AXIS

**Claim.** If `z = a + bi`, then `z̄ = a − bi`. As a point, `(a, b) → (a, −b)` — the **reflection of `z` through the real axis**.

**Consequences (now visible at a glance):**

- `|z̄| = |z|` — reflection preserves length.
- `arg(z̄) = −arg(z)` — reflection negates the angle.
- `z` is real `⇔` `z = z̄` `⇔` `z` lies on the real axis.
- `z` is purely imaginary `⇔` `z = −z̄` `⇔` `z` lies on the imaginary axis.

**Visualize it:** run `figures/fig06_conjugate.py`. It plots `z = 2 + 3i` and `z̄ = 2 − 3i` with the real axis drawn as a mirror line.

---

## 7. MULTIPLICATION = ROTATION + SCALING (preview of L04)

This is the most important geometric fact in the entire module. We won't *prove* it fully here (the proof needs polar form, which is L04). But we can demonstrate it concretely.

### 7.1 Multiplying by `i` rotates by `90°`

Take any `z = a + bi`. Then

```
i · z = i · (a + bi) = ai + bi² = −b + ai
```

As a point: `(a, b) → (−b, a)`. That is exactly a `90°` counterclockwise rotation about the origin.

**Check on the basis points:**

```
i · 1 = i           (1, 0)  → (0, 1)    ✓
i · i = −1          (0, 1)  → (−1, 0)   ✓
i · (−1) = −i       (−1, 0) → (0, −1)   ✓
i · (−i) = 1        (0, −1) → (1, 0)    ✓
```

Multiplying by `i` four times brings you back: `i⁴ = 1`. That is a full `360°` rotation.

> **This is why `i` exists.** `i` is not a "fake number" — it is **the operation of rotating by a quarter turn**, written algebraically. Every other property of complex numbers follows from this single geometric fact.

### 7.2 Multiplying by a real number `r` scales by `r`

If `r ∈ ℝ`, then `r · z = (ra) + (rb)i`. The arrow from `0` to `z` is stretched by factor `r`. If `r < 0`, it also flips through the origin (which is a `180°` rotation).

### 7.3 General multiplication = rotate by `arg(w)`, then scale by `|w|`

The full statement (proved in L04):

```
|zw| = |z|·|w|             — moduli multiply
arg(zw) = arg(z) + arg(w)  — arguments add
```

**Concretely:** to multiply `z` by `w`, rotate the arrow `z` by the angle `arg(w)` and stretch its length by the factor `|w|`.

**Worked example.** `z = 1 + 0i = 1`, `w = 1 + i`.

- `|w| = √2`, `arg(w) = π/4` (45°).
- So `z · w = w` should be `z` rotated by `45°` and scaled by `√2`. Check: rotating the arrow `(1, 0)` by `45°` gives `(cos 45°, sin 45°) = (√2/2, √2/2)`. Scaling by `√2` gives `(1, 1) = 1 + i`. ✓

**Visualize it:** run `figures/fig07_multiplication.py`. It shows three multiplications side-by-side:

1. `z · i` — pure rotation by `90°`
2. `z · 2` — pure scaling by `2`
3. `z · (1 + i)` — rotation by `45°` plus scaling by `√2`

---

## 8. THE UNIT CIRCLE — a preview

The set of complex numbers with `|z| = 1` is the **unit circle** in the plane.

```
{ z ∈ ℂ : |z| = 1 }
```

Everything on this circle has the form `cos(θ) + i sin(θ)` for some angle `θ`. This is the seed of polar form (L04) and of Euler's formula `e^(iθ) = cos(θ) + i sin(θ)`.

**Why it matters:** in QM, a quantum state's overall phase is a point on the unit circle. Multiplying by such a phase is a *pure rotation* — it changes nothing physical (probabilities are `|·|²`). But *relative* phases between two states control interference. None of that language is sayable without this picture.

**Visualize it:** run `figures/fig08_unit_circle.py`. It draws the unit circle and marks `1, i, −1, −i, e^(iπ/4), e^(iπ/3)`.

---

## 9. COMMON TRAPS

**Trap 1 — confusing `Re(z)` with `|z|`.**  
`Re(3 + 4i) = 3`, but `|3 + 4i| = 5`. These coincide *only* on the real axis (`b = 0`).

**Trap 2 — using `arctan(b/a)` blindly.**  
For `z = −1 − i`, `b/a = 1`, so `arctan` returns `π/4`. But `(−1, −1)` is in quadrant III — the actual `arg(z) = −3π/4` (or `5π/4`). Always check the quadrant.

**Trap 3 — thinking `arg(z + w) = arg(z) + arg(w)`.**  
False. Arguments add under **multiplication**, not addition. Addition is the parallelogram rule, which has no clean angle formula.

**Trap 4 — `|z + w| = |z| + |w|`.**  
False in general — only true when `z` and `w` point in the same direction (same argument). The triangle inequality is `|z + w| ≤ |z| + |w|`, with equality only in the colinear case.

**Trap 5 — forgetting that `arg` is multi-valued.**  
`arg(1) ∈ {0, 2π, 4π, −2π, ...}`. When a formula seems to give "two different answers" they probably differ by `2π`. Pick a branch and stick with it.

---

## 10. EXERCISES

E1. Plot the following on the complex plane (just sketch, or run a script): `2 + i`, `−3 + 2i`, `−1 − i`, `4 − 3i`, `2i`, `−5`. Compute `|z|` for each.

E2. Compute `arg(z)` (principal value in `(−π, π]`) for `z = 1 + i`, `z = −1 + i`, `z = −1 − i`, `z = 1 − i`.

E3. Let `z = 2 + 3i`, `w = 1 − i`. Compute `z + w`, `z − w`, `|z − w|`, and describe `z − w` geometrically.

E4. Verify that multiplying by `i` rotates by `90°` for `z = 2 + 3i`. Compute `iz` algebraically, plot both, and confirm the angle changed by `π/2`.

E5. Find all complex numbers `z` with `|z| = 2` and `arg(z) = π/3`. Write `z` in the form `a + bi`.

---

## 11. SOLUTIONS

**E1.**

| `z` | `(a, b)` | `|z|` |
|---|---|---|
| `2 + i` | `(2, 1)` | `√5` |
| `−3 + 2i` | `(−3, 2)` | `√13` |
| `−1 − i` | `(−1, −1)` | `√2` |
| `4 − 3i` | `(4, −3)` | `5` |
| `2i` | `(0, 2)` | `2` |
| `−5` | `(−5, 0)` | `5` |

Run `figures/fig_ex01.py` to see all six plotted.

**E2.**

| `z` | quadrant | `arg(z)` |
|---|---|---|
| `1 + i` | I | `π/4` |
| `−1 + i` | II | `3π/4` |
| `−1 − i` | III | `−3π/4` |
| `1 − i` | IV | `−π/4` |

Notice all four lie on the circle `|z| = √2` and are spaced by `π/2`. They are exactly `√2 · {1, i, −1, −i}`.

**E3.** `z + w = 3 + 2i`. `z − w = 1 + 4i`. `|z − w| = √(1 + 16) = √17`.  
Geometrically, `z − w` is the arrow **from `w` to `z`**, and its length `√17` is the distance between the points `(2, 3)` and `(1, −1)` in the plane. Verify: `√((2−1)² + (3−(−1))²) = √(1 + 16) = √17`. ✓

**E4.** `iz = i(2 + 3i) = 2i + 3i² = −3 + 2i`. As a point: `(2, 3) → (−3, 2)`.  
Check the angle:
- `arg(z) = arctan(3/2) ≈ 0.983 rad ≈ 56.3°`
- `arg(iz) = arctan(2/(−3))` in Q II `= π − arctan(2/3) ≈ π − 0.588 ≈ 2.554 rad ≈ 146.3°`
- Difference: `146.3° − 56.3° = 90°`. ✓

Length unchanged: `|z| = √13`, `|iz| = √(9+4) = √13`. ✓

**E5.** With `|z| = 2` and `arg(z) = π/3`:

```
a = |z|·cos(π/3) = 2 · (1/2) = 1
b = |z|·sin(π/3) = 2 · (√3/2) = √3
z = 1 + √3·i
```

Check: `|z| = √(1 + 3) = 2` ✓. And `tan(arg(z)) = √3/1 = √3 = tan(π/3)` ✓ (and quadrant I, so `arg = +π/3` not `−2π/3`).

---

## 12. NEXT — L04: Polar Form and Euler's Formula

L03 made every `z ∈ ℂ` a point with a length `|z|` and an angle `arg(z)`. L04 turns this picture into a second algebraic notation:

```
z = r·(cos θ + i sin θ) = r·e^(iθ)
```

In this form, multiplication becomes trivial — you just multiply lengths and add angles, exactly as Section 7.3 promised. Euler's formula `e^(iθ) = cos θ + i sin θ` is the bridge, and it is the single most important identity in this entire course.

---

## Figures index

All scripts are in `module_01_complex_numbers/figures/`. Each is standalone — `python3 figXX_name.py` saves a PNG next to the script and shows it.

| Script | What it draws |
|---|---|
| `fig01_argand_basic.py` | Several points on the complex plane with labels |
| `fig02_modulus.py` | `|3 + 4i| = 5` as the hypotenuse of a 3-4-5 triangle |
| `fig03_argument.py` | `arg(z)` as the angle from the positive real axis (4 quadrants) |
| `fig04_addition.py` | Parallelogram rule: `z + w` |
| `fig05_subtraction.py` | `z − w` as the arrow from `w` to `z` |
| `fig06_conjugate.py` | Conjugation as reflection across the real axis |
| `fig07_multiplication.py` | Three panels: `z·i`, `z·2`, `z·(1+i)` — rotate/scale |
| `fig08_unit_circle.py` | The unit circle with marked points |
| `fig_ex01.py` | E1 — six plotted points |
