#!/usr/bin/env python3
# DAN-42 / Y7 O2 Direct-Gauss no-gamma shifted-inertia Arb witness
# RESEARCH_ONLY / NON_CANONICAL / NO_RH_PROOF_CLAIM
#
# EXTENDS prior no-gamma shifted-inertia asset by replacing ONLY the arithmetic
# translation assembly with the now-audited Direct Gauss-200 representation.
#
# Goal:
#   Certify inertia(M0 - 0.70 I) = (7,0,93) for the same correct -2 Y=7
#   100D odd-Legendre head with the regular gamma operator removed.
#
# If successful, combine with independent gamma norm bound
#   ||Gamma|| <= (1/4) log 7
# and the existing polar truncation debit to obtain a lower bound for the
# eighth eigenvalue of the full head.
#
# Fixed one-shot parameters:
#   Arb 512 bits, N=100, Gauss order 200, shift=0.70, m=2,3,4,5.
# No scans, retries, alternate witness search or post-run source patch.

from flint import arb, arb_mat, ctx
from math import factorial
import numpy as np
import json, time, sys, platform

ctx.prec = 512
T0 = time.time()

N = 100
QGAUSS = 200
SHIFT = arb(7)/10
A = arb(7).log()/2
C0 = -A.log()-(2*arb.pi()).log()-arb.const_euler()
DEG = [2*i+1 for i in range(N)]
NORMS = [(arb(2*n+1)/2).sqrt() for n in DEG]

def harmonic(n):
    return sum((arb(1)/k for k in range(1,n+1)), arb(0))

def eval_odd_vector(x):
    return [x.legendre_p(n) for n in DEG]

def direct_translation(d):
    h = 1-d
    M = arb_mat(N,N)
    node_max_radius = 0.0
    weight_max_radius = 0.0
    pointwise_max_radius = 0.0
    term_max_radius = 0.0

    for k in range(QGAUSS):
        x,w = arb.legendre_p_root(QGAUSS,k,weight=True)
        node_max_radius=max(node_max_radius,float(x.rad()))
        weight_max_radius=max(weight_max_radius,float(w.rad()))
        lv = eval_odd_vector(h*x-d)
        rv = eval_odd_vector(h*x+d)
        for v in lv:
            pointwise_max_radius=max(pointwise_max_radius,float(v.rad()))
        for v in rv:
            pointwise_max_radius=max(pointwise_max_radius,float(v.rad()))
        for i in range(N):
            li=lv[i]
            for j in range(N):
                term=w*li*rv[j]
                term_max_radius=max(term_max_radius,float(term.rad()))
                M[i,j] += term

    max_radius = 0.0
    worst = None
    for i in range(N):
        for j in range(N):
            M[i,j] = h*NORMS[i]*NORMS[j]*M[i,j]
            r=float(M[i,j].rad())
            if r > max_radius:
                max_radius=r
                worst={"i":i,"j":j,"degrees":[DEG[i],DEG[j]],
                       "entry":str(M[i,j])}
    return M,{
        "d":str(d),
        "h":str(h),
        "node_max_radius":node_max_radius,
        "weight_max_radius":weight_max_radius,
        "pointwise_legendre_max_radius":pointwise_max_radius,
        "weighted_term_max_radius":term_max_radius,
        "matrix_max_radius":max_radius,
        "matrix_worst_entry":worst,
    }

# endpoint potential
V=arb_mat(N,N)
for i,n in enumerate(DEG):
    for j in range(i,N):
        m=DEG[j]
        if n!=m:
            val=2*NORMS[i]*NORMS[j]/(abs(n-m)*(n+m+1))
        else:
            ss=sum((arb(1)/((2*k-1)*2*k*(2*k+1))
                    for k in range(1,n+1)),arb(0))
            val=1+2*ss-arb(2).log()
        V[i,j]=V[j,i]=val

# polar vector: unchanged source-exact truncated positive series + explicit tail
POLAR_STEPS=100
sv=[]
sv_tail=[]
t=A/2
for i,n in enumerate(DEG):
    term=(arb(2)**(n+1))*(t**n)*arb(factorial(n))/arb(factorial(2*n+1))
    sm=term
    for j in range(POLAR_STEPS):
        term *= t*t*(n+j+1)/((j+1)*(2*n+2*j+2)*(2*n+2*j+3))
        sm += term
    j=POLAR_STEPS
    rnext=t*t*(n+j+1)/((j+1)*(2*n+2*j+2)*(2*n+2*j+3))
    next_term=term*rnext
    tail=next_term/(1-rnext)
    sv.append(NORMS[i]*sm)
    sv_tail.append(NORMS[i]*tail)

# arithmetic translations: same source object, Direct Gauss-200 only
Ar=arb_mat(N,N)
assembly={}
for nn in (2,3,4,5):
    ell=arb(nn).log()
    lam=arb(2).log() if nn==4 else ell
    c=lam/arb(nn).sqrt()
    d=ell/arb(7).log()

    T,diag=direct_translation(d)
    assembly[str(nn)]=diag
    for i in range(N):
        for j in range(N):
            Ar[i,j] += (T[i,j]+T[j,i])*(-c)

# no-gamma center
M0=arb_mat(N,N)
for i in range(N):
    for j in range(N):
        M0[i,j]=V[i,j]+Ar[i,j]-2*A*sv[i]*sv[j]
        if i==j:
            M0[i,j]+=harmonic(DEG[i])+C0

# omitted polar vector debit: unchanged
sn2=arb(0); en2=arb(0)
for x in sv: sn2 += x*x
for e in sv_tail: en2 += e*e
sn=sn2.sqrt(); en=en2.sqrt()
delta_polar=2*A*(2*sn*en+en*en)

# midpoint witness proposal only
Mmid=np.empty((N,N),dtype=float)
for i in range(N):
    for j in range(N):
        Mmid[i,j]=float(M0[i,j].mid())
Mmid=(Mmid+Mmid.T)/2
w,Q=np.linalg.eigh(Mmid)

# Freeze the same witness format as prior runner: 18 decimal digits
Qd=np.vectorize(lambda x: float(f"{x:.18f}"))(Q)
Qa=arb_mat(N,N)
for i in range(N):
    for j in range(N):
        Qa[i,j]=arb(str(Qd[i,j]))

# Gershgorin proof of witness invertibility
Gram=Qa.transpose()*Qa
gram_margins=[]
gram_ok=True
for i in range(N):
    rad=arb(0)
    for j in range(N):
        if i!=j:
            rad += abs(Gram[i,j])
    margin=Gram[i,i]-rad
    gram_margins.append(margin)
    if not bool(margin>0):
        gram_ok=False

# shifted congruence
Hs=arb_mat(N,N)
for i in range(N):
    for j in range(N):
        Hs[i,j]=M0[i,j]
        if i==j:
            Hs[i,j]-=SHIFT

Tmat=Qa.transpose()*Hs*Qa
neg=[]; pos=[]; unresolved=[]
neg_margins=[]; pos_margins=[]
for i in range(N):
    rad=arb(0)
    for j in range(N):
        if i!=j:
            rad += abs(Tmat[i,j])
    di=Tmat[i,i]
    if bool(di+rad<0):
        neg.append(i); neg_margins.append(-(di+rad))
    elif bool(di-rad>0):
        pos.append(i); pos_margins.append(di-rad)
    else:
        unresolved.append(i)

inertia_ok = gram_ok and len(neg)==7 and len(pos)==93 and len(unresolved)==0

# independent gamma debit and target
gamma_upper=A/2  # log(7)/4
full_lambda8_lower=SHIFT-gamma_upper-delta_polar
target_ok=bool(full_lambda8_lower>arb(1)/5)
overall=inertia_ok and target_ok

res={
  "schema":"DAN42_Y7_O2_DIRECT_GAUSS_NOGAMMA_SHIFTED_INERTIA_ARB_V1",
  "boundary":"RESEARCH_ONLY / NON_CANONICAL / NO_RH_PROOF_CLAIM",
  "prec_bits":ctx.prec,
  "N":N,
  "gauss_order":QGAUSS,
  "gauss_exact_degree":2*QGAUSS-1,
  "max_integrand_degree":2*max(DEG),
  "shift":str(SHIFT),
  "assembly":assembly,
  "midpoint_lambda7":float(w[6]),
  "midpoint_lambda8":float(w[7]),
  "gram_invertible":gram_ok,
  "gram_min_margin":str(min(gram_margins,key=lambda z: float(z.mid()))),
  "negative_disc_count":len(neg),
  "positive_disc_count":len(pos),
  "unresolved_rows":unresolved,
  "negative_rows":neg,
  "positive_rows":pos,
  "min_negative_disc_margin":str(min(neg_margins,key=lambda z: float(z.mid()))) if neg_margins else None,
  "min_positive_disc_margin":str(min(pos_margins,key=lambda z: float(z.mid()))) if pos_margins else None,
  "inertia_7_0_93_certified":inertia_ok,
  "delta_polar_opnorm":str(delta_polar),
  "gamma_norm_upper":str(gamma_upper),
  "full_lambda8_lower_from_shift":str(full_lambda8_lower),
  "full_lambda8_gt_0p2":target_ok,
  "overall_pass":overall,
  "runtime_sec":time.time()-T0,
  "python_version":sys.version,
  "platform":platform.platform(),
  "proof_ceiling":"O2 no-gamma shifted-inertia candidate only; no O2/Y7/RH promotion without proof-graph integration audit"
}
print(json.dumps(res,indent=2))
raise SystemExit(0 if overall else 2)
