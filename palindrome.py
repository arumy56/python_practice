import re
input_strng= input("Enter a string to see if it is a Palindrome or Not: ")

# input_strng=input_strng.replace(" ", "").lower()
clean_strng= re.sub(r'[\W_]+', '', input_strng).lower()

if clean_strng==clean_strng[::-1]:
    print(f"the string: '{input_strng}' is a valid palindrom: ", clean_strng)
else:
    print("it is not a palindrome")    



