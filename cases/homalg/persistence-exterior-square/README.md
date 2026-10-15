# Exterior square of a barcode module

Over `R=Q[t]`, the paper's example has underlying module

```text
M = R + R/(t^3) + R/(t^2) + R/(t).
```

Construct this presentation and compute `Lambda^2 M`. The exterior square has
six generators. Its annihilator must be `(t^3)`, and its Fitting ideals
`Fitt_0,...,Fitt_6` must be generated respectively by

```text
t^10, t^7, t^5, t^3, t^2, t, 1.
```

Over the PID `Q[t]`, these invariants identify

```text
Lambda^2 M = R/(t^3) + (R/(t^2))^2 + (R/(t))^3,
```

as predicted by the paper. This case asserts the exact underlying module, not
a reconstruction of persistence intervals or a persistence-specific grading
certificate.
