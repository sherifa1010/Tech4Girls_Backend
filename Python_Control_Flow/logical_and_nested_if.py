#!/usr/bin/python

#is_student = True
#is_employed = False

#if is_student and is_employed:
  # print("you are a working student.")
#elif is_student and not is_employed:
 #   print("you are astudent.")
#elif not is_student and is_employed:
  #  print("you are employed but not astudent.")


age = int(input("please enter your age"))
if age >= 18:
   license = input("Do you have a driver's license? yes/no:")
   if license == 'yes':
       print("you are allowed to drive")
   else:
       print("You need a driver's license to drive.")
else:
    print("You are not old enough to drive.")

     
    
    
    
    



