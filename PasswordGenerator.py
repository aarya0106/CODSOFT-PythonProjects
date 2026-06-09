import string
import random
s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation

plen = int(input("Enter Password Length: \n "))
s= list(s1+s2+s3+s4)
random.shuffle(s)
print("Your Password is:\n")
print("".join(s[0:plen]))