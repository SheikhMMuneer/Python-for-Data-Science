import numpy as np
from numpy.random import randn


# If Statement
answer = None
x = randn()
if x > 1:
    answer = "Greater than 1"
else:
    answer = "Less than 1"
print(x)
print(answer)


# Nested Statement
if x > 1:
    answer = "Greater than 1"
elif x >= -1:
        answer = "Between -1 and 1"
else:
        answer = "Less than -1"
print(x)
print(answer)

