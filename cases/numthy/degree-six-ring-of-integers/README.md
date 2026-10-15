# Certifying a degree-six ring of integers

Let `K = Q(a)`, where `a` is a root of

```text
x^6 - 15*x^4 - 140*x^3 - 270*x^2 + 96*x + 3220.
```

The linked certificate repository proposes the following integral basis:

```text
1
a
a^2
(a^3 - a^2)/2
(a^4 - a^2)/2
a^5/15266 + 1265*a^4/15266 - 80*a^3/449
  - 3045*a^2/7633 + 2605*a/7633 - 2083/7633.
```

The intended claim is stronger than checking that six elements are linearly
independent. They must generate an order, every element must be integral, and
the resulting order must be the full ring of integers.

The solution builds the exact field and basis. It checks integrality through
the characteristic polynomials, asks Noether to validate that the basis defines
an order, computes the maximal order independently, and proves that the two
orders agree. It also verifies

```text
disc(K) = 7381125000000
[Z[a] : O_K] = 61064
disc(Z[a]) = disc(K) * 61064^2.
```

The numerical certificate is the field labelled `6.2.7381125000000.77` in the
source repository accompanying work of Baanen, Chavarri Villarello, and
Dahmen. Only the exact mathematical input is retained here; the implementation
and explanatory text are original Noether code and prose.
