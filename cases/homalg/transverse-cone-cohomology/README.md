# Cohomology of a reduced transverse-cone complex

Consider an exact rational cochain complex concentrated in degrees `-1`
through `5`, with cochain dimensions

```text
1, 6, 15, 20, 15, 6, 1
```

and consecutive differential ranks

```text
0, 1, 3, 3, 1, 0.
```

Choose compatible reduced bases, so the nonzero differentials have disjoint
pivot coordinates and every consecutive composite is zero. The expected
cohomology dimensions are

```text
1, 5, 11, 14, 11, 5, 1.
```

Noether constructs the explicit matrices, verifies that they form a cochain
complex, and verifies every returned cohomology group.

The dimensions and ranks arose in an archived computation of a derived
self-Ext object associated with the cone of a rank-two bivector in an exterior
algebra. Noether 0.1 does not yet construct that exterior algebra or DG object.
This case is therefore exactly the additive complex after basis reduction,
not a translation of the missing multiplicative and derived construction.
