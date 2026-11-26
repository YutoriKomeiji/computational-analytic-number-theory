# Weighted variance under block splitting and a chosen-center prime-bin estimate

Research method reference — 26 November 2026. Author: Akihisa Ono (YutoriKomeiji). AI-assisted derivation, checking and writing: Luminalia 9 Sisters using ChatGPT. The human author is responsible for the claims. No external peer review.

## 1. Exact block decomposition and a false shortcut

For a finite nonempty set $X$ of real observations $y_i$ with positive weights $w_i$, put $W_X=\sum w_i$, $\mu_X=\sum w_i y_i/W_X$, and $V_X=\min_c\sum w_i(y_i-c)^2$. For disjoint nonempty blocks $P,Q$,
$$
V_{P\cup Q}=V_P+V_Q+\frac{W_PW_Q}{W_P+W_Q}(\mu_P-\mu_Q)^2.
$$
Indeed $\sum_{i\in X}w_i(y_i-c)^2=V_X+W_X(c-\mu_X)^2$; minimize the sum of the two quadratics. The formula is classical. The unnormalized minimized sum cannot decrease when observations are added. The normalized variance need not share this property.

In contrast, $V_{P\cup Q}\le V_P+\sum_{i\in Q}w_i y_i^2$ is false: take unit weights and the single observations 1 and 0, respectively; the left side is $1/2$ and the right side is zero. The between-block term cannot be omitted.

## 2. A chosen-center estimate for primes

Let $e<a<b$, let $\theta(x)=\sum_{p\le x}\log p$ with $p$ prime, and suppose $|\theta(x)-x|\le H$ for all $x\in[a,b]$. Use weights $p$ and observations $u(p)=\log(p)/p$ for primes in $(a,b]$. Set $V=0$ if there are no primes. Put
$$
c=\frac{2\log a}{a+b},\quad
\Phi(x)=\frac{(u(x)-c)^2}{u(x)},\qquad u(x)=\frac{\log x}{x}.
$$
Evaluating the objective at $c$, rather than dividing by the discrete total weight, gives $V\le\int_{(a,b]}\Phi\,d\theta$. In the continuous reference,
$$
\int_a^b\Phi(x)\,dx
\le \frac{\log^2 b-\log^2 a}{2}
-\frac{2(b-a)\log a}{a+b}.
$$
To see this, expand $\Phi=u-2c+c^2/u$, use $\int_a^b dx/u(x)\le (b^2-a^2)/(2\log a)$, and substitute $c$.

Write $E(x)=\theta(x)-x$. Stieltjes integration by parts for this right-continuous function and smooth $\Phi$ gives
$$
\left|\int_{(a,b]}\Phi\,dE\right|
\le H\bigl(\Phi(a)+\Phi(b)+\operatorname{Var}_{[a,b]}\Phi\bigr).
$$
Since $u$ decreases on $[a,b]$ and $v\mapsto(v-c)^2/v$ has at most one interior minimum on $v>0$, the variation is at most $\Phi(a)+\Phi(b)$. Thus
$$
V\le\frac{\log^2 b-\log^2 a}{2}
-\frac{2(b-a)\log a}{a+b}+2H(\Phi(a)+\Phi(b)).
$$
The result applies also to any subset of the primes, by evaluating its nonnegative objective at the same chosen center. It requires no lower estimate on prime mass. It remains conditional on the specified discrepancy bound $H$.

## 3. Harmonic bins

For $a=k/(m+1)>e$, $b=k/m$, $m\ge1$ integral, let $r_m=\log(1+1/m)$ and $c_m=r_m-2/(2m+1)>0$. The continuous term in Section 2 equals
$$
c_m\log k+d_m,\qquad
d_m=-c_m\log(m+1)+r_m^2/2\le 1/(2m^2).
$$
Here $r_m=2\operatorname{atanh}(1/(2m+1))>2/(2m+1)$ and $\log(1+1/m)\le1/m$. Summing the continuous terms over any finite set of admissible bins gives at most
$$
(2-2\log2-\gamma)\log k+\pi^2/12,
$$
where $\gamma$ is Euler's constant. Indeed $\sum_{m=1}^N c_m=\log(N+1)-2H_{2N+1}+H_N+2$, with $H_n$ the harmonic numbers; take the limit. This bounds the continuous reference only; the discrepancy terms and higher prime powers still require separate bounds.

## 4. Scope and related work

The exact block identity, least-squares minimization and Stieltjes integration by parts are classical. Related computational variance literature: Chan, Golub and LeVeque, *Algorithms for Computing the Sample Variance: Analysis and Recommendations* (1983), DOI 10.1080/00031305.1983.10483115. For explicit Chebyshev discrepancy estimates see Broadbent, Kadiri, Lumley, Ng and Wilk, arXiv:2002.11068. No particular numerical discrepancy constant from that work is asserted here. The prime-bin construction is a method reference, not a novelty claim or an all-parameter certificate. The full finite/analytic source reconstruction, penalty terms and higher-power corrections are outside this note. No RH claim follows.

Original note offered under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/) to the extent rights are held by the author. Third-party references are not relicensed.
