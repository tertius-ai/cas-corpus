# A codepth-three quotient

Let `R=Q[x,y,z]` and

```text
I = (x*y^2, x*y*z, y*z^2, x^4-y^3*z, x*z^3-y^4).
```

Compute and certify a minimal graded free resolution of `R/I`. Its nonzero
Betti entries must be

```text
beta_(0,0)=1
beta_(1,3)=3, beta_(1,4)=2
beta_(2,4)=2, beta_(2,6)=3, beta_(2,7)=1
beta_(3,8)=2.
```

Thus the total ranks are `(1,5,6,2)`. In the source classification this gives
embedding codepth three, `m=5`, and type `n=2`. Determining the multiplicative
Tor-algebra invariants and the final class `G(2)` is a separate, still-blocked
step.
