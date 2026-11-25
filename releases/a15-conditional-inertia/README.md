# Conditional spectral margins from a finite-rank inertia certificate

Research method reference — 26 November 2026. Author: Akihisa Ono (YutoriKomeiji). AI-assisted mathematical derivation, checking and writing: Luminalia 9 Sisters using ChatGPT. The human author is responsible for the claims and release. No external peer review.

## A finite-dimensional implication

Let $S,S_0$ be real symmetric $N\times N$ matrices, $U$ a real $N\times r$ matrix, and $1\le r<N$. Suppose $e\ge0$, $c>0$, $M>0$, $t\ge0$, and
$$
\|S-S_0\|_2\le e,\quad U^{\mathsf T}S_0U\preceq-cI_r,\quad
\|U\|_F^2\le M,\quad S_0+tUU^{\mathsf T}\succeq bI_N.
$$
If $a=c-Me>0$ and $h=b-e>0$, then, in increasing eigenvalue order,
$$
\lambda_r(S)\le-a/M<0,\qquad \lambda_{r+1}(S)\ge h>0.
$$
In particular the inertia, in the order (negative, zero, positive), is $(r,0,N-r)$.

Proof. For any vector $v$, $v^{\mathsf T}U^{\mathsf T}SUv\le-a\|v\|^2$. This forces $U$ to have rank $r$. Also $\|Uv\|^2\le M\|v\|^2$, so the Rayleigh quotient on $\operatorname{ran}U$ is at most $-a/M$. On $\ker U^{\mathsf T}$, the rank correction vanishes and $x^{\mathsf T}Sx\ge(b-e)\|x\|^2$. That subspace has dimension $N-r$. The two eigenvalue bounds follow from the min-max principle. This is a classical finite-dimensional argument, not a new general inertia theorem.

## Historical numerical instance, conditional on its matrix certificate

A previous internal interval computation for a residualized restricted-resolvent Schur matrix reported $N=549$, $r=7$, $c=11/50$, $M=8$, $t=16$ and
$$
e=\frac{903276691633242821798377993487}{9698771061225000000000000000000000},
\qquad b=\frac{4801981231}{938450000000}.
$$
Exact rational arithmetic gives $c-Me>219/1000$ and $b-e>5/1000$. Under the stated matrix premises, this implies $\lambda_7(S)<-219/8000$ and $\lambda_8(S)>1/200$ and inertia $(7,0,542)$.

Reproduce just the rational comparisons using Python 3 standard library (assertions enabled):

```python
from fractions import Fraction as Q
e = Q(903276691633242821798377993487, 9698771061225000000000000000000000)
b = Q(4801981231, 938450000000)
assert Q(11,50)-8*e > Q(219,1000)
assert b-e > Q(1,200)
print('PASS: conditional spectral margins')
```

This check verifies the arithmetic implication, not the four matrix premises. The complete matrix definition, frozen inputs, interval reconstruction and full independent certificate replay are not included here. The historical certificate used separate outward source-error, residual and finite-rank witness checks. This note deliberately does not present the 549-dimensional instance as independently reproduced. No statement about a distinct infinite-dimensional operator, rooted positivity, or the Riemann hypothesis follows from the finite-dimensional implication alone.

## Related work and reuse

J. H. Maddocks, *Restricted quadratic forms, inertia theorems, and the Schur complement*, Linear Algebra and its Applications 108 (1988), 1–36, DOI: [10.1016/0024-3795(88)90177-2](https://doi.org/10.1016/0024-3795(88)90177-2). Classical inertia and Schur-complement theory are not claimed as novel. The note isolates a checkable implication and its trust boundary.

Original note offered under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/) to the extent rights subsist and are held by the author. Third-party references are not relicensed.
