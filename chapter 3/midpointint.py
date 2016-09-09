"""
Exercise 3.7: Derive the general Midpoint integration rule
Author: Weiyun Lu
"""

from scipy.integrate import quad
from scipy import sin, cos, pi

def midpointint(f,a,b,n):
    i = 0 #initialize counter
    h = (float(b) - float(a)) / n #set rectangle width
    s = 0 #initialize sum
    while i < n:
        m = a + (i + 0.5) * h
        s += f(m)
        i += 1
    s *= h
    return s

f0 = [cos, 0, pi]
f1 = [sin, 0, pi]
f2 = [sin, 0, pi/2]

def verify(f,a,b,n):
    exact = quad(f,a,b)[0]
    trapa = midpointint(f,a,b,n)
    error = abs(exact - trapa)
    print 'The exact value of the integral of %s from %.6f to %.6f is %.6f.' \
     %(f.__name__, a, b, exact)
    print 'The midpoint approximation with n=%d yields %.6f.' %(n, trapa)
    print 'The error is %.6f.' %(error)
    
functions = [f0, f1, f2]

for F in functions:
    verify(F[0],F[1],F[2],10)