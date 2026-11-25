from fractions import Fraction as Q
from math import isqrt

def atan_interval(x, n=32):
    assert 0 < x < 1 and n % 2 == 0
    s = sum(((-1)**k*x**(2*k+1)/(2*k+1) for k in range(n)), Q(0))
    return s, s+x**(2*n+1)/(2*n+1)

def log_interval(x, n=64):
    assert x > 0
    if x < 1:
        a,b = log_interval(1/x,n)
        return -b,-a
    t = (x-1)/(x+1)
    s = 2*sum((t**(2*k+1)/(2*k+1) for k in range(n)), Q(0))
    return s, s+2*t**(2*n+1)/((2*n+1)*(1-t*t))

a,b = atan_interval(Q(1,5)); c,d = atan_interval(Q(1,239))
pi_lo,pi_hi = 16*a-4*d,16*b-4*c
L_lo,L_hi = log_interval(Q(7))
D = 10**12

def beta_interval(z_lo,z_hi,u_lo,u_hi):
    assert 0 < z_lo <= z_hi and 1 < u_lo <= u_hi
    x_lo = z_lo*(u_hi+1)/(4*(u_hi-1))
    x_hi = z_hi*(u_lo+1)/(4*(u_lo-1))
    lo = z_lo/2+log_interval(x_lo)[0]+2*atan_interval(1/u_hi)[0]-pi_hi/2
    hi = z_hi/2+log_interval(x_hi)[1]+2*atan_interval(1/u_lo)[1]-pi_lo/2
    return lo,hi

s = isqrt(7*D**2)
u_lo,u_hi = Q(s,D),Q(s+1,D)
assert u_lo**2 < 7 < u_hi**2
b_lo,b_hi = beta_interval(L_lo,L_hi,u_lo,u_hi)
assert Q(19969390622,10**11) < b_lo <= b_hi < Q(19969390624,10**11)
s = isqrt(isqrt(7*D**4))
u_lo,u_hi = Q(s,D),Q(s+1,D)
assert u_lo**4 < 7 < u_hi**4
h_lo,h_hi = beta_interval(L_lo/2,L_hi/2,u_lo,u_hi)
assert Q(3757957692,10**11) < h_lo <= h_hi < Q(3757957693,10**11)
assert (b_hi+h_hi)/2 < Q(119,1000)
print('PASS: beta(L) and beta(L/2) exact rational enclosures; combined bound < 119/1000')
