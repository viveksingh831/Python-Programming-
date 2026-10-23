print()
line=" index and rindex:- topic "
print(line.upper().center(50,"*"))
text=input("enter the string:-")
word=input("enter the word to find:-")
print("index:-",text.index(word))
print("rindex:-",text.rindex(word))

line=" find and rfind:- topic "
print(line.upper().center(50,"*"))
text=input("enter the string:-")
word = input("enter the word to find:-")
print("find:-",text.find(word))
print("rfind:-",text.rfind(word))

line=" center and ljust and rjust:-topic "
print(line.upper().center(50,"*"))
text=input("enter the string:-")
print(text.center(50))
print(text.center(50,"*"))
print(text.ljust(50))
print(text.ljust(50,"*"))
print(text.rjust(50))
print(text.rjust(50,"*"))

line=" zfill:-topic "
print(line.center(50,"*"))
n=input("enter the number:-")
o=int(input("enter the number to fill:-"))
print("zfill:-",n.zfill(o))

line=" removeprefix and removesuffix:- topic"
print(line.center(50,"*"))
text=input("enter the string:- ")
word=input("enter the beginning word that you want to remove:- ")
print(text.removeprefix(word))
print("note:-removeprefix remove beginning word mean first word")
word=input("enter the ending word that you want to remove:-")
print(text.removesuffix(word))
print("note:-removesuffix remove ending word")


line=" split and splitlines:- topic "
print(line.center(50,"*"))
text=input("enter the string:-")
print("split:-",text.split())
print(len(text.split()))
print("note:- split brack every word accourding to space")
text="vivek\nkumar\nsingh"
print("splitlines:-",text.splitlines())
print("note:- splitlines break the string according to line breaks")
print(len(text.splitlines()))