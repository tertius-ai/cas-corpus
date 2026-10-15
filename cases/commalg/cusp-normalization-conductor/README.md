# Normalize a cusp and certify its conductor

Let

```text
A = Q[x,y]/(x^2-y^3).
```

Compute the normalization of `A`, its coordinate map, and the conductor back
in the source ring. The paper begins its normalization algorithm with the test
pair `((x,y),x)` and adjoins the fraction `t=y^2/x`; its relations imply
`x=t^3` and `y=t^2`.

Noether returns the normal algebra `Q[t]`, verifies the finite birational map,
and certifies that the source conductor is `(x,y)`.
