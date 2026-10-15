# A bowtie simplicial complex

Take two filled triangles that meet in exactly one vertex. With vertices
numbered `0` through `4`, their facets are `[0,1,2]` and `[2,3,4]`.

Construct the complex, verify that it has five vertices, six edges, and two
triangles, and compute its integral homology. It is connected and contractible:
`H_0` is `Z`, while `H_1` and `H_2` vanish. Its Euler characteristic is one.

The source reports its f-vector with an additional leading entry for the empty
face. Noether's `face_counts()` reports only nonempty dimensions, so this case
checks `[5,6,2]`.
