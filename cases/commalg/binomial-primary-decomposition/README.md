# A primary decomposition with an embedded component

Let

`I = (x^2 - xy, xy - y^2)`

in `Q[x,y]`. Compute and certify its primary decomposition

`I = (x-y) intersect (x,y)^2`.

The two components have different roles: `(x-y)` is the reduced line, while
`(x,y)^2 = (x^2,xy,y^2)` is primary to the embedded maximal ideal `(x,y)`.
The program asks Noether for the decomposition, verifies every primary and
prime certificate, and checks both returned ideals against these explicit
expected components by certified ideal membership in both directions.

This is an independently written, hand-checkable adaptation of the small
binomial-decomposition problem recorded during intake. It does not redistribute
the paper or its Macaulay2 material.
