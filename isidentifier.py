print("isidentifier:-check string is valid only allow first latter then number\nor only string and also allow underscore")
print("text:-vivek")
name="vivek"
print(name.isidentifier())
print("text:-vivek kumar")
text="vivek kumar"
print(text.isidentifier())
print("beacuse space is not allow")
print("text:-vivek123")
text="vivek123"
print(text.isprintable())
print("text:-123vivek")
text="123vivek"
print(text.isidentifier())
print("text:-vivek_singh")
text="vivek_singh"
print(text.isidentifier())