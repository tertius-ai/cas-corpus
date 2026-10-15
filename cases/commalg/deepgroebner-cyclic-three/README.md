# A deterministic cyclic-three Gröbner regression

The source's deterministic Buchberger tests include the cyclic-three ideal

```text
(x+y+z, xy+yz+zx, xyz-1) in F_32003[x,y,z].
```

Its expected reduced basis is
`(x+y+z, y^2+yz+z^2, z^3-1)`. Noether recomputes the basis in grevlex order
and verifies mutual containment of the original and expected generators. This
isolates the exact algebra benchmark from the repository's reinforcement-
learning environment and implementation-specific pair-selection tests.

