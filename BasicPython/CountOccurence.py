#Write a python program that reads text from an input file (use your own input text file, it should contain at least 5-6 small sentences) 
# and counts the number of times each alphabet is appearing in it, 
# and displays the frequency of the occurrence of each alphabet. (Use dictionary data-structure to solve it)

f = open("/Users/anirudhagupta/Desktop/file.txt")
s = f.read()
dict = {}
for i in range(len(s)):
    if ord(s[i]) in range(97, 123) or ord(s[i]) in range(65,91):
        if s[i] in dict.keys():
            dict[s[i]] = dict[s[i]] + 1

        else:
            dict[s[i]] = 1


for i in sorted(dict):
    print("occurence of ", i, "is: ", dict[i])




