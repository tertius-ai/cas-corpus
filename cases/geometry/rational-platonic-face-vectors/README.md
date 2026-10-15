# Face vectors of rational Platonic solids

Construct exact rational models of the tetrahedron, cube, and octahedron from
their vertices. Recover their face vectors

```text
(4,6,4), (8,12,6), (6,12,8),
```

respectively, and verify every resulting polytope certificate. Noether's
`f_vector` includes the empty face and the whole polytope, so the corresponding
values are `[1,4,6,4,1]`, `[1,8,12,6,1]`, and `[1,6,12,8,1]`.

The source also prints data for the dodecahedron and icosahedron. Those models
require irrational coordinates and are not folded into this rational case.
