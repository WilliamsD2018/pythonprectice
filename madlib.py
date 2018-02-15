story = "{0} is {1} down the road,{0} is using a {5} {2}"
name = raw_input("enter a name ")
verb = raw_input("enter a verb ")
noun = raw_input("enter a noun ")
name2 =raw_input("enter another name ")
verb2 = raw_input("enter another verb ")
adjetive = raw_input("enter an adjetive ")
adjusted = story.format(name, verb, noun, name2, verb2, adjetive)
print (adjusted)
