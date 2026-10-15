# Verify an order-eight cyclotomic-sequence linear complexity

Specialize the paper's Sage verification to `p=17`, `q=41` and their first common primitive root `g=6`. The CRT construction gives a 348-term binary generating polynomial. Its gcd with `x⁶⁹⁷−1` gives linear complexity 696, independently matching the paper's discrete-log formula.
