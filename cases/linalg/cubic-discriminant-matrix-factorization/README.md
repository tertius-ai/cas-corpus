# A cubic-discriminant matrix factorization

Over `Q[s1,s2,s3]`, enter the two `3 x 3` matrices `A` and `B` displayed in
the paper's `S1 x S2` example. Let

```text
Delta = s1^2*s2^2 - 4*s1^3*s3 - 4*s2^3 + 18*s1*s2*s3 - 27*s3^2
```

be the discriminant of a monic cubic expressed in elementary symmetric
functions. Verify the two exact identities

```text
A*B = Delta*I3 = B*A.
```

The case checks a published factorization; it does not construct the matrices
from Young symmetrizers or Specht modules.
