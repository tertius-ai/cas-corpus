# Minimal primes and a primary hypersurface power

In `Q[x,y,z]`, determine the minimal primes of `(xy,yz)`. Then decompose
`((x^2+1)^2)` and certify both its primary component and associated prime.

The expected results are

```text
Min(xy,yz) = {(y), (x,z)},
((x^2+1)^2) is (x^2+1)-primary.
```

The source continues by splitting the latter ideal after a quadratic
number-field extension. This case is intentionally scoped to the rational
decompositions that Noether 0.2 certifies end to end.
