# Cases

Cases are grouped by their owning Noether domain:

```text
cases/<domain>/<slug>/
  case.json
  README.md
  solution.py
```

Use one primary owning domain in the path and list every participating domain
in `case.json`. Case IDs are stable and have the form `<domain>.<slug>`.

A translation is semantic rather than necessarily line-for-line: it should
compute the same mathematical object or establish the same claim using
Noether's idioms. If a faithful result needs an API absent from the pinned
release, keep the candidate in `cas-corpus-intake`.

## Current cases

### `linalg`

- [`linalg.cubic-discriminant-matrix-factorization`](linalg/cubic-discriminant-matrix-factorization/)
  verifies both exact products in a `3 x 3` matrix factorization of the cubic
  discriminant.

- [`linalg.druzkowski-matrix-invariants`](linalg/druzkowski-matrix-invariants/)
  computes an exact rank and characteristic polynomial over `Q(i)` for a
  matrix from a Jacobian-conjecture calculation.

- [`linalg.galois-orbit-cubic-independence`](linalg/galois-orbit-cubic-independence/)
  test cubics on a finite-field Galois orbit.

- [`linalg.generalized-mixed-discriminant`](linalg/generalized-mixed-discriminant/)
  recover a generalized mixed discriminant as a determinant coefficient.

- [`linalg.golden-endomorphism-matrix`](linalg/golden-endomorphism-matrix/)
  certifies the determinant and rational characteristic polynomial of a
  golden-ratio endomorphism matrix.

- [`linalg.graph-minimum-rank-witness`](linalg/graph-minimum-rank-witness/)
  certify an exact graph minimum-rank witness.

- [`linalg.hodge-diagonal-constraint-kernel`](linalg/hodge-diagonal-constraint-kernel/)
  computes the one-dimensional exact kernel of fourfold Hodge-diagonal and
  boundary constraints.

- [`linalg.hyperbolic-face-cycle-vectors`](linalg/hyperbolic-face-cycle-vectors/)
  enumerate short vectors in a face-cycle lattice.

- [`linalg.imaginary-quadratic-endomorphism-matrix`](linalg/imaginary-quadratic-endomorphism-matrix/)
  computes the determinant and characteristic polynomial of an endomorphism
  matrix over `Q(sqrt(-3))`.

- [`linalg.matroid-intersection-form-rank`](linalg/matroid-intersection-form-rank/)
  certifies full rank and determinant `-1` for an intersection matrix printed
  by an OSCAR matroid computation.

- [`linalg.monomial-wlp-characteristic`](linalg/monomial-wlp-characteristic/)
  test weak Lefschetz behavior of a monomial complete intersection.

- [`linalg.picard-cremona-transformations`](linalg/picard-cremona-transformations/)
  compose Cremona transformations on divisor-class data.

- [`linalg.rank3-quiver-mutation`](linalg/rank3-quiver-mutation/)
  iterate exact mutations of rank-three quivers.

- [`linalg.real-hyperplane-lct`](linalg/real-hyperplane-lct/)
  compute a real log canonical threshold of a hyperplane arrangement.

- [`linalg.restricted-grassmannian-secant-rank`](linalg/restricted-grassmannian-secant-rank/)
  compute a restricted Grassmannian secant rank.

- [`linalg.semiclifford-rank-consistency`](linalg/semiclifford-rank-consistency/)
  certify a symbolic rank bound from vanishing maximal minors.

- [`linalg.sqrt-two-endomorphism-matrix`](linalg/sqrt-two-endomorphism-matrix/)
  verifies that a matrix over `Q(sqrt(2))` squares to twice the identity.

- [`linalg.square-strip-chromatic-transfer`](linalg/square-strip-chromatic-transfer/)
  compute a square-strip chromatic polynomial by transfer matrix.

- [`linalg.tipsy-cop-markov-chain`](linalg/tipsy-cop-markov-chain/)
  compute exact tipsy cop-and-robber survival probabilities.

- [`linalg.triangular-strip-chromatic-transfer`](linalg/triangular-strip-chromatic-transfer/)
  compute a triangular-strip chromatic polynomial by transfer matrix.

- [`linalg.vandermonde-general-position`](linalg/vandermonde-general-position/)
  certifies all 70 maximal minors of an eight-column Vandermonde matrix.

- [`linalg.young-idempotent-matrix-check`](linalg/young-idempotent-matrix-check/)
  verify a self-adjoint Young-symmetrizer idempotent.

### `numthy`

- [`numthy.cubic-field-embeddings`](numthy/cubic-field-embeddings/)
  compute certified embeddings of a cubic number field.

- [`numthy.degree-eight-permutations-gf11`](numthy/degree-eight-permutations-gf11/)
  enumerate normalized degree-eight permutation polynomials over GF(11).

- [`numthy.degree-eight-permutations-gf16`](numthy/degree-eight-permutations-gf16/)
  enumerate normalized degree-eight permutation polynomials over GF(16).

- [`numthy.degree-seven-permutation-witnesses`](numthy/degree-seven-permutation-witnesses/)
  verify degree-seven permutation-polynomial witnesses over GF(11).

- [`numthy.degree-six-ring-of-integers`](numthy/degree-six-ring-of-integers/)
  certifies a proposed integral basis, maximal order, discriminant, and
  equation-order index.

- [`numthy.diagonal-quadric-local-density-sums`](numthy/diagonal-quadric-local-density-sums/)
  evaluate local-density character sums modulo eight.

- [`numthy.error-tolerant-rational-reconstruction`](numthy/error-tolerant-rational-reconstruction/)
  reconstruct a rational number despite bad modular residues.

- [`numthy.f4001-square-roots`](numthy/f4001-square-roots/)
  verifies two square-root relations used in a Jacobian endomorphism
  computation over `F_4001`.

- [`numthy.finite-field-cyclic-dft`](numthy/finite-field-cyclic-dft/)
  compute and invert a length-three DFT over F4.

- [`numthy.finite-field-isomorphism-f25`](numthy/finite-field-isomorphism-f25/)
  verifies a deterministic explicit isomorphism and its inverse between two
  presentations of `F_25`.

- [`numthy.generalized-leibnitz-numbers`](numthy/generalized-leibnitz-numbers/)
  compute generalized Leibnitz numbers from their finite double sum.

- [`numthy.generalized-stirling-recurrence`](numthy/generalized-stirling-recurrence/)
  verify Mathar's recurrence for generalized-Stirling sequence A001711.

- [`numthy.geometric-arithmetic-prime-progressions`](numthy/geometric-arithmetic-prime-progressions/)
  enumerate geometric-arithmetic prime progressions.

- [`numthy.googol-fibonacci-residue`](numthy/googol-fibonacci-residue/)
  compute Fibonacci number F_(10^100) modulo 1000.

- [`numthy.hodge-chern-orders`](numthy/hodge-chern-orders/)
  compute the arithmetic factors bounding top Hodge Chern-class orders.

- [`numthy.isogeny-primes-quadratic-field`](numthy/isogeny-primes-quadratic-field/)
  computes the maximal order and discriminants of `Q(sqrt(-127))`.

- [`numthy.isogeny-primes-smooth-factorization`](numthy/isogeny-primes-smooth-factorization/)
  certifies the factorization `9102 = 2*3*37*41` from an isogeny-prime test.

- [`numthy.lehmer-comtet-recurrence`](numthy/lehmer-comtet-recurrence/)
  verify Mathar's recurrence for Lehmer-Comtet diagonal A045406.

- [`numthy.miura-elliptic-addition`](numthy/miura-elliptic-addition/)
  reproduces an exact divisor-class addition on an elliptic Miura curve.

- [`numthy.padic-newton-cube-root`](numthy/padic-newton-cube-root/)
  compute a cube root of two by 5-adic Newton iteration.

- [`numthy.prime-short-interval-counts`](numthy/prime-short-interval-counts/)
  count primes in a family of square-root-length intervals.

- [`numthy.quadratic-field-arithmetic`](numthy/quadratic-field-arithmetic/)
  computes the maximal order, primes above `7`, and the ideal factorization of
  `(sqrt(235))`.

- [`numthy.rational-cubic-two-cycle`](numthy/rational-cubic-two-cycle/)
  doubles an exact rational elliptic point and applies a published dictionary
  to obtain and verify a cubic two-cycle.

- [`numthy.rational-orbit-nonperiodicity`](numthy/rational-orbit-nonperiodicity/)
  test a rational recurrence for periods through 1000 terms.

- [`numthy.satotateg3-septic-factorization`](numthy/satotateg3-septic-factorization/)
  factors and certifies a septic polynomial used in a genus-three Sato--Tate
  computation.

- [`numthy.weak-carmichael-examples`](numthy/weak-carmichael-examples/)
  verify constructions of weak Carmichael numbers.

### `commalg`

- [`commalg.a348410-algebraic-generating-function`](commalg/a348410-algebraic-generating-function/)
  verify an algebraic generating function for A348410.

- [`commalg.affine-cubic-curve-dimension`](commalg/affine-cubic-curve-dimension/)
  certify the dimension of a parametrized affine cubic curve.

- [`commalg.apollonius-circle-groebner-basis`](commalg/apollonius-circle-groebner-basis/)
  certify a symbolic Apollonius-circle Groebner basis.

- [`commalg.binary-independence-ideal`](commalg/binary-independence-ideal/)
  reduce a binary independence model to its determinant equation.

- [`commalg.binomial-primary-decomposition`](commalg/binomial-primary-decomposition/)
  certifies the reduced and embedded components of a small binomial ideal.

- [`commalg.bivariate-monomial-power-growth`](commalg/bivariate-monomial-power-growth/)
  counts the minimal generators of thirteen consecutive powers of a concrete
  bivariate monomial ideal.

- [`commalg.boolean-function-nonlinearity`](commalg/boolean-function-nonlinearity/)
  compute the nonlinearity of a two-variable Boolean function.

- [`commalg.boolean-groebner-basis`](commalg/boolean-groebner-basis/)
  certify a Boolean Groebner basis over F2.

- [`commalg.conic-line-characteristic-number`](commalg/conic-line-characteristic-number/)
  compute the characteristic number of a conic-line arrangement.

- [`commalg.coordinate-ideal-primary-decomposition`](commalg/coordinate-ideal-primary-decomposition/)
  decompose a coordinate ideal into plane and axis components.

- [`commalg.cusp-normalization-conductor`](commalg/cusp-normalization-conductor/)
  normalizes the cusp `x^2=y^3` and certifies its coordinate map and conductor.

- [`commalg.cycle-vertex-cover-power`](commalg/cycle-vertex-cover-power/)
  certify membership in the square of a cycle cover ideal.

- [`commalg.cyclotomic-sequence-linear-complexity`](commalg/cyclotomic-sequence-linear-complexity/)
  verify an order-eight cyclotomic-sequence linear complexity.

- [`commalg.d222-hyperdeterminant`](commalg/d222-hyperdeterminant/)
  recover the 2 x 2 x 2 hyperdeterminant by elimination.

- [`commalg.deepgroebner-cyclic-three`](commalg/deepgroebner-cyclic-three/)
  verify a deterministic cyclic-three Groebner regression.

- [`commalg.del-pezzo-f7-point-count`](commalg/del-pezzo-f7-point-count/)
  reproduces a 29-point finite-field count used to identify Frobenius data for
  a degree-one del Pezzo surface.

- [`commalg.dingdong-weighted-critical-ideal`](commalg/dingdong-weighted-critical-ideal/)
  recover the weighted critical ideal of the Dingdong surface.

- [`commalg.evolution-algebra-isomorphism`](commalg/evolution-algebra-isomorphism/)
  decide an evolution-algebra isomorphism by Groebner basis.

- [`commalg.f4-groebner-basis`](commalg/f4-groebner-basis/)
  certify a published reduced Groebner basis over F101.

- [`commalg.f5-groebner-example`](commalg/f5-groebner-example/)
  reproduce an F5 Gröbner-basis example.

- [`commalg.finite-projective-variety-point-count`](commalg/finite-projective-variety-point-count/)
  counts the rational points on an intersection of quadrics over `F_5`.

- [`commalg.foliation-singular-scheme-saturation`](commalg/foliation-singular-scheme-saturation/)
  recovers a foliation's three-point singular scheme by saturating a
  maximal-minor ideal.

- [`commalg.groebner-membership-witnesses`](commalg/groebner-membership-witnesses/)
  produce checkable witnesses for ideal membership and equality.

- [`commalg.hadamard-m-polynomial-table`](commalg/hadamard-m-polynomial-table/)
  expand the Hadamard m-polynomial table at length six.

- [`commalg.hermite-criterion-degree-eight`](commalg/hermite-criterion-degree-eight/)
  expand a degree-eight Hermite-criterion polynomial.

- [`commalg.hough-double-ideal-radicals`](commalg/hough-double-ideal-radicals/)
  certifies positive and negative radical-membership tests underlying two
  Hough-regularity decisions.

- [`commalg.ideal-sum-factorization`](commalg/ideal-sum-factorization/)
  form an ideal sum and factor its Groebner generator.

- [`commalg.isogonal-conjugate-distance-identity`](commalg/isogonal-conjugate-distance-identity/)
  verify an isogonal-conjugate distance identity.

- [`commalg.k3-univariate-certificates`](commalg/k3-univariate-certificates/)
  verifies exact Weil-polynomial, finite-field square-root, and real-root
  certificates from a K3 computation.

- [`commalg.klein-quartic-f43-point-count`](commalg/klein-quartic-f43-point-count/)
  certifies that the Klein quartic has 80 projective rational points over
  `F_43`.

- [`commalg.lex-groebner-basis-example`](commalg/lex-groebner-basis-example/)
  verifies a lexicographic Groebner basis over the rationals.

- [`commalg.meixner-sequence-recurrence`](commalg/meixner-sequence-recurrence/)
  verify the generating-function recurrence for Meixner sequence A214615.

- [`commalg.mobius-truncated-ring-identities`](commalg/mobius-truncated-ring-identities/)
  verify Mobius-generator identities modulo t^22.

- [`commalg.monomial-ideal-colon-witnesses`](commalg/monomial-ideal-colon-witnesses/)
  verifies colon-ideal witnesses for a monomial associated prime.

- [`commalg.multisymmetric-big-diagonal-ideal`](commalg/multisymmetric-big-diagonal-ideal/)
  identify a big diagonal ideal by alternating determinants.

- [`commalg.multivariate-faa-di-bruno`](commalg/multivariate-faa-di-bruno/)
  expand a bounded multivariate Faà di Bruno formula.

- [`commalg.multivariate-partial-fraction-check`](commalg/multivariate-partial-fraction-check/)
  certifies a displayed multivariate partial-fraction identity by exact
  denominator clearing.

- [`commalg.neural-ideal-primary-decomposition`](commalg/neural-ideal-primary-decomposition/)
  primary-decompose a three-neuron neural ideal.

- [`commalg.octic-quotient-degree-eight`](commalg/octic-quotient-degree-eight/)
  certify degree-eight vanishing in an Artinian quotient.

- [`commalg.oscar-elimination-groebner-basis`](commalg/oscar-elimination-groebner-basis/)
  recovers the lexicographic elimination basis of two rational plane quadrics.

- [`commalg.oscar-prime-decompositions`](commalg/oscar-prime-decompositions/)
  certifies a minimal-prime decomposition and a primary hypersurface power.

- [`commalg.polymake-polynomial-arithmetic`](commalg/polymake-polynomial-arithmetic/)
  reproduce an exact multivariate polynomial tutorial calculation.

- [`commalg.polynomial-crt-reconstruction`](commalg/polynomial-crt-reconstruction/)
  reconstruct a rational polynomial from modular images.

- [`commalg.prime-interval-support`](commalg/prime-interval-support/)
  compute prime support in dyadic and short intervals by residue-ring arithmetic.

- [`commalg.projective-quartic-hilbert-polynomial`](commalg/projective-quartic-hilbert-polynomial/)
  computes the exact dimension, degree, and Hilbert polynomial of a projective
  quartic curve.

- [`commalg.rational-two-cycles-seven-torsion-identity`](commalg/rational-two-cycles-seven-torsion-identity/)
  verify the rational seven-torsion polynomial identity.

- [`commalg.reciprocal-progression-elementary-symmetric`](commalg/reciprocal-progression-elementary-symmetric/)
  evaluates an elementary symmetric polynomial on reciprocal integers.

- [`commalg.reducible-cubic-determinantal-representation`](commalg/reducible-cubic-determinantal-representation/)
  certify a symmetric determinant for a reducible plane cubic.

- [`commalg.reducible-ring-normalization`](commalg/reducible-ring-normalization/)
  normalizes a reduced union of three affine planes into three polynomial-ring
  components.

- [`commalg.reversible-binary-recurrence`](commalg/reversible-binary-recurrence/)
  verify Mathar's recurrence for reversible binary strings A032123.

- [`commalg.second-jet-xyz-radical`](commalg/second-jet-xyz-radical/)
  computes the radical and ten minimal primes of the explicit second jet of
  the hypersurface `xyz=0`.

- [`commalg.separating-rational-identity`](commalg/separating-rational-identity/)
  verifies an exact separating identity in a rational-function field.

- [`commalg.signed-ideal-intersection`](commalg/signed-ideal-intersection/)
  verify signed generators of a three-ideal intersection.

- [`commalg.singular-locus-saturation`](commalg/singular-locus-saturation/)
  recover a diagonal singular locus by saturation.

- [`commalg.sparse-surface-implicitization`](commalg/sparse-surface-implicitization/)
  eliminates a sparse parametrization to recover a 41-term sextic implicit
  equation and resolve two nonhomogeneous source typos.

- [`commalg.square-slack-ideal`](commalg/square-slack-ideal/)
  computes and saturates the principal slack ideal of a square.

- [`commalg.symbolic-two-torsion-root`](commalg/symbolic-two-torsion-root/)
  verify a symbolic two-torsion section of an elliptic Jacobian.

- [`commalg.three-quadric-groebner-normal-form`](commalg/three-quadric-groebner-normal-form/)
  compute a lexicographic Groebner basis and normal form for three quadrics.

- [`commalg.toric-ideal-implicitization`](commalg/toric-ideal-implicitization/)
  implicitize monomial curves and the quadratic Veronese map.

- [`commalg.two-point-secant-elimination`](commalg/two-point-secant-elimination/)
  certifies that the secant construction for two projective points eliminates
  to their joining line.

- [`commalg.zero-dimensional-quotient-minpoly`](commalg/zero-dimensional-quotient-minpoly/)
  compute minimal polynomials in a zero-dimensional quotient.

### `groups`

- [`groups.degree-four-permutation-actions`](groups/degree-four-permutation-actions/)
  checks orders, stabilizers, structural properties, and conjugacy data for the
  five transitive permutation groups of degree four.

- [`groups.flexrilog-order-five-symmetry`](groups/flexrilog-order-five-symmetry/)
  certifies an order-five rotation inside the full automorphism group of a
  25-vertex rigidity graph.

- [`groups.gelfand-tsetlin-weight-character`](groups/gelfand-tsetlin-weight-character/)
  recovers a six-dimensional `GL(3)` weight character from semistandard
  tableaux underlying Gelfand--Tsetlin data.

- [`groups.hurwitz-degree-nine-generating-triple`](groups/hurwitz-degree-nine-generating-triple/)
  certify a degree-nine Hurwitz generating triple.

- [`groups.igraph-complete-five-automorphisms`](groups/igraph-complete-five-automorphisms/)
  recovers `Aut(K_5)` and a point stabilizer from an IGraph/M test.

- [`groups.lr-ray-symmetry-group`](groups/lr-ray-symmetry-group/)
  certify the 144 symmetries of the SL3 LR chamber rays.

- [`groups.oscar-four-cube-automorphisms`](groups/oscar-four-cube-automorphisms/)
  constructs the order-384 facet automorphism group of the four-cube.

- [`groups.simplicial-cp2-automorphisms`](groups/simplicial-cp2-automorphisms/)
  recovers the order-54 automorphism group of a nine-vertex `CP^2`
  triangulation.

- [`groups.simplicial-torus-automorphisms`](groups/simplicial-torus-automorphisms/)
  recovers the order-42 automorphism group of a seven-vertex torus.

- [`groups.triple-product-property-search`](groups/triple-product-property-search/)
  search S3 for triple-product-property subsets.

### `topology`

- [`topology.bowtie-complex-homology`](topology/bowtie-complex-homology/)
  computes the face counts and homology of two triangles joined at one vertex.

- [`topology.hollow-triangle-homology`](topology/hollow-triangle-homology/)
  recovers the integral first homology of a three-edge cycle.

- [`topology.incremental-dialogue-nerve`](topology/incremental-dialogue-nerve/)
  build a finite nerve incrementally and certify its homology.

- [`topology.matroid-independence-complex-homology`](topology/matroid-independence-complex-homology/)
  computes the integral homology of a rank-three matroid independence complex.

- [`topology.real-projective-plane-integral-homology`](topology/real-projective-plane-integral-homology/)
  computes the integral homology of a ten-facet triangulation and retains its
  `Z/2` torsion.

- [`topology.secondary-example-primary-operations`](topology/secondary-example-primary-operations/)
  computes the mod-two cohomology and vanishing `Sq^2` input to a published
  secondary-operation example.

- [`topology.simplicial-cp2-homology`](topology/simplicial-cp2-homology/)
  computes the full integral homology of the nine-vertex triangulation of
  complex projective two-space.

- [`topology.simplicial-klein-bottle-homology`](topology/simplicial-klein-bottle-homology/)
  recovers the free and two-torsion parts of a triangulated Klein bottle's
  integral homology.

- [`topology.simplicial-mobius-strip-homology`](topology/simplicial-mobius-strip-homology/)
  computes the integral homology of a five-triangle Möbius strip.

- [`topology.simplicial-torus-homology`](topology/simplicial-torus-homology/)
  recovers integral homology ranks `(1,2,1)` for a seven-vertex torus.

- [`topology.simplicialhomology-basic-betti-numbers`](topology/simplicialhomology-basic-betti-numbers/)
  compute elementary simplicial Betti numbers over exact fields.

### `homalg`

- [`homalg.cellular-monomial-resolution`](homalg/cellular-monomial-resolution/)
  verifies the ordinary minimal resolution of a monomial ideal used in a
  cellular-resolution example.

- [`homalg.codepth-three-h43-resolution`](homalg/codepth-three-h43-resolution/)
  certifies Betti totals `(1,5,7,3)` beneath a codepth-three `H(4,3)`
  classification.

- [`homalg.codepth-three-resolution`](homalg/codepth-three-resolution/)
  certifies Betti totals `(1,5,6,2)` for a quotient used in a codepth-three
  classification.

- [`homalg.determinantal-module-annihilators`](homalg/determinantal-module-annihilators/)
  identify determinantal ideals as module annihilators.

- [`homalg.divisor-poset-hibi-resolution`](homalg/divisor-poset-hibi-resolution/)
  builds the Hibi generators of the divisor poset of 12 and reproduces its
  minimal Betti table.

- [`homalg.four-cycle-morse-resolution`](homalg/four-cycle-morse-resolution/)
  resolves the four-cycle edge ideal underlying a discrete-Morse example.

- [`homalg.generic-two-by-four-minors-resolution`](homalg/generic-two-by-four-minors-resolution/)
  resolves the six maximal minors of a generic `2 x 4` matrix and records two
  source corrections.

- [`homalg.graded-minimal-free-resolution`](homalg/graded-minimal-free-resolution/)
  certifies a minimal graded resolution with total Betti ranks `(1,5,5,1)`.

- [`homalg.homalg-module-functors`](homalg/homalg-module-functors/)
  compute Hom and Ext of presented polynomial modules.

- [`homalg.line-arrangement-jacobian-syzygies`](homalg/line-arrangement-jacobian-syzygies/)
  compute Jacobian syzygies of a singular line arrangement.

- [`homalg.oscar-module-kernel`](homalg/oscar-module-kernel/)
  computes and certifies the principal kernel of a polynomial-module map.

- [`homalg.persistence-exterior-square`](homalg/persistence-exterior-square/)
  identifies a persistence module's exterior square from its annihilator and
  complete sequence of Fitting ideals.

- [`homalg.rational-quartic-resolution`](homalg/rational-quartic-resolution/)
  resolves a rational quartic coordinate ring over `F_32003`.

- [`homalg.s4-squarefree-quadratic-resolution`](homalg/s4-squarefree-quadratic-resolution/)
  computes the ordinary resolution beneath an equivariant `S_4` Betti-character
  example.

- [`homalg.second-veronese-betti-table`](homalg/second-veronese-betti-table/)
  reproduces the second Veronese surface's Betti totals `(1,6,8,3)`.

- [`homalg.singularinterface-ideal-syzygies`](homalg/singularinterface-ideal-syzygies/)
  recover an ideal Groebner basis and its two syzygies.

- [`homalg.strongly-stable-betti-table`](homalg/strongly-stable-betti-table/)
  verifies the pure Betti table `(1,9,13,5)` of a strongly stable ideal from a
  weighted-Borel example.

- [`homalg.transverse-cone-cohomology`](homalg/transverse-cone-cohomology/)
  verifies a reduced exact cochain complex and its seven cohomology dimensions.

### `combin`

- [`combin.basic-enumerative-identities`](combin/basic-enumerative-identities/)
  verify factorial, Touchard, and Narayana polynomial identities.

- [`combin.basic-matroid-cryptomorphisms`](combin/basic-matroid-cryptomorphisms/)
  recovers rank, circuits, closure, duality, deletion, and contraction from a
  small matroid basis presentation.

- [`combin.bernhart-kainen-algebraic-graph`](combin/bernhart-kainen-algebraic-graph/)
  verifies the parity-coupled ten-cycle and two-triples construction of the
  16-vertex Bernhart--Kainen graph and its two automorphism orbits.

- [`combin.circulant-double-cover-stability`](combin/circulant-double-cover-stability/)
  verify stability of small circulant graph double covers.

- [`combin.cozero-divisor-wiener-index`](combin/cozero-divisor-wiener-index/)
  compute Wiener indices of cozero-divisor graphs of finite rings.

- [`combin.dundee-exact-winning-probabilities`](combin/dundee-exact-winning-probabilities/)
  compute exact winning probabilities for Dundee bids.

- [`combin.igraph-grid-spanning-trees`](combin/igraph-grid-spanning-trees/)
  counts the fifteen spanning trees of a `2 x 3` grid by an exact
  reduced-Laplacian determinant.

- [`combin.igraph-k4-spanning-trees`](combin/igraph-k4-spanning-trees/)
  certifies the sixteen spanning trees of `K_4` by the Matrix-Tree theorem.

- [`combin.integer-poset-invariants`](combin/integer-poset-invariants/)
  computes height, width, extrema, comparabilities, and symmetries of a
  six-element integer poset.

- [`combin.johnson-strongly-regular-graph`](combin/johnson-strongly-regular-graph/)
  construct and certify the Johnson graph J(5,2).

- [`combin.nowhere-zero-modular-flows`](combin/nowhere-zero-modular-flows/)
  enumerate nowhere-zero modular flows and verify orientation independence.

- [`combin.oscar-five-element-matroid`](combin/oscar-five-element-matroid/)
  derives the circuits of a rank-three matroid from its eight bases.

- [`combin.oscar-four-element-matroid`](combin/oscar-four-element-matroid/)
  recovers the circuits and Tutte polynomial of a matroid given by five bases.

- [`combin.oscar-k4-graphic-matroid`](combin/oscar-k4-graphic-matroid/)
  computes the exact Tutte polynomial of the graphic matroid of `K_4`.

- [`combin.permutation-cyclic-sieving`](combin/permutation-cyclic-sieving/)
  verify cyclic sieving for descents and complementation.

- [`combin.polymake-square-graph-automorphisms`](combin/polymake-square-graph-automorphisms/)
  compute automorphisms, stabilizers, and orbits of a square graph.

- [`combin.polymake-vector-matroid-invariants`](combin/polymake-vector-matroid-invariants/)
  recover bases, circuits, Tutte data, deletion, and contraction.

- [`combin.sylvester-denumerant-quasipolynomial`](combin/sylvester-denumerant-quasipolynomial/)
  interpolate the quasipolynomial for 6x+2y+3z=t.

- [`combin.uniform-matroid-direct-sum-tutte`](combin/uniform-matroid-direct-sum-tutte/)
  compute the Tutte polynomial of two copies of U(1,2).

- [`combin.weak-order-tamari-posets`](combin/weak-order-tamari-posets/)
  compare the order-three weak order and Tamari lattice.

- [`combin.zonal-polynomial-recurrence`](combin/zonal-polynomial-recurrence/)
  compute zonal polynomials from the partition recurrence.

### `geometry`

- [`geometry.antichain-probability-polytope`](geometry/antichain-probability-polytope/)
  verifies that the probability-functions polytope of a three-element
  antichain is the exact three-cube.

- [`geometry.order-four-permutahedron`](geometry/order-four-permutahedron/)
  construct the order-four permutahedron and enumerate its faces.

- [`geometry.order-three-permutahedron`](geometry/order-three-permutahedron/)
  constructs the order-three permutahedron and verifies its exact face data.

- [`geometry.oscar-cyclic-four-polytope`](geometry/oscar-cyclic-four-polytope/)
  constructs `C(4,8)` on the rational moment curve and certifies its face
  vector.

- [`geometry.oscar-pentagon-face-structure`](geometry/oscar-pentagon-face-structure/)
  recovers the rational facets, incidence, and face vector of the introductory
  OSCAR pentagon.

- [`geometry.oscar-triangle-square-product`](geometry/oscar-triangle-square-product/)
  computes the exact face vector of the Cartesian product of a triangle and a
  square.

- [`geometry.polymake-basic-exact-polytopes`](geometry/polymake-basic-exact-polytopes/)
  construct the same exact square from points and halfspaces.

- [`geometry.random-six-polytope-g-vectors`](geometry/random-six-polytope-g-vectors/)
  compute a g-vector for a sampled simplicial six-polytope.

- [`geometry.rational-platonic-face-vectors`](geometry/rational-platonic-face-vectors/)
  certifies the face vectors of rational tetrahedron, cube, and octahedron
  models.
