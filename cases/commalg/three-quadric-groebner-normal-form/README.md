# A lexicographic basis for three quadrics

Over `Q[x,y,z]`, the source computes a reduced lexicographic Gröbner basis of

```text
(x^2+y^2+2z^2-8, x^2-y^2-z^2+1, x-y+z).
```

Noether reproduces the displayed basis
`(6z^4-18z^2+1, y+3z^3-9z, x+3z^3-8z)`, normalizing the first generator
to its monic associate. The case additionally reduces
`x^2+y^2+z^2` to `-z^2+8`, giving a compact membership and normal-form
check rather than relying on printed basis order.
