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

# Accumulators

acc = 0
for val in range(1, 6, 1):
    acc = acc + val

print(acc)

# compute the sum of the first 100 even numbers
# compute the sum of the first 50 odd numbers
# compute the average of the first 100 odd numbers
# write a function that returns the average of the first N numbers, where
#   N is a parameter
# write a function called a factorial that computes the product of the first N
#   numbers, where N is a parameter
# Each number in the fibonacci sequence is the sum of the previous two numbers,
#   The first two numbers in the sequence are 1 and 1. compute the 10th
#   Fibonacci number

# A Monto carlo simulation

# ramdom numbers

import random

print(random.random())

# boolean expressions
# <, <=, >, >=, ==, !=
# compound Boolean expressions
# and, or, not

dogWeight = 25
print(dogWeight >= 25)
catWeight = 12
print(dogWeight > 25 or catWeight <= 10)
print(not catWeight <= 10)

# Decision making skills

alice = 20
bob = 25
carol = 25
ans = 0
if alice > 20:
    if bob < 50:
        ans = 150
    else:
        ans = 300
else:
    if carol > 500:
        ans = 200
    else:
        ans = 75
print(ans)

value = 75
if value > 100:
    print("bigger than 100")
else:
    if value > 80:
        print("bigger than 80")
    else:
        if value > 45:
            print('bigger than 45')
        else:
            print("not bigger than much")

def MontePi(numDart):

    inCircle = 0

    for i in range(numDart):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2 + y**2)
        if distance <= 1:
            inCircle = inCircle + 1

            pi = inCircle / numDart * 4
            return pi

print(MontePi(10000))






















































































































































































































































































































