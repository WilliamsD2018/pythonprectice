
s=raw_input("Pease enter a word-")
upper_s = s.upper()
print(upper_s)
lower_s = s.lower()
print(lower_s)

combined = upper_s + lower_s

print(combined)

num_s = len(s)
print(num_s)
num_combined =len(combined)
print(num_combined)


halfway = len(s)/2
print(s[halfway])
print(s[0])
print("at s[0]")
print(s[0])
last = len(s) - 1
print(s[last])
print(s[-1])


firsthalf = s[:halfway]
lasthalf = s[halfway:last+1]
print("This is a test write")
print(firsthalf)
print(lasthalf)


copy = s[:]
skip = s[1::2]
print(skip)

#slice
#start,stop,increment

#concat

print(s.count("l"))
print(s.find("e"))
print(s[:s.find("e")])



#s.replase("o","0")
replaced = s.replace("great","awsome")

#value = s[len(s):halfway:-1]
#print(value)
words = s.split()
numberofwords = len(words)
print(words[0:2])
print(words[0:2:-1])
print(words[::-1])

sentence = " ".join(words)
print(sentence)

newsentence = sentence.replace("\n",":-)")
print(newsentence)
#slice
#start,stop,increment

#concat
