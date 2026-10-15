# General position from a Vandermonde matrix

The paper begins with the `4 x 8` matrix whose column indexed by
`lambda in {1,...,8}` is `(1, lambda, lambda^2, lambda^3)^T`. Its Magma code
checks every four-column determinant before constructing a complete
intersection and an invariant Jacobian ring.

Certify that all `binom(8,4)=70` maximal minors are nonzero. For each selected
four-tuple, independently compare Noether's exact determinant with the
Vandermonde product

```text
product_{i<j} (lambda_j-lambda_i).
```

This case isolates the source computation's exact general-position
precondition. It does not claim to reproduce the paper's later invariant-ring
or Higgs-locus calculation.
