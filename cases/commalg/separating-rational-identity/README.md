# A separating rational identity

Set

`p = xy - x - y - x^2 y^2`.

The source finds one-variable rational functions whose difference is a
rational multiple of `p`:

`((x-y)/(x^2 y^2)) p = (1-x-x^3)/x^2 - (1-y-y^3)/y^2`.

The case clears the common denominator and asks Noether to verify the
equivalent identity exactly in `Q[x,y]`:

`(x-y)p = y^2(1-x-x^3) - x^2(1-y-y^3)`.

This bounded translation checks the published certificate. It does not claim
to implement the source's algorithm for discovering poles, multiplicities, or
separated generators.
