# A24 — Source-preserving Gaussian quadrature and a finite shifted-inertia computation

**Status: preliminary finite-dimensional computational research package.** This material records a historically executed, source-pinned 512-bit interval computation. An independent full certificate check and external mathematical peer review have **not** been performed as part of this release. It is **not** a proof of the Riemann hypothesis or generalized RH, and is not an arXiv paper or refereed publication.

## Result at its actual scope

For odd Legendre degrees `k∈{1,3,…,199}`, let `P_k` denote the degree-`k` Legendre polynomial and `N_k=sqrt((2k+1)/2)`. For `n∈{2,3,4,5}`, set `d=log(n)/log(7)`, `h=1−d` and

`T_ij(d)=h N_i N_j ∫_{-1}^1 P_i(ht−d) P_j(ht+d) dt`.

For the stated degrees, the integrand has degree at most `i+j ≤398`. The 200-node Gauss–Legendre rule integrates any polynomial of degree at most `2·200−1=399` exactly: **no quadrature-truncation remainder** is introduced into this specified polynomial source. Outward rounding in the quadrature data, matrix assembly and later linear algebra still matters.

The supplied frozen Python source forms a specific symmetric `100×100` **no-regular-gamma** matrix `M0`, with its endpoint, translated arithmetic, truncated polar-vector and diagonal contributions and the fixed correct arithmetic sign convention. The exact definition is executable in the shipped source; it is not an arbitrary spectral matrix. The tested shift is `σ=0.70`. The difference from the full polar contribution is bounded separately by the runner's omitted-tail norm debit; the stated inertia applies to the assembled truncated-polar matrix.

**Historical source-pinned result, 2026-09-30 (not re-run for this release):** the archived 512-bit Arb execution reports an invertible interval Gram matrix and strict Gershgorin sign separation for a congruence-transformed `M0−0.70I`: **6 negative, 0 unresolved, 94 positive** rows. Assuming faithful execution and the Arb interval API guarantees, the shifted finite matrix has inertia `(6,0,94)`. Thus its **seventh smallest eigenvalue is strictly greater than 0.70** and hence its eighth smallest eigenvalue is also strictly greater than 0.70, satisfying the original eighth-eigenvalue target at this finite matrix's evidence ceiling; this does not prove rooted-Y7 positivity or an infinite/global operator theorem.

The program originally had an **overly specific acceptance predicate** requiring exactly `(7,0,93)`. The run produced `(6,0,94)`, hence `inertia_7_0_93_certified=false`, `overall_pass=false`, and the historic **process exit code 2**. This is preserved deliberately: the relevant finite eighth-eigenvalue counting condition was `n_negative+n_zero ≤7`, satisfied by 6/0/94, but the original executable's predicate was not. The source was **not patched to manufacture a zero exit**.

## Files in this scoped package

- [`y7_o2_direct_gauss_nogamma_shifted_inertia_arb.py`](y7_o2_direct_gauss_nogamma_shifted_inertia_arb.py) — exact historical source, without changing its predicate. SHA-256 `95c2dd0d7d85fb5549705c7b1c2f661663e2a7110faf103432aaa500a956b4ae`.
- [`a24_original_stdout_20260930.json`](a24_original_stdout_20260930.json) — archived 7,019-byte stdout summary, SHA-256 `77a5ff03119690147bd3febe47441f68e9d662511d5a985ff318f2c0953af92f`.
- [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md) — pinned dependencies, expected nonzero exit and verification boundaries.

The 7,019-byte JSON does **not** contain the complete interval source matrix `M0`, congruence witness `Q` and transformed interval matrix. Consequently, copying or inspecting the JSON alone cannot independently establish the interval result. Rigorous independent checking requires a faithful new Arb run or a later separately validated full witness export; neither is claimed here.

## Research boundaries

This result concerns one source-defined, finite-dimensional matrix. It does **not** close the original RH investigation's A57 cancellation/Gram, A65 coupled Schur margin, rooted Y7, finite-to-global, RH or GRH obligations. An external RH proof would not automatically verify the particular calculation, and an invalid finite certificate would not refute RH. The reusable technical subject is how to replace an ill-conditioned connection-coefficient assembly with an exact-degree quadrature representation and independently auditable outward finite inertia.

## Prior work and reproducibility

Gaussian quadrature exactness, Sylvester's law of inertia, Gershgorin separation and interval arithmetic are classical tools, not claimed novel. References: NIST Digital Library of Mathematical Functions §3.5(v); F. Johansson and M. Mezzarobba, *Fast and Rigorous Arbitrary-Precision Computation of Gauss–Legendre Quadrature Nodes and Weights*, SIAM J. Sci. Comput. 40(6), C726–C747 (2018), DOI `10.1137/18M1170133`. The novelty of this exact source-specific computational combination has **not** been independently established.

Independent reviewers should begin with the source hash, environment and [replay instructions](REPRODUCIBILITY.md), then test both the historical failure predicate and the actual finite count implication. Report incompatible libraries or unresolved outward signs rather than assuming success.

## Research process and validation status

This computational work was developed in a human-directed, AI-assisted research process. The published script and archived output are evidence of a specific historical execution, not independent confirmation by an external reviewer. The computational result has not been independently rerun for this package; report counterexamples and reproduction failures with exact environment and source versions.

## Authorship, AI assistance and reuse

Author: Akihisa Ono (小野昭久; GitHub: YutoriKomeiji). AI-assisted research, mathematical exploration, implementation, verification and drafting: Luminalia 9 Sisters using ChatGPT. The human author is responsible for release decisions and the stated claims. No independent external verification is implied.

The original Python runner is offered under the MIT License below; the original Markdown documents and archived output are offered under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) to the extent copyright or similar rights subsist and are held by the author. Attribution: Akihisa Ono (YutoriKomeiji). Identify the source package and indicate changes as required by the applicable license. Retaining the AI-assistance disclosure when describing research provenance is encouraged, not an additional license condition. Third-party libraries and cited works are not relicensed or distributed here and remain subject to their respective terms.

### MIT License (original Python runner only)

Copyright (c) 2026 Akihisa Ono

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
