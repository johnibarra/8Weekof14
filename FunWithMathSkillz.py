# we are going to look at approximations of Pi
# as well as looking at the math Module

print(22/7)
print(355/113)

import math

print(9801 / (2206 * math.sqrt(2)))

def archimedes(numSides):
    innerAngelB = 360.0 / numSides













print(archimedes(4))
print(archimedes(8))
print(archimedes(16))


for sides in range(8, 10, 8):
    print(sides, archimedes(sides))

# see the loop above. in addition to the value of pi, print he difference
# between the values calculated by the archimedes function and by math.pi.


