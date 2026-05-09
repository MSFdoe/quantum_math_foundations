# L02 — Arithmetic of Complex Numbers

**Module**: 01 — Complex Numbers  
**Prerequisite**: L01 (definition of `i`, complex number `z = a + bi`)  
**Feeds into**: L03 — The Complex Plane and Geometric Interpretation

---

## 1. MOTIVATION

L01 established the object: a complex number is `z = a + bi` with `i² = -1`.

That is a static definition. It tells you what a complex number *is*, but not what you can *do* with two of them. Physics and engineering need to combine complex numbers — superpose two quantum states, multiply two oscillations, divide two impedances. For any of that to be possible, addition, subtraction, multiplication, and division must be defined on `ℂ`.

The key claim of this lesson:

> **No new axioms are needed.** Every arithmetic rule on `ℂ` follows from `i² = -1` and the ordinary algebra of real numbers.

If you treat `a + bi` as a polynomial in the symbol `i`, do the algebra you already know, and replace `i²` with `-1` whenever it appears — that is the entire system.

---

## 2. WHAT WE INHERIT FROM ℝ

We assume the real numbers obey the standard field axioms. For any `a, b, c ∈ ℝ`:

```
a + b = b + a                   (commutativity of +)
a · b = b · a                   (commutativity of ·)
(a + b) + c = a + (b + c)       (associativity of +)
(a · b) · c = a · (b · c)       (associativity of ·)
a · (b + c) = a · b + a · c     (distributivity)
```

We extend these to `ℂ` by *fiat*: every complex number is a polynomial in `i`, and we manipulate it like any other polynomial. The only extra rule is:

```
i² = -1
```

Wherever `i²` appears, substitute `-1`. That is the whole game.

---

## 3. ADDITION

Let `z₁ = a + bi` and `z₂ = c + di` with `a, b, c, d ∈ ℝ`.

Treat them as polynomials in `i` and collect like terms — real with real, `i`-term with `i`-term:

```
z₁ + z₂ = (a + bi) + (c + di)
        = a + c + bi + di
        = (a + c) + (b + d)i
```

**Rule:**

```
(a + bi) + (c + di) = (a + c) + (b + d)i
```

This is just vector addition in two components. Real parts add to real parts, imaginary parts to imaginary parts.

**Subtraction** is the same with the second operand negated:

```
(a + bi) − (c + di) = (a − c) + (b − d)i
```

There is no use of `i² = -1` yet — addition does not require it. The rule will become essential the moment we multiply.

---

## 4. MULTIPLICATION

Distribute term by term, same as multiplying two binomials in algebra:

```
z₁ · z₂ = (a + bi)(c + di)
        = a·c + a·di + bi·c + bi·di
        = ac + adi + bci + bd·i²
```

Now use the only new rule, `i² = -1`:

```
        = ac + adi + bci + bd(-1)
        = ac − bd + adi + bci
        = (ac − bd) + (ad + bc)i
```

**Rule:**

```
(a + bi)(c + di) = (ac − bd) + (ad + bc)i
```

Notice: the real part of the product is `ac − bd`, **not** `ac`. The minus sign comes directly from `i² = -1`. This minus sign is the whole reason complex multiplication will turn out to encode rotation in L03 — but for now, just track where it comes from.

---

## 5. THE COMPLEX CONJUGATE

Before we can divide, we need one auxiliary object.

**Definition:** the **complex conjugate** of `z = a + bi` is

```
z̄ = a − bi
```

It is the same complex number with the sign of the imaginary part flipped.

**Why it matters — the key identity:**

```
z · z̄ = (a + bi)(a − bi)
      = a² − abi + abi − b²i²
      = a² − b²(-1)
      = a² + b²
```

So:

```
z · z̄ = a² + b²    ∈ ℝ,    ≥ 0
```

Multiplying any complex number by its conjugate gives a **non-negative real number**. The imaginary part vanishes. This is the trick that will let us divide.

---

## 6. DIVISION

We want to compute `z₁ / z₂` and end up with something of the form `(real) + (real)i`. The problem: `z₂ = c + di` has an `i` in the denominator, and we have not defined what dividing by `i` means.

**The technique:** multiply numerator and denominator by the conjugate of the denominator.

```
z₁     a + bi     a + bi     c − di
─── =  ──────  =  ──────  ·  ──────
z₂     c + di     c + di     c − di
```

This is allowed because `(c − di)/(c − di) = 1` (provided `z₂ ≠ 0`).

The denominator becomes a real number by §5:

```
(c + di)(c − di) = c² + d²
```

The numerator is ordinary complex multiplication from §4:

```
(a + bi)(c − di) = ac + bd + (bc − ad)i
                   ─────   ─────────
                   real     imaginary
```

(Check: `(a)(c) + (a)(−d)i + (bi)(c) + (bi)(−di) = ac − adi + bci − bdi² = ac + bd + (bc − ad)i`.)

Putting it together:

```
z₁     (ac + bd) + (bc − ad)i
─── = ─────────────────────────
z₂           c² + d²
```

**Rule:**

```
a + bi     ac + bd        bc − ad
────── = ─────────  +  ─────────  i
c + di    c² + d²        c² + d²
```

Provided `c² + d² ≠ 0`, i.e., `z₂ ≠ 0`.

This is just real-number arithmetic on each component. Division on `ℂ` reduces to multiplication plus one division by a positive real.

---

## 7. WORKED EXAMPLES

**Example 1 — Addition and subtraction.**

```
(3 + 4i) + (5 − 2i) = (3 + 5) + (4 − 2)i = 8 + 2i

(3 + 4i) − (5 − 2i) = (3 − 5) + (4 − (−2))i = −2 + 6i
```

**Example 2 — Multiplication.**

```
(2 + 3i)(4 − i)
   = 2·4 + 2·(−i) + 3i·4 + 3i·(−i)
   = 8 − 2i + 12i − 3i²
   = 8 − 2i + 12i − 3(−1)
   = 8 + 3 + (−2 + 12)i
   = 11 + 10i
```

**Example 3 — Squaring.**

```
(1 + i)² = (1 + i)(1 + i)
        = 1 + i + i + i²
        = 1 + 2i + (−1)
        = 0 + 2i
        = 2i
```

So `(1 + i)² = 2i`. Note: a non-real number squared can land on the imaginary axis.

**Example 4 — Conjugate and modulus-squared.**

```
z = 3 + 4i
z̄ = 3 − 4i
z · z̄ = (3 + 4i)(3 − 4i) = 9 − 12i + 12i − 16i² = 9 + 16 = 25
```

(Notice: `25 = 3² + 4²`. This will become the squared magnitude `|z|²` in L03.)

**Example 5 — Division.**

```
3 + 4i      3 + 4i     1 − 2i
──────  =   ──────  ·  ──────
1 + 2i      1 + 2i     1 − 2i

Numerator:   (3 + 4i)(1 − 2i)
           = 3 − 6i + 4i − 8i²
           = 3 + 8 + (−6 + 4)i
           = 11 − 2i

Denominator: (1 + 2i)(1 − 2i) = 1 + 4 = 5

Result:      (11 − 2i)/5  =  11/5 − (2/5)i
```

Check by multiplying back:

```
(1 + 2i) · (11/5 − 2/5 i)
   = 11/5 − 2/5 i + 22/5 i − 4/5 i²
   = 11/5 + 4/5 + (−2/5 + 22/5)i
   = 15/5 + 20/5 i
   = 3 + 4i  ✓
```

**Example 6 — Reciprocal of `i`.**

```
1     1     −i      −i      −i
─── = ── · ──── = ──────── = ─── = −i
 i     i    −i     −i²        1
```

So `1/i = −i`. (We saw this in L01 as `i⁻¹ = −i`; here it is from the division rule.)

---

## 8. COMMON TRAPS

**Trap 1 — Forgetting the `i² = −1` substitution.**  
Writing `(2 + 3i)(4 − i) = 8 − 2i + 12i − 3i²` and stopping there is incomplete. You must replace `i²` with `−1`. The arithmetic is not done until every `i²` (and `i³`, `i⁴`, …) has been reduced.

**Trap 2 — Treating `i` as a real variable.**  
You may *not* write `√i` casually, or "cancel" `i` against `i` in non-trivial expressions. The safe operation is: treat `i` as an algebraic symbol, and apply `i² = −1` only when `i` appears squared.

**Trap 3 — Division by writing `1/(c + di)` as `1/c + 1/(di)`.**  
This is wrong. `1/(x + y) ≠ 1/x + 1/y` for any numbers. Always multiply by the conjugate.

**Trap 4 — Conjugating a sum incorrectly.**  
The conjugate of a sum is the sum of conjugates: `(z₁ + z₂)̄ = z̄₁ + z̄₂`. The conjugate of a product is the product of conjugates: `(z₁ · z₂)̄ = z̄₁ · z̄₂`. But the conjugate is **not** distributive over the symbol `i` directly — you flip the sign of the imaginary part of the *whole* expression after simplification.

**Trap 5 — Writing the result with `i²` still in it.**  
A complex number in standard form is `(real) + (real)i`. If your final answer contains `i²`, `i³`, or `1/i`, simplify further until it is in standard form.

---

## 9. STRUCTURAL NOTE — ℂ IS A FIELD

With the four operations now defined, `ℂ` satisfies all the field axioms `ℝ` satisfies:

- Addition is commutative and associative, with identity `0 = 0 + 0i` and inverses `−z = −a − bi`.
- Multiplication is commutative and associative, with identity `1 = 1 + 0i` and inverses `1/z = z̄ / (a² + b²)` for `z ≠ 0`.
- Multiplication distributes over addition.

What `ℂ` *loses* compared to `ℝ`: it cannot be ordered. There is no consistent way to say `i > 0` or `i < 0` (any such ordering forces a contradiction, since both `i² = −1` and squares-of-positives ought to be positive). `ℂ` is a field but not an ordered field. Keep this in mind: inequalities like `z₁ < z₂` are **undefined** for general complex numbers.

---

## 10. EXERCISES

**E1** (direct). Compute each in standard form `a + bi`:

```
(a)  (1 − 2i) + (3 + 5i)
(b)  (4 + i)(2 − 3i)
(c)  (2 + i)²
(d)  (1 + i)/(1 − i)
```

**E2** (conjugate). For `z = 5 − 12i`, compute `z̄`, `z + z̄`, `z − z̄`, and `z · z̄`. What pattern do you see relating `z + z̄` to `Re(z)` and `z − z̄` to `Im(z)`?

**E3** (reciprocal). Derive a general formula for `1/(a + bi)` in standard form. Then verify your formula on `1/(3 + 4i)`.

**E4** (structural). Show that `(z₁ · z₂)̄ = z̄₁ · z̄₂` for arbitrary `z₁ = a + bi`, `z₂ = c + di`. (Compute both sides explicitly and compare.)

**E5** (thinking). The product `(a + bi)(c + di)` produced a real part `ac − bd`. Where, mechanically, did the minus sign come from? If we had defined `i² = +1` instead of `−1`, what would the multiplication rule become, and would the conjugate trick `z · z̄ = a² + b²` still work?

---

## 11. WORKED SOLUTIONS

### E1

```
(a)  (1 − 2i) + (3 + 5i) = (1 + 3) + (−2 + 5)i = 4 + 3i

(b)  (4 + i)(2 − 3i) = 8 − 12i + 2i − 3i²
                     = 8 + 3 + (−12 + 2)i
                     = 11 − 10i

(c)  (2 + i)² = 4 + 4i + i² = 4 + 4i − 1 = 3 + 4i

(d)  (1 + i)/(1 − i) · (1 + i)/(1 + i)
       Numerator:   (1 + i)² = 2i      (from Example 3)
       Denominator: (1 − i)(1 + i) = 1 + 1 = 2
       Result:      2i / 2 = 0 + i = i
```

### E2

```
z   = 5 − 12i
z̄   = 5 + 12i

z + z̄ = (5 − 12i) + (5 + 12i) = 10 + 0i = 10
z − z̄ = (5 − 12i) − (5 + 12i) = 0 − 24i = −24i
z · z̄ = (5)² + (12)² = 25 + 144 = 169
```

Pattern:

```
z + z̄ = 2·Re(z)        →   Re(z) = (z + z̄)/2
z − z̄ = 2i·Im(z)       →   Im(z) = (z − z̄)/(2i)
```

These two identities will be useful for separating real and imaginary parts of expressions later.

### E3

```
1         1        a − bi      a − bi
────  =  ─────  · ──────  =  ─────────
a+bi     a+bi      a − bi    a² + b²

       =    a            −b
          ──────  +    ──────  i
          a²+b²        a²+b²
```

Formula:

```
   1         a              b
─────  =  ──────  −     ──────  i        (provided a² + b² ≠ 0)
a+bi      a²+b²         a²+b²
```

Check on `1/(3 + 4i)`:

```
a = 3, b = 4, a² + b² = 25
1/(3+4i) = 3/25 − (4/25)i
```

Verify: `(3 + 4i)(3/25 − 4i/25) = (9 + 16)/25 + (−12 + 12)i/25 = 25/25 = 1.` ✓

### E4

```
z₁ · z₂ = (a + bi)(c + di) = (ac − bd) + (ad + bc)i

(z₁ · z₂)̄ = (ac − bd) − (ad + bc)i

z̄₁ · z̄₂ = (a − bi)(c − di)
        = ac − adi − bci + bd·i²
        = ac − bd − (ad + bc)i
        = (ac − bd) − (ad + bc)i
```

The two are identical. ∎

### E5

The minus sign in `ac − bd` comes from exactly one place: the term `(bi)(di) = bd · i²`, and `i² = −1` flips its sign before it is collected with `ac`.

If we instead defined `i² = +1`, we would get:

```
(a + bi)(c + di) = ac + bd + (ad + bc)i
```

and the conjugate trick would give:

```
z · z̄ = (a + bi)(a − bi) = a² − b²·i² = a² − b²
```

That is **not** non-negative — it can be zero (when `a = ±b`) for non-zero `z`. So `z · z̄` would no longer act like a squared magnitude, and division by an arbitrary non-zero `z` would fail (you would divide by zero on the line `a = ±b`). The choice `i² = −1` is exactly what makes `ℂ` a field. The number system you would get from `i² = +1` is called the **split-complex numbers** — it exists and is useful in its own right (relativity), but it is not a field.

---

## 12. NEXT LESSON

L02 reduced all four arithmetic operations on `ℂ` to: ordinary algebra on the symbol `i`, plus the substitution `i² = −1`. We also introduced the conjugate `z̄` and saw that `z · z̄ = a² + b²` is a non-negative real.

L03 will give complex numbers a **geometric** identity: plotting `z = a + bi` as the point `(a, b)` in the plane. Once we do that, `z · z̄ = a² + b²` will be recognized as the squared distance from the origin (the **modulus** `|z|`), addition will become vector addition, and complex multiplication will reveal itself as **rotation and scaling** — the deepest fact about `ℂ` and the gateway to everything in quantum mechanics.
