# A lexicographic Groebner basis

In the polynomial ring `Q[x,y]` with lexicographic order, form

`I = <y^4 + x^3 - x^2 + x, x^4>`.

Compute and verify the exact Groebner basis

`[x + y^12 - y^8 + y^4, y^16]`.

The source obtains this target with a Groebner walk beginning in graded reverse
lexicographic order. Noether 0.1 directly computes the target basis in the
declared lexicographic context. This bounded case does not claim to reproduce
the walk path, its four crossed cones, or the paper's benchmark study.
