# A24 — Independent reproduction procedure for the finite Arb512 case

**Status: reproduction instructions for a preliminary, source-pinned finite-dimensional computation.** This document describes a new independent execution that a reviewer can attempt; it does **not** say that such an execution has occurred. The original historical runner's process exit is **2**, not zero.

## Inputs / exact provenance

| File | Expected SHA-256 | Scope |
|---|---|---|
| `y7_o2_direct_gauss_nogamma_shifted_inertia_arb.py` | `95c2dd0d7d85fb5549705c7b1c2f661663e2a7110faf103432aaa500a956b4ae` | Original frozen historical runner, unmodified. |
| `a24_original_stdout_20260930.json` | `77a5ff03119690147bd3febe47441f68e9d662511d5a985ff318f2c0953af92f` | Original stdout, exactly 7,019 bytes; historical result only. |

The original runner's recorded source commit was `2a33d2d8fd53a7f628fc1a51f0ef1b88bb3abb04` and archived stdout date 2026-09-30; those source identifiers document provenance, **not a public checkout or URL dependency**. The standalone package must contain both files itself.

Historical runtime: Python 3.12.14, python-flint 0.9.0 / FLINT 3.6.0, NumPy 2.3.5, Linux x86_64/glibc 2.39, Arb context 512 bits. Pin and inspect actual versions; different build/runtime combinations need independent interpretation. The script imports only the `flint` library, NumPy and Python standard modules. Execute in a disposable environment after reviewing the source, not as a trusted binary.

## Re-run one fixed computation

From this package directory, in a compatible isolated Linux runtime:

```bash
python3 --version
python3 -c 'import flint,numpy; print(flint.__version__,numpy.__version__)'
sha256sum y7_o2_direct_gauss_nogamma_shifted_inertia_arb.py a24_original_stdout_20260930.json

# Do not use set -e: the original runner returns 2 on the observed finite outcome.
python3 y7_o2_direct_gauss_nogamma_shifted_inertia_arb.py > a24_replay.stdout.json 2> a24_replay.stderr.txt
status=$?
printf 'runner_exit_code=%s\n' "$status"
sha256sum a24_replay.stdout.json a24_replay.stderr.txt
```

Record UTC, operating system, pinned source hash, library/binary versions, command, exit status, raw stdout+stderr hashes, wall time and CPU/RAM limits. The historical run lasted ~8.7 seconds; this is not a runtime guarantee. No parameter search, changing matrix source, post-hoc witness tuning or artificial exit-zero conversion is permitted in a purported same-source reproduction.

## Expected evidence fields and critical checks

The historical JSON reports `N=100`, `prec_bits=512`, `gauss_order=200`, `max_integrand_degree=398`, `gauss_exact_degree=399`, and the fixed shifted source assembly. It reports `gram_invertible=true`; `negative_disc_count=6`, `positive_disc_count=94`, `unresolved_rows=[]`; reported minimum signed Gershgorin and Gram margins have strictly positive outward lower ends. The 100 indices must be partitioned exactly once among negative and positive rows.

The old program checks for **exactly 7 negative/93 positive**, sets `inertia_7_0_93_certified=false`, `overall_pass=false` and exits **2** in the historical outcome. A fresh faithful run may reproduce this same nonzero exit and still contain the finite signed count `6/0/94`. Treat the **actual claimed finite eighth-eigenvalue implication** as a separately checked consequence of `n_negative+n_zero≤7` and of the source/API/outward-interval contract; do not equate the obsolete program gate with the correct finite mathematical threshold.

The archived JSON prints selected margins and summary counts; it omits complete outward interval `M0`, interval congruence basis `Q`, and `Qᵀ(M0−0.70I)Q`. Reading it, matching text SHA or running ordinary binary floating arithmetic does **not** independently verify the full interval enclosure. Strict reproducibility is a complete same-source Arb replay with all sign decisions and Gram checks retained, or a later full witness export reviewed independently.

**FAIL_CLOSED** if SHA or fixed definitions differ, the matrix is not symmetric under stated source, Gram invertibility/sign margins are undecidable, there are unresolved row signs, the outdated exact-tuple acceptance code is silently modified, or the runtime/API contract is incompatible. The new stdout need not be byte-identical to historical stdout if version/format differs; compare semantics, intervals and trusted source.

This finite experiment never by itself establishes infinite-dimensional RH-related positivity, the global theorem, RH or GRH. Published claims and each independent execution receipt must be version- and source-pinned.

## Independent review and corrections

This is a fixed-source reproduction recipe, not a certification that the numerical result has been replicated by third parties. Preserve the historical exit status and sign-margin evidence even if a later replay disagrees. Attribute any observed discrepancies to the exact runtime and input hashes, and retain failing evidence for independent scrutiny.
