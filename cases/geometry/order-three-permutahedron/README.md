# The order-three permutahedron

Take all six permutations of `(1,2,3)` as points in `Q^3` and form their
convex hull. Every point lies in the affine plane `x1+x2+x3=6`, so the hull has
ambient dimension three but affine dimension two.

The resulting hexagon has f-vector `[1,6,6,1]`: six vertices, six edges, and
one two-dimensional face. Thus it has 13 nonempty faces, as described in the
source. Noether computes and verifies the complete face lattice and its cover
relations.

This bounded case does not attempt the source's weak orders, lattice
congruences, associahedra, permutrees, or Hopf algebras.
