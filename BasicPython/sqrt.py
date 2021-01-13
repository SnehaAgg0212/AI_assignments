#Write a python program to find the square root of a given number (n) within a given precision (p). 
# Do not use any predefined library. (Take a guess, compute error at each successive step, 
# until error is less than given precision) Example values of n are 10,15, 45, etc. 
# Example values of p are 0.1, 0.05, 0.01, etc

n = int(input("Enter the number: "))
p = float(input("Enter the precision: "))
dec = 0
q = p
while q<1:
    q*=10
    dec+= 1
num = 0
for i in range(n):
    if(i*i)> n:
        num = i-1
        break

while num != n:
    newNum = num + p
    error = n - (newNum * newNum)
    if error < p:
        break
    else:
        num = newNum

print("Answer: ", round(newNum,dec))




