print('spam eggs')
print("paris rabbit got your back :)! yap!")
print('"doesn\'t"')
print('\'"Yes," they said.\'')
print(''''"yes," they said.'             ''')
print(''''"Isn\'t," they said.' ''')
print('\'"Isn\'t," they said.\'')

print("split string")

def string(text):
	return text.split()

print(string("i love bhopal"))

print ("Replace String")
text="i love bihar"
print("original string:-",text)
print("after the replace")
print(text.replace("bihar","Bhopal"))
print("After the full string replace")
print(text.replace("i love bihar","I love myself"))

print("join string:- 2 string ko add krna:-")
words=input("Enter the string:-").split()

print(" ".join(words))
print("-".join(words))
print("@".join(words))
print("*".join(words))

print("topic find string:- string me index find krna")
text=input("enter the sentence:-")
word=input("enter the word to find:-")
print(text.find(word))

print("count string:- string ko count krta hai:")

text=input("enter the string:-")
word=input("enter the word to find count:-")

print(text.count(word))





