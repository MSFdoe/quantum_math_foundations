# L01 — The Problem With Real Numbers

**Module**: 01 — Complex Numbers  
**Prerequisite**: Algebra (polynomials, square roots)  
**Feeds into**: L02 — Arithmetic of Complex Numbers

---

## 1. MOTIVATION

You have been using real numbers your entire engineering career. They describe force, velocity, temperature, pressure — every physical quantity you have measured. The real number line is complete in the sense that between any two reals there is another real.

But there is a specific, unavoidable algebraic operation that the real numbers cannot close under: **taking the square root of a negative number**.

This is not a matter of taste or convention. It is a structural gap. Close that gap, and you get complex numbers. Complex numbers then turn out to describe wave mechanics, oscillations, and quantum states — not because someone forced them to, but because the physics demands them.

---

## 2. THE GAP — WHERE REAL NUMBERS BREAK

Start with the simplest polynomial:

```
x² = 4
```

Two solutions: `x = 2` and `x = -2`. Both real. No problem.

Now shift by one:

```
x² = 1
```

Two solutions: `x = 1` and `x = -1`. Still real.

Now shift to zero:

```
x² = 0
```

One solution: `x = 0`. Still real.

Now cross zero:

```
x² = -1
```

No solution on the real line. Squaring any real number — positive, negative, or zero — always gives a non-negative result:

```
(positive)² = positive
(negative)² = positive
(0)²        = 0
```

There is no real number whose square is negative. The real line has a structural gap here.

---

## 3. WHY THIS MATTERS — THE FUNDAMENTAL THEOREM OF ALGEBRA

There is a theorem that states:

> Every polynomial of degree `n` has exactly `n` roots, counting multiplicity.

A degree-2 polynomial has 2 roots. A degree-5 polynomial has 5 roots.

But `x² + 1 = 0` is a degree-2 polynomial. It has no real roots. If the theorem is to hold, those roots must exist somewhere outside the reals.

This is not a choice — it is a mathematical necessity if you want algebra to be complete.

---

## 4. THE DEFINITION OF i

Define a new symbol `i` with exactly one rule:

```
i² = -1
```

`i` is called the **imaginary unit**. The name is historical and misleading — it is not imaginary in any physical sense. It is simply a new algebraic object that fills the gap the reals leave open.

From this single rule:

```
i¹ = i
i² = -1
i³ = i² · i = -1 · i = -i
i⁴ = i² · i² = (-1)(-1) = 1
i⁵ = i⁴ · i = 1 · i = i
```

The powers of `i` cycle with period 4: `i, -1, -i, 1, i, -1, -i, 1, ...`

This cycle is not an accident — it will become rotation by 90° in the complex plane.

---

## 5. THE COMPLEX NUMBER

A **complex number** is any expression of the form:

```
z = a + bi
```

Where:
- `a ∈ ℝ` — the **real part**, written `Re(z)`
- `b ∈ ℝ` — the **imaginary part**, written `Im(z)`
- `i` — the imaginary unit, `i² = -1`

The set of all complex numbers is written `ℂ`.

Real numbers are a subset: when `b = 0`, `z = a + 0i = a`. So `ℝ ⊂ ℂ`.

---

## 6. THE EQUATION x² = -1 IS NOW SOLVABLE

```
x² = -1
x = ±i
```

Verify:
```
i²  = -1  ✓
(-i)² = (-1)²(i²) = (1)(-1) = -1  ✓
```

The degree-2 polynomial `x² + 1` now has exactly 2 roots: `i` and `-i`. The Fundamental Theorem of Algebra holds.

---

## 7. WORKED EXAMPLES

**Example 1**: Identify real and imaginary parts.

```
z = 5 + 3i     →   Re(z) = 5,   Im(z) = 3
z = -2 - 7i    →   Re(z) = -2,  Im(z) = -7
z = 4          →   Re(z) = 4,   Im(z) = 0
z = -i         →   Re(z) = 0,   Im(z) = -1
z = 0          →   Re(z) = 0,   Im(z) = 0
```

Note: `Im(z)` is the coefficient of `i`, not the full term. `Im(3i) = 3`, not `3i`.

**Example 2**: Compute powers of `i`.

```
i⁷ = i⁴ · i³ = 1 · (-i) = -i

i²³: divide 23 by 4 → remainder 3 → i²³ = i³ = -i

i¹⁰⁰: divide 100 by 4 → remainder 0 → i¹⁰⁰ = i⁰ = 1
```

Rule: to find `iⁿ`, compute `n mod 4` and use the cycle `{0:1, 1:i, 2:-1, 3:-i}`.

---

## 8. COMMON TRAPS

**Trap 1**: Writing `Im(z) = 3i` when `z = 5 + 3i`.  
`Im(z) = 3`. The imaginary part is a real number — the coefficient of `i`.

**Trap 2**: Thinking `i` is "not real" in the sense of "not valid."  
`i` is exactly as valid as `-1`. Both required extending the number system beyond the natural numbers. `i` extends it once more.

**Trap 3**: `√(-4) = 2i`, not `±2i`.  
The principal square root of a negative number is defined as the positive real multiple of `i`. So `√(-4) = √4 · √(-1) = 2i`.

---

## 9. EXERCISES

**E1** (direct): Compute `i¹⁷`, `i⁴⁶`, `i⁻¹`.  
Hint for `i⁻¹`: find a real number `r` and `s` such that `i · (r + si) = 1`.

**E2** (structural): The polynomial `x⁴ - 1 = 0` has 4 roots. Find all of them (some are real, some are not).

**E3** (thinking): Why can't we solve the gap by defining `j = √(-1)` separately from `i = √(-1)` and treating them as different numbers? What goes wrong?

---

## 10. WORKED SOLUTIONS

### E1 — Compute `i¹⁷`, `i⁴⁶`, `i⁻¹`

```
i¹⁷ → 17 mod 4 = 1 → i¹⁷ = i

i⁴⁶ → 46 mod 4 = 2 → i⁴⁶ = -1

i⁻¹ → find (r + si) such that i · (r + si) = 1
     → ir + si² = 1
     → ir + s(-1) = 1
     → -s + ir = 1
     → -s = 1 and r = 0
     → s = -1, r = 0
     → i⁻¹ = -i

Check: i · (-i) = -i² = -(-1) = 1  ✓
```

### E2 — All 4 roots of `x⁴ - 1 = 0`

```
x⁴ - 1 = 0
x⁴ = 1

Factor as difference of squares:
(x² - 1)(x² + 1) = 0

x² - 1 = 0  →  x² = 1   →  x = 1, x = -1
x² + 1 = 0  →  x² = -1  →  x = i, x = -i

Four roots: {1, -1, i, -i}
```

Two real, two complex. Degree 4 → exactly 4 roots. The Fundamental Theorem of Algebra holds.

### E3 — Why `i` and `j` can't both equal `√(-1)` as separate objects

```
If i = √(-1) and j = √(-1) as distinct objects, then:

i² = -1
j² = -1

So i² = j², which means i² - j² = 0, so (i-j)(i+j) = 0.

This forces either i = j (same object) or i = -j (negatives).
```

There is no room for a third option. The algebra forces them to be either identical or negatives of each other. Calling them "different" creates a contradiction.

This is why `ℂ` has exactly one imaginary unit (and its negative). You can't extend the number system further in this direction without breaking algebra.

---

## 11. NEXT LESSON

L01 established that `i` must exist and defined complex numbers as `a + bi`.

L02 will define **arithmetic** — how to add, subtract, multiply, and divide complex numbers — and derive the rules entirely from `i² = -1` and standard algebra. No new axioms are needed.
