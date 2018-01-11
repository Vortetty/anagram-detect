x = input("what would you like to check for anagrams")
y = x[::-1]
 if y == x:
	print("you have an anagram on your hands")
elif y!=x:
	print("sorry, no anagram here")
else:
	print("woops, looks like somthing broke, please try again later or reload the page")
	
print("\nmade by vortetty for mohan")
