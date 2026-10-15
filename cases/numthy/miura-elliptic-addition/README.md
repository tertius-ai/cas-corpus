# A Miura divisor-class addition on an elliptic curve

On the elliptic curve

```text
E: y^2 = x^3 + 3x
```

over `Q`, add the points `(0,0)` and `(1,2)`. Verify both inputs and the output
on the curve, and recover

```text
(0,0) + (1,2) = (3,-6).
```

The source's Miura package reports this divisor-class sum by the ideal
`(x-3,y+6)`. Noether's native elliptic-curve point is the canonical result for
this genus-one subcase. General divisor arithmetic on Miura curves remains a
larger feature.
