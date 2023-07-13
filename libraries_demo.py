import math
import random as ran
# only importing the pow function from the math library
from math import pow

result_1 = pow(2, 4)
print("result_1 is ", result_1)

result_2 = math.sqrt(16)
print("result_2 is ", result_2)

result_3 = ran.randint(1, 10)
print("result_3 is ", result_3)

names = ["Kass", "Ben", "Darien"]
print("original name: ", names)

ran.shuffle(names)
print("names after shufffling: ", names)

result_4 = ran.choice(names)
print("result name is: ", result_4)