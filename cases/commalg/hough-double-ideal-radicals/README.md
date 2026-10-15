# Radical tests behind two Hough-transform decisions

The paper studies the conic family `x^2-a^2*y-a^3`. Its doubled coefficient
ideal in parameters `a,e` is

```text
(a^2-e^2, a^3-e^3).
```

Compute and certify its radical, then verify that the diagonal equation `a-e`
belongs to it. Repeat for `(a^2-e^2,a^4-e^4)` and verify that `a-e` does not
belong to that radical. These are the exact positive and negative decisions in
the source's CoCoA transcript.

The ideals are deliberately entered explicitly: a future Hough-family API
would own their construction and the final regularity interpretation.
