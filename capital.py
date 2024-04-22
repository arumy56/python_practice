
letter=input("enter your word or letter: ")
if not letter.isalpha():
    print("Invalid Input. enter a string which is either word or letter: ")
    
else:
 option=input("choose the operation you want:\n"
             "A:Capitalize the word/letters\n"
             "B:Lower Case \n"
             "operation: ")

 if option.upper()=="A":
    print(letter.upper())
 elif option.upper()=="B":
    print(letter.lower())
 else:
    print("Wrong operation. Choose either A or B from the operations above: ")