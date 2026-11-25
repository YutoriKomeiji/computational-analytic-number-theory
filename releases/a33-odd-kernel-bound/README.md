# Rational verification of a symmetric-kernel odd-sector norm bound

Research evidence package — 25 November 2026. Not the full submission manuscript. No external peer review.

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
Hence, using the analytic premises above, the odd-sector norm is strictly below $119/1000$. The numerical checker verifies the scalar inequalities, not the full analytic argument. Historical internal execution passed; independent external reproduction and review are not yet reported. This is an upper bound, not the actual norm or a claim of optimality, full Lean formalization, or RH. No novelty priority is asserted. Related work: I. Schur, DOI 10.1515/crll.1911.140.1; M. Anikushin and A. Romanov, [arXiv:2510.05585](https://arxiv.org/abs/2510.05585), on optimization of Schur test functions (abstract-level comparison only).

## Reuse

Original README: CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/) to the extent rights subsist and are held by the author. Original Python checker: MIT license below. Third-party material is not relicensed.

MIT License (Python checker only)

Copyright (c) 2026 Akihisa Ono

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
