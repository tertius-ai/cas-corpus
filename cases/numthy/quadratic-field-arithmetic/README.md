# Exact arithmetic in `Q(sqrt(235))`

Let `K = Q(a)` with `a^2 = 235`. Compute its ring of integers, discriminant,
the primes above `7`, and the factorization of the principal ideal `(a)`.

The expected results are

```text
O_K = Z[a]
disc(K) = 940
(7) = (7, a + 5) (7, a + 2)
(a) = p_5 p_47
N(p_5) = 5,  N(p_47) = 47.
```

The solution also checks `Tr(a) = 0`, `N(a) = -235`, signature `(2,0)`, and
the ramification and residue degrees of every returned prime. Returned prime
ideals verify their own exact evidence before their defining memberships are
checked.

The source chapter continues with the class group and unit group. Those are
not part of Noether 0.1 and are not silently approximated here; this case ends
at the coherent supported ideal-factorization computation.
