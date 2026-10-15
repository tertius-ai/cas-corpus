# Elementary exact Betti-number examples

The source repository's regression suite records the homology and Betti
numbers of named point, line, circle, sphere, torus, Klein-bottle, Möbius-strip,
and projective-space complexes.

This bounded case uses the first four examples, whose facets fit directly in
the solution. Noether constructs each complex and its chain complex, verifies
that the differential squares to zero, and reproduces the expected Betti
numbers over both `Q` and `F_2`: `[1]`, `[1,0]`, `[1,1]`, and
`[1,0,1]`. The larger named triangulations remain covered by separate corpus
cases.

