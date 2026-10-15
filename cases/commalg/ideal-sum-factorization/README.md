# Factor the generator of an ideal sum

The source maps two principal ideals into a common polynomial ring and obtains
the reduced Gröbner generator

```text
x^5 - 3*x^4 + 3*x^3 - x^2 = x^2 (x - 1)^3.
```

This translation names the common variable explicitly, constructs the two
source ideals `(x^2(x-1)^4)` and `(x^3(x-1)^3)`, forms their sum, and asks
Noether both for its Gröbner basis and the certified factorization of its sole
generator.

