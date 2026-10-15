# Compute exact tipsy cop-and-robber survival probabilities

Replay the source's ten-state path-distance transition model for seven rounds with `r=3/10`, `t=2/5`, and `c=3/10`. Exact matrix powers give survival probabilities; solving `(I−T)e=1` gives expected durations without the floating-point loss in the original Sage session.
