# The secant of two projective points

The two points `[1:0:0]` and `[0:1:0]` in `P^2` have homogeneous ideal
`I=(x0*x1,x2)`. Following the paper's displayed secant construction, introduce
two copies `y1`, `y2` and form

```text
J = I(y1) + I(y2)
    + (y10+y20-x0, y11+y21-x1, y12+y22-x2).
```

Eliminate the six `y` variables and certify that the result is `(x2)`, the
line joining the two points. This small example exercises the algebraic core
of the source construction; it does not replace the still-missing general
secant-variety workflow.
