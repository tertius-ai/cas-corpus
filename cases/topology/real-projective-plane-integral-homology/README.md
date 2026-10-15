# Integral homology of a triangulated real projective plane

Take the abstract simplicial complex on vertices `1` through `6` with facets

```text
123  234  345  154  521  562  462  164  365  163
```

This ten-triangle complex is a triangulation of the real projective plane. Its
integral homology is

```text
H_0 = Z,    H_1 = Z/2,    H_2 = 0.
```

The coefficient context matters: rational Betti numbers alone would not see
the factor of two. The solution verifies the simplicial complex, checks that it
has 6 vertices, 15 edges, 10 triangles, and Euler characteristic 1, and then
constructs its chain complex over `Z`. Noether verifies that the signed
boundary maps form a chain complex before computing and verifying the finitely
generated abelian-group invariants in degrees zero through two.

The triangulation and comparison computation are drawn from Nathan Grieve's
paper on abstract simplicial complexes in Macaulay2. This case expresses the
same integral calculation through Noether's topology and homological-algebra
objects.
