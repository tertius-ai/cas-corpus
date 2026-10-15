# Probability-functions polytope of a three-antichain

Let `P` be the antichain on three elements. A probability function has one
independent coordinate for each unordered pair: after imposing

```text
pi(a,b) + pi(b,a) = 1,
```

the three coordinates vary independently in `[0,1]`. The paper therefore
identifies the probability-functions polytope of `P` with the cube `[0,1]^3`.

The solution checks that the input really is a three-element antichain, builds
the exact cube from its eight vertices, and verifies its six irredundant
facets. Its Noether `f_vector`, including the empty and full faces, is

```text
[1, 8, 12, 6, 1].
```

This bounded example tests the paper's concrete polyhedral claim. Constructing
the probability-functions polytope of an arbitrary finite poset would be a
separate higher-level combinatorial operation.
