# A degree-one del Pezzo point count over `F_7`

Consider the weighted-projective sextic

```text
X: w^2 = z^3 + 2x^6 + 2y^6  in P(1,1,2,3) over F_7.
```

The paper counts its rational points by covering the base `P^1(F_7)` with the
fibers

```text
C_[a,b]: w^2 = z^3 + 2a^6 + 2b^6.
```

Use exact finite-field arithmetic to count each affine fiber. Verify that the
fiber at infinity and the fiber at `a=0` each have eight points, the six
remaining fibers each have two, and the weighted-projective vertex contributes
one. The required total is therefore `29`.

This is the paper's complete `F_7` subcalculation. Its `F_{7^3}` count and the
deduction of Frobenius order and trace remain outside this bounded case.
