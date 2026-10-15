# Five transitive permutation groups of degree four

Construct the cyclic, Klein four, dihedral, alternating, and symmetric groups
in their standard transitive actions on four points. Verify their orders,
point stabilizers, elementary structural properties, and conjugacy-class
sizes.

The expected class-size multisets are

```text
C4:  1, 1, 1, 1
V4:  1, 1, 1, 1
D8:  1, 1, 2, 2, 2
A4:  1, 3, 4, 4
S4:  1, 3, 6, 6, 8
```

For every class, the solution verifies Noether's class evidence and checks
`|class| * |centralizer| = |group|`. It also checks orbit--stabilizer at a
point, so the calculation tests more than recognition by group order.

The finite list was prompted by a larger archived search involving
degree-four permutation quotients. This case retains only the bounded native
permutation-group calculation available in Noether 0.1; it does not reproduce
the surrounding geometric search.
