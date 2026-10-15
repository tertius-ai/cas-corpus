# Normalization of three intersecting affine planes

Let

`A = Q[x,y,z]/((x-y)(x-z)(y-z))`.

Its three minimal components are the planes `x=y`, `x=z`, and `y=z`. Each
component is already normal and has a polynomial coordinate ring in two
variables, so the normalization of the reduced ring is their direct product.

The program asks Noether for the reduced affine normalization and verifies its
complete evidence record. It then checks that there are exactly three minimal
prime components, three component maps, and three normal, degree-one,
dimension-two polynomial quotient rings. This translates the concrete
normalization example without reproducing the paper's Macaulay2 or Singular
sessions.
