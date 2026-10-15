# Exact face structure of a rational pentagon

Take the convex hull of the five points

```text
(1,0), (1,1), (0,1), (-1,0), (-1,-1).
```

The resulting polygon has the irredundant inequality description

```text
-x <= 1
-x + y <= 1
 x - 2y <= 1
 x <= 1
 y <= 1.
```

The solution constructs the hull over the rationals, verifies its internal
vertex/facet evidence, and checks the complete vertex-facet incidence. It has
five vertices and five edges. Noether includes the empty face and the polytope
itself in its `f_vector`, so the result is `[1, 5, 5, 1]`; the OSCAR transcript
reports the proper nonempty entries `[5, 5]`.

The same source transcript goes on to compute area and lattice points. Those
are deliberately outside this bounded case: the face-structure computation is
already a coherent exact operation supported by Noether 0.1.
