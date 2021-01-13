#Write a python program that takes a sentence as input from the user and reverses the words in the sentence. 
# Eg. If the sentence is 'Welcome to AI lab', then the output should be 'lab AI to Welcome'. 
# (Use list and string data structures) 

sent = input("""Enter the sentence:
""")
a = []
word = ""
for i in range(len(sent)):
    if sent[i] == ' ':
        a.append(word)
        word = ""
    else:
        word = word + sent[i]

a.append(word)

newSent = ""
for i in reversed(range(1,len(a))):
    newSent = newSent + a[i]+ " "

newSent = newSent + a[0]
print("""The reversed sentence is:
""", newSent)





