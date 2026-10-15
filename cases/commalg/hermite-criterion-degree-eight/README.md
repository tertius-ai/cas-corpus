# Expand a degree-eight Hermite-criterion polynomial

Translate the source's `HC(5, 27, ...)` computation literally: distribute the binary-place weights of 27, retain the multiples of 31 selected by Hermite's criterion, and collect the resulting polynomial over `GF(2)`. The exact result has total degree 27 and 42 nonzero terms after characteristic-two cancellation.
