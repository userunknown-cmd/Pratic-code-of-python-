# student passing programm alteast 33 percent and 44% minimum

a1  = int(input("enter the passing numbers for first subject : "))
a2  = int(input("enter the passing numbers for second subject : "))
a3  = int(input("enter the passing numbers for third subject : "))

# if(a1>=33):
#     print("you have passed the subject ") 
# else:
#     print("you have to give this paper again")    
# if(a2>=33):
#     print("you have passed the subject ")
# else:
#     print("you have to give this paper again")    
# if(a3>=33):
#     print("you have passed the subject ")
# else:
#     print("you have to give this paper again")    

# total percentage >= 40 

total_percentage = (100*(a1 + a2 + a3)/300)
if(total_percentage>=40 and a1>=33 and a2>=33 and a3>=33):
    print("you have passed the examination",total_percentage)
else:
   print("you have failed the examination,Try next time",total_percentage)    

