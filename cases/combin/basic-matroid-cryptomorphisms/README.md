# Recover matroid data from bases

Consider the rank-two matroid on ground set `{0,1,2,3}` with exactly two
bases, `{0,1}` and `{0,2}`. This is the first example in the source paper,
after replacing its element names `{a,b,c,d}` with their integer indices.

Noether recovers the paper's rank and circuit descriptions:

```text
rank(E)       = 2
rank({0,3})   = 1
circuits      = {{1,2}, {3}}
```

Thus `3` is a loop and `1` and `2` are parallel. Deleting `3` leaves the two
original bases on `{0,1,2}`. Contracting `1` gives a rank-one matroid on
`{0,2,3}` with sole basis `{0}`; both `2` and `3` are loops in that minor.

This case stays within the paper's elementary basis-defined example. It does
not claim the later represented-matroid, isomorphism, flat, or Chow-ring
computations.
