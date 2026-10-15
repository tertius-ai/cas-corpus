# Resolve the generic two-by-four determinantal quotient

Let `R=Q[x1,...,x8]`, form the matrix

```text
[x1 x3 x5 x7]
[x2 x4 x6 x8],
```

and let `I` be its six `2 x 2` minors. Compute and certify the minimal graded
free resolution of `R/I`.

The source prints `Z[x1,...,x6]` despite using `x7,x8`, and gives the format
`(1,6,8,4,1)`. Direct certified computation instead gives the classical
Eagon--Northcott table `(1,6,8,3)`, with shifts `0,2,3,4`. This scoped case
records both corrections; it does not implement persistence exactification.
