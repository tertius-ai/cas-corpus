# The slack ideal of a square

Let `x0,...,x7` label the nonzero entries, row by row, of the symbolic
slack matrix

```text
[x0 x1  0  0]
[ 0 x3 x2  0]
[ 0  0 x5 x4]
[x7  0  0 x6].
```

Compute its determinant and saturate the resulting ideal by the product of
all eight variables. Certify that the result is the principal ideal

```text
(x0*x3*x5*x6 - x1*x2*x4*x7).
```

This is the paper's square example after translating from a vertex list to
the displayed symbolic matrix. It does not implement the general slack-matrix
constructor.
