# Rational verification of a symmetric-kernel odd-sector norm bound

Research evidence package — 25 November 2026; reproduction update 26 November 2026. Not the full submission manuscript. No external peer review.

Author: Akihisa Ono (YutoriKomeiji). AI-assisted research and implementation: Luminalia 9 Sisters using ChatGPT. Human author responsible for release and claims.

## Target and analytic premises

Set $L=\log 7$, $A=L/2$, and define $\rho(0)=1/4$ and
$$
\rho(z)=\frac{\exp(3z/2)}{\exp(2z)-1}-\frac1{2z},\quad 0<z\le L.
$$
The target is the restriction to odd functions of the integral operator with kernel $-A\rho(A|x-y|)$ on $L^2([-1,1],dx)$. Reflection preserves the sector and the constant kernel annihilates odd functions. With $d=1/4-\rho$, the effective kernel is $A d(A|x-y|)$. The analytic input is $0\le\rho\le1/4$ on $[0,L]$: the upper inequality follows from the nonnegative power-series coefficients of $(2+z)\sinh z-2z\exp(z/2)$; the lower follows from $h(z)=2z-\exp(z/2)+\exp(-3z/2)$, with $h(0)=h'(0)=0$, $h''(z)=\exp(-3z/2)(9-\exp(2z))/4$ and $h'(L)>0$. The endpoint follows from the continuous extension.

Let $D(s)=\int_0^s d(z)dz$ and $\beta(s)=2D(s)$. Row integrals are $D(A(1+x))+D(A(1-x))$. Their arguments sum to $L$, and the smaller is at most $L/2$. Since $D$ is nondecreasing, row and column bounds are at most $D(L)+D(L/2)$. Schur's test therefore gives the norm bound $(\beta(L)+\beta(L/2))/2$.

The scalar identity, obtained by substituting $u=\exp(s/2)$ in the primitive of $\rho$, is
$$
\beta(s)=s/2-\pi/2+2\arctan(1/u)+
\log\left(\frac{s(u+1)}{4(u-1)}\right).
$$

## Reproduce the scalar certificate

Run with Python 3 (standard library only, assertions enabled; do not use -O):
```
python a33_sharper_bound.py
```

The checker uses exact Fraction arithmetic, integer square-root brackets, Machin's identity and rigorously bounded arctangent and logarithm series. Expected output:
```
PASS: beta(L) and beta(L/2) exact rational enclosures; combined bound < 119/1000
```

The exact rational inequalities are
$$
0.19969390622<\beta(L)<0.19969390624,\qquad
0.03757957692<\beta(L/2)<0.03757957693.
$$
Hence, using the analytic premises above, the odd-sector norm is strictly below $119/1000$. The numerical checker verifies the scalar inequalities, not the full analytic argument. Historical internal execution passed. External human peer review is not established. This is an upper bound, not the actual norm or a claim of optimality, full Lean formalization, or RH. No novelty priority is asserted. Related work: I. Schur, DOI 10.1515/crll.1911.140.1; M. Anikushin and A. Romanov, [arXiv:2510.05585](https://arxiv.org/abs/2510.05585), on optimization of Schur test functions (abstract-level comparison only).

## Second certificate: 16-cell partition

The revised manuscript (not included in this package) uses a sharper bound for the **same kernel and odd subspace**, based on the same nonnegative deficit and primitive. For $n=16$ and $s\in[iL/n,(i+1)L/n]$, monotonicity gives
$
D(s)+D(L-s)\le D((i+1)L/n)+D((n-i)L/n).
$
The maximum of these 16 upper bounds covers every row and, by symmetry, every column. Schur's test then gives the norm bound. The checker encloses each endpoint using rational root brackets, logarithm and arctangent series. No grid-point sampling assumption is made.

Run with Python 3, assertions enabled:

```
python a33_partition_bound.py
```
Expected output:
```
PASS: all 16 row/column envelopes < 101/1000
Diagnostic largest upper endpoint: 0.10002113206245009
```

The decimal is diagnostic only; the strict comparison with $101/1000$ uses exact rational arithmetic. The two certificates prove upper bounds, not the exact norm. Neither checker verifies the analytic premises automatically.

For completeness, the upper bound on $\rho$ can be checked directly: in $(2+z)\sinh z-2z e^{z/2}$ the coefficient of $z^j$, multiplied by $j!$, is $2-2j/2^{j-1}$ for odd $j\ge1$, and $j(1-2/2^{j-1})$ for even $j\ge2$. These are nonnegative (the $j=1,2$ coefficients vanish). For the lower bound, $h''$ changes from positive to negative at $\log3$; $h'(0)=0$ and $h'(L)=2-\sqrt7/2-3/(2\,7^{3/2})>0$, so $h'\ge0$ on the interval. This proves the analytic premises including the continuous endpoint.

## Version and integrity

Certificate files, 25 November 2026, with reproduction instructions updated 26 November 2026:

| File | SHA-256 |
| --- | --- |
| [a33_sharper_bound.py](a33_sharper_bound.py) — endpoint bound < 0.119 | 295e3ef288a97ef439aee624403783c7f2bbeccf7c186f8c217dab3b73d365c6 |
| [a33_partition_bound.py](a33_partition_bound.py) — partition bound < 0.101 | 4141bacfdcf97a683f370f2314ba19795d73e4a1c1e05a169d3ae727884dc3fc |

The second file is unchanged from the checker accompanying the revised manuscript. Its exact source was internally rerun under Python 3.13.5 with exit code 0 on 26 November 2026. The full manuscript is not released here. No arXiv submission, endorsement or external human peer review is asserted.

## Reuse

Original README: CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/) to the extent rights subsist and are held by the author. Both original Python checkers: MIT license below. Third-party material is not relicensed.

MIT License (both Python checkers only)

Copyright (c) 2026 Akihisa Ono

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
