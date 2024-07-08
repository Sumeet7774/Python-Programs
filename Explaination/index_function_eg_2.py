# to enter your hobby and character and check if both are present in list or not 

hobby = ['Football','Cricket','Basketball','Swimming','Music']

print(hobby)

a = input('Select your hobbies from above: ')
b = input('Select character from your hobby: ')


print('Your hobby is ',hobby.index(a),'is found in list')
print('Your character is present in hobby is at index: ',a.index(b))
