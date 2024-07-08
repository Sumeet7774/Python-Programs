#Food order confirm message using formatted string

name = input("Enter your name: ")
ld = input("Enter your landmark: ")
p_id = 7059
p_no = int(input("Enter your number: "))
food = input("Enter your food item: ")                 
amount = 500

                 
print("Please confirm your information given below: ")
print("\nSir %s your requested order having id %d has been received, Please check the below information: \nFood name is %s,\nAmount is %d,\nPhone number is %d, \nLandmark is %s, \nTo confirm your order press 1 and To cancel press 0" %(name,p_id,food,amount,p_no,ld))

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Your order is confirmed")
    print("Food name is : ",food,"\nLandmark is: ",ld,"\nPhone number is: ",p_no,"\nAmount is: ",amount,"\nOrder id is: ",p_id, "\nYour order has been successfully placed." )
else :
    print("Your order is cancelled")    
