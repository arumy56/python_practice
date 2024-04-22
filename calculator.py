# print("heloo, hehe")

while True:
   number_uno= input("enter a number : ")
   number_dos= input("enter second numero: ")


   operation = input("choose an operation for the calculator: \n"
                    "A FOR ADDITION:\n"
                    "B FOR SUBTRACTION:\n"  
                    "C FOR MULTPLICATION: \n"
                     "D FOR DIVISION\n"
                     "Operation:  ")
 
   try:
     num1= int(number_uno)
     num2=int(number_dos)

   except ValueError:
     try:
       num1=float(number_uno)
       num2=float(number_dos)

     except ValueError:
        print("enter a valid number please")
        continue
 
   if operation.upper()=="A" or operation.lower()=="a":
     add=num1+num2
     print("the addition is: ", add)

   elif operation.upper()=="B" or operation.lower()=="b":
     sub=num1 -num2
     print("the substraction is: ", sub)

   elif operation.upper()=="C" or operation.lower()=="c":
     multi=num1*num2
     print("the multiplication: ", multi)

   elif operation.upper()=="D":
     if num2 == 0:
        print("a number cannot be divisible by zero. enter another number")
     else:
      
      div= num1 / num2
      print("the divison is: ", div)

   else:
      print("wrong operation. choose from operations indicated by the letters above")

   retry=input("if you want to continue with the calculator press (y) if not press (n): ")
   if retry.lower()!="y":
     break
   

  
print("thank you for using me, see you next time")



 
