# spam filtes for the given key words 

p1 = "make alot of money"
p2 = "buy know"
p3 = "subcribe this"
p4 = "click this link"

messege = input("please Enter the messege here : ")

if((p1 in messege) or (p2 in messege) or (p3 in messege) or (p4 in messege)):
    print("this is a spame")
else:
    print("this is not a spame")  