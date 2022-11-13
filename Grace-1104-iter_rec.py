'''
funtion iterativePower
    if the exponent is 0
        return 1
    else
        start, which is the original base, will equal to the changed base
        loop in range of exponent 
            base times the starting base
        return base
'''

start = 0

def iterativePower(base, exp):
    '''
    base: int or float
    exp: int >= 0
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        start = base
        for i in range(exp-1):
            base *= start
        return base

print (iterativePower(2, 5))

'''
function recursivePower
    if exponent is 0
        return 1
    else
        return base times the output of the function itself
'''

def recursivePower(base, exp):
    '''
    base: int or float
    exp: int >= 0
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        return base * recursivePower(base, exp - 1)

print (recursivePower(2, 6))