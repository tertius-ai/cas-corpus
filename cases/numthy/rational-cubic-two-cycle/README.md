# A cubic two-cycle from an elliptic multiple

For `a=1`, consider

`E_a: Y^2 = X^3 + 4X^2 + 16a^2`

and its rational point `P_a=(0,-4a)`. Noether computes
`[2]P_a=(-4,4)`. For a nondegenerate point `(X,Y)` on this curve, the paper's
rational dictionary is

```text
b  = -X/4 - 2 - 16a^2/X^2,
x1 = (-4a-Y)/(2X),
x2 = (-4a+Y)/(2X).
```

At `[2]P_a`, these formulas give `b=-2` and `(x1,x2)=(1,0)`. The program
then verifies exactly that `f(x)=x^3-2x+1` exchanges `1` and `0`, so this is a
genuine rational two-cycle rather than merely a point on the parameter curve.
