# Algebraic construction of the 16-vertex Bernhart--Kainen graph

Start with a cycle on vertices `0,...,9` and two independent triples

```text
A = {10,11,12},    B = {13,14,15}.
```

Join every vertex of `A` to the five odd cycle vertices, and every vertex of
`B` to the five even cycle vertices. This is the algebraic construction found
in the source paper for a raw graph arising in the Bernhart--Kainen
dispersability problem.

The resulting graph has 16 vertices and 40 edges and is connected and
5-regular. Its evident bipartition is

```text
{0,2,4,6,8,10,11,12} | {1,3,5,7,9,13,14,15}.
```

Noether verifies its canonical-label certificate. Its automorphism group has
order 720 and has exactly the two structural vertex orbits: the ten cycle
vertices and the six vertices in the independent triples.

This bounded case verifies the paper's structural graph construction. The
separate exhaustive computation showing that the graph is nondispersable is
not part of Noether 0.1 and is not claimed here.
