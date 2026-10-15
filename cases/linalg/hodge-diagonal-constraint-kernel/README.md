# Kernel of fourfold Hodge-diagonal constraints

Let `d[p,q]` denote a proposed change in the Hodge number `h[p,q]` of a
complex fourfold. Impose Hodge symmetry and Serre duality,

```text
d[p,q] = d[q,p] = d[4-p,4-q],
```

so the 25 entries are represented by nine variables. Also impose invariance of
every diagonal sum `sum(p-q=k) d[p,q]` and fix the five boundary values
`d[0,q]` to zero.

The resulting rational constraint matrix has shape 14 by 9 and rank 8. Its
kernel is one-dimensional: in the representative order used by the solution,
an integral generator has only

```text
d[1,1] = -1,    d[2,2] = 2
```

nonzero. The solution constructs the constraints from their mathematical
definitions, verifies Noether's returned solution space, and checks this exact
direction.

This is intentionally a linear-algebra case. It does not model Hodge
structures or prove that the formal variation is geometrically realizable. An
archived Sage session motivated the calculation, but the statement and Noether
program here are independent and no archived source is redistributed.
