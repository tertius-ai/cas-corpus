# Check a multivariate partial fraction decomposition

In `Q(x,y)`, certify the displayed identity

```text
(x^2 + 3*x*y - y^2) / ((x+1)*(2*x+y))
  = 1/2
    + (9*y/2 + 9)/(2*x+y)
    + (-y-5)/(x+1)
    - 9/((x+1)*(2*x+y)).
```

Clear the two denominator factors and establish exact polynomial equality.
This checks the paper's output; it does not choose the decomposition or
reproduce the ordering-dependent Leinartas algorithm.
