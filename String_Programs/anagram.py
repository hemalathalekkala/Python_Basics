

str1=input()
str2=input()
if len(str1)!=len(str2):
    print("Not Anagram")
else:
    if sorted(str1)==sorted(str2):
        print("Anagram")
    else:
        print("Not Anagram")
