# Hibi quotient of the divisor poset of 12

Order the six divisors `1,2,3,4,6,12` by divisibility. Enumerate its order
ideals. For every order ideal `I`, form the squarefree degree-six monomial

```text
u_I = product_{i in I} x_i * product_{i not in I} y_i.
```

There are ten such monomials. Let `J` be the ideal they generate in the
12-variable polynomial ring over `Q`. Regard `R/J` as a graded presented
module and certify its minimal resolution. The required nonzero Betti entries
are

```text
beta_(0,0)=1, beta_(1,6)=10, beta_(2,7)=12, beta_(3,8)=3.
```

This recreates the paper's divisor-poset Hibi example from Noether's poset and
module primitives without claiming a general Hibi-ideal constructor.
