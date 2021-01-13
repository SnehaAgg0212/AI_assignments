#Create a suitable class in python to represent the mathematical concept of '1-D vector'
#(use list data structure to represent 1-D vector). 
# Create appropriate member variables and member functions of this class to perform operations:
#  Length of vector, Cosine similarity between two vectors, Euclidean distance between two vectors. 

import math
class Vect:
    def __init__(self, l):
            self.lt = l 

    def length(self):
        return len(self.lt)

    def compute_cosine(self, l):
        sumxx, sumxy, sumyy = 0, 0, 0
        for i in range(len(self.lt)):
            x = self.lt[i]
            y = l.lt[i]
            sumxx += x*x
            sumyy += y*y
            sumxy += x*y
        return sumxy/math.sqrt(sumxx*sumyy)

    def EuclideanDist(self, l):
        sumxy = 0 
        diffxy = 0
        for i in range(len(self.lt)):
            x = self.lt[i]
            y = l.lt[i]
            diffxy = x-y
            sumxy = sumxy + (diffxy ** 2)
        return math.sqrt(sumxy)


v1 = Vect([1,2,3,4])
v2 = Vect([3,4, 8, 10])
print (v1.length())
print (v1.compute_cosine(v2))
print (v2.EuclideanDist(v1))