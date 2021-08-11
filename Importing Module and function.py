'''
import math
#print(dir(math))

print(math.sqrt(16))
print(math.pi)
print(math.floor(3.9))
print(math.ceil(3.9))
print(math.pow(3,2))
print(math.e)

# Using Alias for Module
import math as m
print(m.sqrt(25))
print(m.pi)

import math as m
print(m.sqrt(25)) 
print(m.pi)
print(math.floor(3.9)) # Gives Name error for math module

# Import functions directly from Module
from math import sqrt
print(sqrt(25))
print(pi) # NameError: name 'pi' is not defined

# Solution for Error 
# 1st solution
from math import sqrt,pi
print(sqrt(36))
print(pi)

# 2nd Solution
from math import *
print(sqrt(36))
print(pi)

from math import sqrt as s
print(s(25))

from math import sqrt as s, pi as p
print(s(36))
print(p)
'''


