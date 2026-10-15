# Checkable Gröbner witnesses

GroebnerTactic uses CAS output to discharge Lean goals about remainders,
membership, and equality of ideals. This translation asks Noether for verified
reduction records, checks their multiplier identity directly, distinguishes a
nonmember by its nonzero remainder, and certifies a source ideal-equality
example in both directions.
