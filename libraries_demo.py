import math
import random as ran
# only importing the pow function from the math library
from math import pow
from random import shuffle as sh

result_1 = pow(2, 4)
print("result_1 is ", result_1)

result_2 = math.sqrt(16)
print("result_2 is ", result_2)

result_3 = ran.randint(1, 10)
print("result_3 is ", result_3)

names = ["Kass", "Ben", "Darien"]
print("original name: ", names)

sh(names)
print("names after shufffling: ", names)

result_4 = ran.choice(names)
print("result name is: ", result_4)

import registry_system_class as rsc
course = rsc.Course("AI", 3, "Benedict", 25)
student = rsc.Student("Alice", 18, 12, course)
student.introduce_course()
course.introduce()

import numpy as np
import matplotlib.pyplot as plt
# fixing random state for reproducibility
np.random.seed(19680801)
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
# 0 to 15 point radii
area = (30 * np.random.rand(N))**2
plt.scatter(x, y, s=area, c=colors, alpha = 0.5)
plt.show()

# make sure to close to plot, otherwise the numpy code will not run
import numpy as np
A = [[3,5],
     [2,4]]
B = [[1,2],
     [3,4]]
C = np.add(A, B)
print("Element-wise sum of A and B is: ")
print(C)
D = np.subtract(A, B)
# \n means starting new line
print("\nElement-wise subtraction of A and B is: ")
print(D)
E = np.multiply(A, B)
print("\nElement-wise multiplication of A and B is: ")
print(E)
F = np.dot(A, B)
print("\nDot product of A and B is: ")
print(E)