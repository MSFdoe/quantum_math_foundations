# L04 — Polar Form and Euler's Formula

> **Goal of this lesson.** Rewrite every complex number as a length and an angle, prove Euler's formula `e^(iθ) = cos θ + i sin θ`, and discover that multiplication of complex numbers is just addition of angles. This is the most important single result of Module 01 — every quantum state we will ever write down is a complex exponential.

---

## 1. Motivation — why cartesian form is the wrong language for rotation

In L03 we found that multiplying by `i` rotates by 90°, multiplying by `r > 0` scales by `r`, and multiplying by a general `w` rotates by `arg(w)` and scales by `|w|`.

But to *prove* that, in cartesian form, we had to multiply out `(a + bi)(c + di)` and stare at the result. The cartesian form `a + bi` hides the geometry. We need a notation in which **length** and **angle** are written down directly.

That notation is **polar form**.

---

## 2. Polar form

Any non-zero complex number `z = a + bi` is determined by two numbers:

- its **modulus** `r = |z| = √(a² + b²)` — how far it is from the origin
- its **argument** `θ = arg(z)` — the angle from the positive real axis

The link back to cartesian:
$$a = r\cos\theta, \qquad b = r\sin\theta$$

So:
$$z = a + bi = r\cos\theta + i\,r\sin\theta = r(\cos\theta + i\sin\theta)$$

This is **polar form**.

$$\boxed{\;z = r(\cos\theta + i\sin\theta)\;}$$

The factor `(cos θ + i sin θ)` is a **point on the unit circle** at angle `θ`. The factor `r` then stretches it out to the correct length.

### Worked example

`z = 1 + i`.

- `r = √(1² + 1²) = √2`
- `θ = arg(1 + i) = π/4` (first quadrant, equal real and imaginary parts)

Check: `r(cos θ + i sin θ) = √2 (cos(π/4) + i sin(π/4)) = √2 · (√2/2 + i·√2/2) = 1 + i`. ✓

---

## 3. Euler's formula — the central identity

Define the complex exponential by extending the real Taylor series of `eˣ`:
$$e^{x} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots$$

Now plug in `x = iθ` (purely imaginary). Use `i² = −1`, `i³ = −i`, `i⁴ = 1` to collect terms:

$$
e^{i\theta} = 1 + i\theta + \frac{(i\theta)^2}{2!} + \frac{(i\theta)^3}{3!} + \frac{(i\theta)^4}{4!} + \cdots
$$

Separating real and imaginary parts:

$$
e^{i\theta} = \underbrace{\left(1 - \frac{\theta^2}{2!} + \frac{\theta^4}{4!} - \cdots\right)}_{=\cos\theta} + i\,\underbrace{\left(\theta - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} - \cdots\right)}_{=\sin\theta}
$$

Those are exactly the Taylor series of `cos θ` and `sin θ`. So:

$$\boxed{\;e^{i\theta} = \cos\theta + i\sin\theta\;}$$

This is **Euler's formula**.

Combined with polar form:

$$\boxed{\;z = r\,e^{i\theta}\;}$$

Every non-zero complex number is one length `r` times one complex exponential `e^(iθ)`.

### Euler's identity (the special case `θ = π`)

$$e^{i\pi} + 1 = 0$$

Five constants — `0, 1, i, π, e` — in one equation. It is `θ = π` plugged into Euler's formula: `e^(iπ) = cos π + i sin π = −1`.

---

## 4. Multiplication in polar form — the payoff

Take two complex numbers in polar form:
$$z = r_1 e^{i\theta_1}, \qquad w = r_2 e^{i\theta_2}$$

Multiply them like exponentials:
$$z \cdot w = r_1 r_2 \, e^{i(\theta_1 + \theta_2)}$$

**Multiplying complex numbers multiplies their moduli and adds their arguments.**

$$\boxed{\;|zw| = |z|\cdot|w|, \qquad \arg(zw) = \arg(z) + \arg(w)\;}$$

This is the result L03 hinted at — now it is a one-line consequence of `e^a · e^b = e^(a+b)`.

### Division

$$\frac{z}{w} = \frac{r_1}{r_2}\, e^{i(\theta_1 - \theta_2)}$$

Divide moduli, subtract arguments.

### Conjugation

$$\overline{r\,e^{i\theta}} = r\,e^{-i\theta}$$

Flipping the sign of `θ` is reflection across the real axis — same fact as L03, now obvious.

---

## 5. Powers — De Moivre's theorem

Apply multiplication `n` times to `z = r·e^(iθ)`:

$$z^n = r^n\, e^{i\,n\theta}$$

Spelled out without exponentials:

$$\boxed{\;\big(r(\cos\theta + i\sin\theta)\big)^n = r^n(\cos n\theta + i\sin n\theta)\;}$$

This is **De Moivre's theorem**. To raise a complex number to the `n`-th power: raise the modulus to the `n`-th power, multiply the angle by `n`.

### Worked example

`(1 + i)^8`.

`1 + i = √2 · e^(iπ/4)`, so `(1+i)^8 = (√2)^8 · e^(i · 8 · π/4) = 16 · e^(i2π) = 16`. Done — no eight-fold cartesian expansion required.

---

## 6. Roots — going the other way

If `z^n = w`, how many `z`s solve it? Exactly `n` of them, evenly spaced around a circle.

Write `w = R·e^(iφ)`. Then the `n` solutions are:

$$z_k = R^{1/n}\, e^{i(\varphi + 2\pi k)/n}, \qquad k = 0, 1, 2, \ldots, n-1$$

All `n` roots lie on a circle of radius `R^(1/n)`, separated by an angle of `2π/n`.

### The `n`-th roots of unity

Special case `w = 1`, so `R = 1`, `φ = 0`:

$$z_k = e^{i\,2\pi k / n}, \qquad k = 0, 1, \ldots, n-1$$

These are `n` points on the unit circle forming a regular `n`-gon with one vertex at `z₀ = 1`.

- `n = 2`: `{1, −1}` — two points on the real axis.
- `n = 3`: `{1, e^(i2π/3), e^(i4π/3)}` — equilateral triangle.
- `n = 4`: `{1, i, −1, −i}` — square.

---

## 7. Why this matters for quantum mechanics

A quantum state in the simplest case is a unit-length complex number — a point on the unit circle:
$$|\psi\rangle = e^{i\theta}$$

Time evolution multiplies this state by another unit-length complex exponential, `e^(−iEt/ℏ)`. So **time evolution is rotation in the complex plane**.

This is the entire reason quantum mechanics is built on complex numbers. Real numbers can scale; only complex numbers (via Euler) can rotate continuously. We will see this come back in Modules 06 and 07.

---

## 8. Traps

1. **Confusing degrees and radians.** All formulas above use radians. `θ = π/4` not `θ = 45`. Calculators in degree mode produce nonsense here.
2. **Forgetting the principal-value branch.** `arg(z)` lives in `(−π, π]`. When you compute `arg(z) + arg(w)` it can fall outside that range — you must add or subtract `2π` to bring it back.
3. **Polar form of `0`.** `0` has modulus `0` but no defined argument. Polar form `r·e^(iθ)` only works for `z ≠ 0`.
4. **De Moivre for non-integer `n`.** `(r e^(iθ))^n = r^n e^(inθ)` is unambiguous for integer `n`. For fractional `n` you must use the full root formula in §6 — there is no single "the" answer, there are `n` of them.
5. **`e^(iθ)` is not always 1.** It has modulus 1, but it equals 1 only when `θ` is a multiple of `2π`.

---

## 9. Exercises

**E1.** Convert to polar form `r·e^(iθ)`:
(a) `z = 1 + i√3`
(b) `z = −2`
(c) `z = −1 − i`
(d) `z = 3i`

**E2.** Convert back to cartesian form `a + bi`:
(a) `z = 2·e^(iπ/3)`
(b) `z = e^(iπ)`
(c) `z = √2 · e^(i·3π/4)`

**E3.** Compute using polar form (no cartesian expansion):
(a) `(1 + i)^{10}`
(b) `(√3 + i)^6`

**E4.** Find all solutions of `z^3 = 8`. Plot them mentally — what shape do they form?

**E5.** Find all 4th roots of unity. Verify that their sum is `0`. (This generalises: the sum of the `n`-th roots of unity is `0` for every `n ≥ 2` — a useful fact.)

---

## 10. Solutions

**E1.**
(a) `r = √(1 + 3) = 2`, `θ = arctan(√3/1) = π/3`. So `z = 2·e^(iπ/3)`.
(b) `r = 2`, `θ = π`. `z = 2·e^(iπ)`.
(c) `r = √2`, third quadrant, so `θ = −3π/4` (or equivalently `5π/4`, but principal value is `−3π/4`). `z = √2·e^(−i3π/4)`.
(d) `r = 3`, `θ = π/2`. `z = 3·e^(iπ/2)`.

**E2.**
(a) `2(cos(π/3) + i sin(π/3)) = 2(1/2 + i·√3/2) = 1 + i√3`.
(b) `cos π + i sin π = −1`.
(c) `√2 (cos(3π/4) + i sin(3π/4)) = √2(−√2/2 + i·√2/2) = −1 + i`.

**E3.**
(a) `1 + i = √2 · e^(iπ/4)`, so `(1+i)^{10} = (√2)^{10} · e^(i·10π/4) = 32 · e^(i·5π/2) = 32 · e^(iπ/2) = 32i`.
(b) `√3 + i = 2·e^(iπ/6)`, so `(√3+i)^6 = 64 · e^(iπ) = −64`.

**E4.** Write `8 = 8·e^(i·0)`, so the three cube roots are `z_k = 8^{1/3} · e^(i·2πk/3) = 2·e^(i·2πk/3)` for `k = 0, 1, 2`. Explicitly:
- `z₀ = 2`
- `z₁ = 2·e^(i·2π/3) = −1 + i√3`
- `z₂ = 2·e^(i·4π/3) = −1 − i√3`

They form an equilateral triangle of radius 2 centred at the origin.

**E5.** Fourth roots of unity: `z_k = e^(i·2πk/4) = e^(iπk/2)` for `k = 0, 1, 2, 3` — namely `{1, i, −1, −i}`. Sum: `1 + i − 1 − i = 0`. ✓

---

## 11. Figures index

Run from `module_01_complex_numbers/figures/`:

- `fig09_polar_basic.py` — a point shown with both `(a, b)` and `(r, θ)`
- `fig10_euler.py` — the unit circle traced out by `e^(iθ)` as `θ` runs from `0` to `2π`
- `fig11_polar_multiplication.py` — two numbers multiplied: angles add, moduli multiply
- `fig12_de_moivre.py` — `z^n` for `z` on the unit circle traces a regular pattern
- `fig13_roots_of_unity.py` — the 3rd, 4th, 5th, 6th roots of unity as regular polygons

---

*Next: L05 deepens this into more general functions on the complex plane and sets up Module 02 (vectors).*
