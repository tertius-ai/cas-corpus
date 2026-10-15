# Certified embeddings of a cubic field

For `K=Q(a)` with `a^3=2`, the source reports signature `(1,1)`: one real
embedding and one conjugate pair. It evaluates `a-1` at the real embedding
near `0.2599210499`.

Noether constructs the exact number field, checks trace and norm, and computes
all three embeddings as certified complex balls at 128-bit precision. The
real ball for `a-1` must overlap a narrow rational interval around the
published decimal, while the other two embeddings must have nonzero imaginary
parts.

