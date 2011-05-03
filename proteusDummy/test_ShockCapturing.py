from ShockCapturing import *
    
def testDummmy():
    class C:
        def __init__(self):
            self.nc = 1
    cd = ConstantDiffusion_SC(coefficients=C(),nd=3,shockCapturingFactor=0.25,lag=True)
    print "hello test 1"
    assert(True)

def testDummmy2():
    class C:
        def __init__(self):
            self.nc = 1
    cd = ConstantDiffusion_SC(coefficients=C(),nd=3,shockCapturingFactor=0.25,lag=True)
    print "hello test 2"
    assert(False)#adding a failed test to see what happens

def testDummmy3():
    class C:
        def __init__(self):
            self.nc = 1
    cd = ConstantDiffusion_SC(coefficients=C(),nd=3,shockCapturingFactor=0.25,lag=True)
    print "hello test 3"
    assert(True)

def testDummmy4():
    class C:
        def __init__(self):
            self.nc = 1
    cd = ConstantDiffusion_SC(coefficients=C(),nd=3,shockCapturingFactor=0.25,lag=True)
    print "hello test 4"
    assert(True)

def testDummmy5():
    class C:
        def __init__(self):
            self.nc = 1
    cd = ConstantDiffusion_SC(coefficients=C(),nd=3,shockCapturingFactor=0.25,lag=True)
    print "hello test 5"
    assert(True)
