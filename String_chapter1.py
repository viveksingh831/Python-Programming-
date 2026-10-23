from operator import le


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

print("islower_&_isupper:-string topic \n")
print("islower:- check every latter is lower ")
text=input("enter the string:-")
print(text.islower(),"\n")
print("isupper:-check every latter is capital")
text=input("enter the string:-")
print(text.isupper())


print("title and istitle topic:-")
print("title:-do every word first latter captial\n")
text=input("enter the string:-")
print(text.title(),"\n")
print("istitle:- check every word first latter capital")
text=input("enter the string:")
print(text.istitle())
print(text.title(),"\n")

print("isspace:- check string is space or not")
text=input("enter the string:-")
print(text.isspace())
print("Because:- string=empty or space then True otherwise False\n")


print("starting and ending word checker:-......")
text=input("enter the string:-")
word=input("enter the word that you want to search:-")
print("Starting word=:-", text.startswith(word))
print("Ending word:- ",text.endswith(word),"\n")


print("\n string checker_&_Number checker_&_Number and string checker(not allow space and special character):-")
text=input("enter the text or sentence:-")
print("string:- ",text.isalpha())
print("Digit:- ",text.isdigit())
print("string and dight:- ",text.isalnum(),"\n")

print("isprintable Topic:- ")
text=input("enter the string")
print(text.isprintable())
print("text:-vivek\nkumar\nsingh")
print("vivek\nkumar\nsingh".isprintable())
print("because:-text is not simple text its include next line ")









