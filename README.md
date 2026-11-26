# Computational Analytic Number Theory

A public-facing home for carefully scoped computational research, reproducible verification, and independent review in analytic number theory.

## Status

**Five supporting research packages are now available.** The full manuscripts are in preparation. This repository is not a claim to have proved the Riemann hypothesis (RH), generalized RH, or any other open problem.

This public repository is **separate from the private internal research workspace**. It has its own history and will contain only separately reviewed, explicitly approved public release packages. Unpublished notes, internal evidence archives, raw session logs, credentials, and private repository history are not mirrored.

## Research packages

| Package | Contents | Evidence and scope |
| --- | --- | --- |
| [Finite inertia via direct Gaussian quadrature](releases/a24-finite-inertia/) | Historical interval computation, original runner and reproducibility notes | Finite 100-dimensional result; historical run reported six negative and 94 positive eigenvalues, original non-passing overall status preserved; independent complete certificate replay pending. |
| [Boundary-jet and affine connection formulas](releases/a30-legendre-boundary-jet/) | Exact finite Legendre integral identities and prior-art discussion | Classical formulas; no claim of numerical superiority or general novelty. |
| [Odd-sector symmetric-kernel bound](releases/a33-odd-kernel-bound/) | Analytic premises and two exact rational Python checkers | Upper bounds below 0.119 (endpoint estimate) and 0.101 (16-cell partition) for the same kernel and odd subspace; not an optimal norm or external peer-reviewed result. |
| [Conditional finite-rank inertia margins](releases/a15-conditional-inertia/) | Classical min-max implication and rational margin check | Conditional 549-dimensional instance; complete matrix premises not independently reproduced. |
| [Weighted variance and prime-bin estimates](releases/a16-a17-weighted-variance/) | Exact block identity and conditional chosen-center Stieltjes estimate | Continuous reference bound for harmonic bins; discrepancy and higher-prime-power terms and full all-parameter result not certified here. |

Further material is in preparation on full finite-rank certificate reconstruction, weighted-variance discrepancy bounds, and parameter-family operator certificates. These are research directions, not announcements of completed or accepted papers. Releases are selective and may be revised as independent checks and literature comparisons proceed.

## What to expect

- Source-pinned methods and precise mathematical statements, including their domains, conventions and assumptions.
- Small reproducible computational experiments and independent-checking procedures when they are cleared for public release.
- Explicit distinctions among historical run receipts, independently reproduced results, rigorous outward interval certificates, formal typechecking, mathematical proofs, and conjectures.
- Negative findings, unresolved obligations, prior-art comparisons and known limitations.

## Evidence and claim policy

A published research package must identify its source version and digest (see the [release digest inventory](SHA256SUMS)), dependencies, exact reproducer, expected output, evidence limitations, attribution, relevant licenses, and an explicit claim ceiling. A finite experiment never implies a global theorem by itself. A green Lean build is not automatically a mathematical review or evidence of RH.

**All RH/GRH claims remain unproven within this repository unless a specific, independently checkable argument is actually published and reviewed.** None of the current packages asserts such a proof.

## Participation

Independent, technically specific reviews, reproduction reports, falsification attempts and corrections are welcome. Please identify the package, exact version, mathematical statement or reproduction command, and evidence when reporting a discrepancy. Please do not post sensitive data.

## Release boundary

This index documents the repository's purpose, public packages and verification standards. Publication of research results, datasets, manuscripts or contact with third-party projects remains subject to explicit owner approval of the exact content and destination. No external RH proof or participation status is asserted here.
