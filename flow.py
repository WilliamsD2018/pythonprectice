print("this is great")
response = raw_input("how are you?")
if(response.lower() == "good"):
	print("totally great")
	print("agreed")
elif(response.lower() == "ok"):
	print("Okay, I understand")
elif(response.lower() == "bad"):
	print("...haaaalp")
else:
	print("what was that? I don't understnd what you said")








print('''answer the next question, I will tell you if you are correct
ARE YOU READY?''')
answer = raw_input("tell me")
if(answer.lower() == "yes"):
	print ("you passed the first question") 
else:
	print ("you suck")
