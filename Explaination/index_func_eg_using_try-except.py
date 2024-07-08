# to enter your hobby and character and check if both are present in list or not using try except

hobby = ['Football','Cricket','Basketball','Swimming','Music']

print(hobby)

a = input('Select your hobbies from above: ')
b = input('Select character from your hobby: ')

#if the hobby is found it will run the try block 
try :
    print('Your hobby is ',hobby.index(a),'found in list')  
    print('Your character is present in hobby: ',a.index(b))
   
#if the hobby is not found it will execute further
except ValueError:
    print('Your hobby is not found in the list')    
    


# if error will occur in try block then it will jump to except block and it will further execute it
# if error doesnt occurs then try block will be successfully be executed. And except block wont be executed.
# try block ma jya thi error aavse tya thi sidhu te except block ma jump thay jase execute thava mate
