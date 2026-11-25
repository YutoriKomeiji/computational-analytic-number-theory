# Boundary-jet and affine connection formulas for truncated Legendre couplings

Research formula reference — 25 November 2026. This is a supporting research artifact, not the full submission manuscript.

Author: Akihisa Ono (小野昭久; GitHub: YutoriKomeiji). AI-assisted research and writing: Luminalia 9 Sisters using ChatGPT. The human author is responsible for the claims and release. This note has not undergone external peer review.

## Abstract
We give two finite exact representations of a shifted Legendre integral: a boundary-jet recurrence and an affine connection-coefficient contraction. The derivative depth of the first is bounded by the source polynomial degree; the second exhibits a signed diagonal metric. Classical orthogonality also gives a degree-uniform coefficient envelope. These are exact finite identities, not claims of numerical stability or infinite-dimensional positivity.

## 1. Boundary-jet recurrence
Let $P_j$ denote the ordinary Legendre polynomial, normalized by $P_j(1)=1$. For a real polynomial $f$, $a\in[-1,1]$, and integer $j\ge0$, define
$$
I_j(f;a)=\int_a^1 f(z)P_j(z)\,dz.
$$
For $j\ge1$, the classical derivative identity $(P_{j+1}-P_{j-1})'=(2j+1)P_j$ and integration by parts give
$$
I_j(f;a)=-\frac{f(a)(P_{j+1}(a)-P_{j-1}(a))}{2j+1}
-\frac{I_{j+1}(f';a)-I_{j-1}(f';a)}{2j+1}.
$$
The upper endpoint cancels. At index zero use $I_0(f;a)=\int_a^1f(z)\,dz$, evaluated exactly by integrating the polynomial (or its finite Taylor expansion about $a$). For degree at most $p$, derivative orders beyond $p$ vanish. Hence the recursive reduction terminates using at most $p+1$ derivative levels; no negative Legendre index is required. This bound concerns depth, not total runtime or the cost of evaluating large-index Legendre polynomials.

## 2. Shifted coupling and endpoint formula
Let $0<d<1$, $h=1-d$, $N_k=\sqrt{(2k+1)/2}$, and $\phi_k(x)=N_kP_k(2x-1)$. Changing variables $z=2(x+d)-1$ gives
$$
2\int_0^h\phi_p(x)\phi_j(x+d)\,dx
=N_j I_j(N_pP_p(\,\cdot-2d);2d-1).
$$
The shifted head endpoint is always $(2d-1)-2d=-1$. For $0\le m\le p$, the generating function $\sum_{p\ge0}P_p(x)t^p=(1-2xt+t^2)^{-1/2}$ gives at $x=1$, after $m$ differentiations, $(2m-1)!!t^m(1-t)^{-2m-1}$ (with $(-1)!!=1$). Extracting the coefficient of $t^p$ and applying parity yields
$$
P_p^{(m)}(-1)=(-1)^{p+m}\frac{(p+m)!}{2^m m!(p-m)!}.
$$
Thus the endpoint derivatives of the translated head polynomial are independent of the shift, but the full integral depends on the shift through the lower cut and other endpoint values. For a finite source sum the identities apply termwise, with no infinite-series exchange asserted.

## 3. Independent affine contraction
Set $\alpha=1-d$, and define $C_m(r)$ by
$$
P_m(\alpha t-d)=\sum_{r=0}^m C_m(r)P_r(t).
$$
By parity, the coefficients of $P_m(\alpha t+d)$ are $(-1)^{m+r}C_m(r)$. Substituting $z=d+\alpha t$ into
$$
J_{j,i}(d)=\int_{2d-1}^1 P_j(z)P_i(z-2d)\,dz
$$
and using Legendre orthogonality gives
$$
J_{j,i}(d)=\alpha\sum_{r=0}^{\min(i,j)}
(-1)^{j+r} C_j(r)C_i(r)\frac{2}{2r+1}.
$$
The coefficients can be computed from the classical three-term recurrence, starting with $P_0=1$, $P_1(\alpha t-d)=\alpha t-d$, and using
$$
tP_r(t)=\frac{r+1}{2r+1}P_{r+1}(t)+\frac r{2r+1}P_{r-1}(t)
$$
with the second term absent at $r=0$.

For a finite odd-index set, define $C$ to have rows $C_m$ padded with zeros to a common finite length, $N$ diagonal with entries $N_m$, and $D=\operatorname{diag}((-1)^r2/(2r+1))$. Writing $J$ for the matrix with entries $J_{j,i}(d)$ on this index set, the normalized source matrix $-2cNJN$, for a real scalar $c$, equals $2c\alpha(NC)D(NC)^{\mathsf T}$. This is a signed metric representation, not a positive-semidefinite factorization.

## 4. Coefficient envelope
For $t\in[-1,1]$, $\alpha t-d\in[-1,1]$, so $|P_m(\alpha t-d)|\le1$. Orthogonality implies
$$
\sum_{r=0}^{m}\frac{2}{2r+1}C_m(r)^2\le2,
\qquad |C_m(r)|\le\sqrt{2r+1}.
$$
Writing $W=\operatorname{diag}(2/(2r+1))$, the Cauchy–Schwarz inequality gives $|c_m D c_k^{\mathsf T}|\le2$ for padded rows $c_m,c_k$, since $D=W^{1/2}\operatorname{diag}((-1)^r)W^{1/2}$. This analytic envelope alone proves neither numerical stability nor a sharp operator norm bound.

## 5. Scope and evidence
The identities above are analytic finite statements. The underlying derivative identities, generating function, parity, affine basis transformations and orthogonality are classical; no novelty is claimed for these ingredients. The purpose of this note is to organize them into two distinct evaluation paths for the same integral. No priority or novelty claim is made. Gao and Iserles, [arXiv:2308.08266](https://arxiv.org/abs/2308.08266), Lemma 1, cover the corresponding cross-index recurrence via their general connection-coefficient framework. For head degree below tail index, Rodrigues' formula also gives a direct boundary evaluation. The endpoint derivative formula at +1 is stated by Wunderlich et al., [arXiv:2509.22904](https://arxiv.org/abs/2509.22904), equation (3); the -1 form follows by parity. These relationships are not evidence of computational superiority.

The general identities are established by the analytic derivations above, not by numerical tests or Lean. Historical formal support for elementary endpoint alignment is not a formalization of the full note. This note does not claim numerical stability, high-degree interval certification, infinite-tail positivity, or any result on the Riemann hypothesis.

## References

NIST Digital Library of Mathematical Functions, Chapter 18, *Orthogonal Polynomials*, [§18.3 (definitions and orthogonality)](https://dlmf.nist.gov/18.3), [§18.9 (recurrence relations and derivatives)](https://dlmf.nist.gov/18.9), [§18.12 (generating functions)](https://dlmf.nist.gov/18.12), and [§18.14 (inequalities)](https://dlmf.nist.gov/18.14). These are references for the classical ingredients; they are not evidence of novelty for the combined representation.

## Reuse

This original note is offered under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) to the extent copyright or similar rights subsist and are held by the author. Attribution: Akihisa Ono (YutoriKomeiji). Identify the source and indicate changes as required by the license. Third-party references are not relicensed.
