# A deterministic six-polytope g-vector sample

The source notebook samples 20 points on the unit sphere in dimension six,
computes the simplicial polytope's f- and g-vectors, and then repeats this for
a scatter plot. Its stored first output came from an unrecorded random state.

For a replayable corpus case, this adaptation uses seed `20260907` to choose
20 exact integer points. Noether certifies their six-dimensional convex hull,
its 292 simplex facets, and f-vector
`[1,20,156,564,1012,876,292,1]`. The standard relation between f- and
h-vectors gives `g=[1,13,57,49]`. A cyclic six-polytope on 20 vertices is
also constructed to check the componentwise upper-bound comparison.

