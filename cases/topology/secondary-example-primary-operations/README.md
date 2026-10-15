# Primary data for an Adem secondary-operation example

The paper gives an explicit simplicial complex on 11 vertices by listing 19
maximal simplices. Over `F_2`, compute its homology and cohomology ring. Verify

```text
(b0,b1,b2,b3,b4,b5) = (1,0,4,0,0,1)
```

and compute `Sq^2` on every basis class in `H^2`. All four images must vanish,
so the kernel used as the domain of the paper's secondary operation has
dimension four.

This is a faithful execution of the now-supported primary portion of the
published example. It stops before `Psi_2`, whose domain, indeterminacy, and
chain-level evidence are not represented by Noether 0.2.
