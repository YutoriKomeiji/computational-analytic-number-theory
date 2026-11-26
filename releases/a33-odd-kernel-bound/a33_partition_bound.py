from fractions import Fraction as Q

def atan_interval(x,n=64):
    assert 0<x<1 and n%2==0
    s=sum(((-1)**k*x**(2*k+1)/(2*k+1) for k in range(n)),Q(0))
    return s,s+x**(2*n+1)/(2*n+1)

def log_interval(x,n=64):
    assert x>0
    if x<1:
        a,b=log_interval(1/x,n)
        return -b,-a
    t=(x-1)/(x+1)
    s=2*sum((t**(2*k+1)/(2*k+1) for k in range(n)),Q(0))
    return s,s+2*t**(2*n+1)/((2*n+1)*(1-t*t))

def root_bracket(k,n,D=10**12):
    target=7**k*D**(2*n)
    lo,hi=D,3*D
    assert lo**(2*n)<=target<hi**(2*n)
    while hi-lo>1:
        mid=(lo+hi)//2
        if mid**(2*n)<=target: lo=mid
        else: hi=mid
    assert lo**(2*n)<=target<hi**(2*n)
    return Q(lo,D),Q(hi,D)

a,b=atan_interval(Q(1,5));c,d=atan_interval(Q(1,239))
pi_lo,pi_hi=16*a-4*d,16*b-4*c
L_lo,L_hi=log_interval(Q(7))
n=16
B=[Q(0)]
for k in range(1,n+1):
    z_lo,z_hi=L_lo*k/n,L_hi*k/n
    u_lo,u_hi=root_bracket(k,n)
    x_hi=z_hi*(u_lo+1)/(4*(u_lo-1))
    B.append(z_hi/2+log_interval(x_hi)[1]+2*atan_interval(1/u_lo)[1]-pi_lo/2)
# Each subinterval s in [i L/n,(i+1)L/n] has L-s <= (n-i)L/n.
# Nonnegativity of d implies monotonicity of beta=2 integral(d).
U=[(B[i+1]+B[n-i])/2 for i in range(n)]
assert max(U)<Q(101,1000)
print('PASS: all 16 row/column envelopes < 101/1000')
print('Diagnostic largest upper endpoint:', float(max(U)))
