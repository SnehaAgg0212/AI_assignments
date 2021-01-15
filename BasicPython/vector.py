#Create a suitable class in python to represent the mathematical concept of 'vector'
#(use list data structure to represent vector). 
# Create appropriate member variables and member functions of this class to perform operations:
#  Length of vector, Cosine similarity between two vectors, Euclidean distance between two vectors. 

import math
class Vect:
    def __init__(self, l):
            self.lt = l 

    def length(self):
        s = 0
        for i in range(len(self.lt)):
            s = s + (self.lt[i] ** 2)

        return math.sqrt(s)

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


print ("Enter the dimensions for the first vector")
l1 = [int(x) for x in input().split()]
print ("Enter the dimensions for the second vector")
l2 = [int(x) for x in input().split()]
if len(l1) != len(l2):
    print ("There is a mismatch in the dimensions of the two vectors, please try again")
else:
    v1 = Vect(l1)
    v2 = Vect(l2)
    print ("Length of the vector: ",v1.length())
    print ("Computing the cosine: ",v1.compute_cosine(v2))
    print ("Computing the Euclidean distance: ",v2.EuclideanDist(v1))
