# Exact invariants of a Druzkowski candidate matrix

Let `i^2=-1` and consider the matrix over `Q(i)`

```text
[ 1   i   1   1]
[-i   1  -i  -i]
[-1  -i   1  -1]
[-1  -i   1  -1].
```

Compute its exact rank and characteristic polynomial. The required results are

```text
rank(A) = 2,
chi_A(t) = t^2(t^2-2t+4).
```

In particular, the matrix is not nilpotent. These are the exact linear-algebra
checks in the source example; its much stronger Condition C1 radical
certificate is not part of this case.
