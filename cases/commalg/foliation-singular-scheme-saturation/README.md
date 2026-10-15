# Recover a foliation's singular scheme

In `Q[x0,x1,x2,x3]`, let `C` be defined by

```text
x0^2, x0*x1, x1^2, x0*(x2^2-x3^2)-x1*x2*x3,
```

and let `P` be the union of the three points defined in the solution. Form
`Z=C union P`. The paper supplies a quadratic vector field
`v=(a0,a1,a2,a3)`. Form the six `2 x 2` minors of

```text
[x0 x1 x2 x3]
[a0 a1 a2 a3]
```

and saturate their ideal by `(x0,x1,x2,x3)`. Certify both containments between
the saturated ideal and `I(Z)`. This recovers the singular scheme but does not
construct the vector field from differential forms and syzygies.
