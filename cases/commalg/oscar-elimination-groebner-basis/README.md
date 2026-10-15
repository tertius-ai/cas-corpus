# Eliminate one variable from two plane quadrics

Over the rationals, consider

```text
2x^2 - xy + 2y^2 - 2,
2x^2 - 3xy + 3y^2 - 2.
```

Use lexicographic order with `y` before `x`. Compute the reduced Groebner
basis and verify that it consists of the monic forms of

```text
3y + 8x^3 - 8x,
4x^4 - 5x^2 + 1.
```

The second element is the elimination polynomial in `x`. The source prints
the corresponding non-monic OSCAR basis; this translation checks the ideal
and exact basis rather than treating printed output as an oracle.
