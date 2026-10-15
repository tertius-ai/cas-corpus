# Dimension of a parametrized affine cubic curve

The OSCAR transcript studies the ideal

```text
I = (x2 - x1^2, x3 - x1*x2) in Q[x1,x2,x3].
```

It reports that the radical of the leading ideal is `(x2,x1)` and that
`dim(I)=1`. Noether computes the monomial initial ideal, takes its radical,
and verifies that both ideals have Krull dimension one. This is the exact
algebraic core of the source example, without its presentation machinery.

