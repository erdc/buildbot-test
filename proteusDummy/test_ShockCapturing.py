from ShockCapturing import *
    
def testDummmy():
    class C:
        def __init__(self):
            self.nc = 1
    cd = ConstantDiffusion_SC(coefficients=C(),nd=3,shockCapturingFactor=0.25,lag=True)
    print "hello test"
    assert(True)

def testDummmy2():
    class C:
        def __init__(self):
            self.nc = 1
    cd = ConstantDiffusion_SC(coefficients=C(),nd=3,shockCapturingFactor=0.25,lag=True)
    print "hello test"
    assert(True)

def testDummmy3():
    class C:
        def __init__(self):
            self.nc = 1
    cd = ConstantDiffusion_SC(coefficients=C(),nd=3,shockCapturingFactor=0.25,lag=True)
    print "hello test"
    assert(True)
