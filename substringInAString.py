

#defining a function

def SubstringInAString(string_s1, Substring_s2):
    if Substring_s2 in string_s1:
        return "Substring exists"
    else:
        return "Substring doesn't exists"


#Taking input from user.
string_s1=input("Enter the string : ")
Substring_s2=input("Enter a substring : ")

print(SubstringInAString(string_s1, Substring_s2))











