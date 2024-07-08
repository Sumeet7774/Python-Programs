#to enter your hobby and character and check if both are present in list or not using try except

language = ['c','c++','java','python','ruby','react']

print(language)

a = input('Enter your programming language from list: ')
b = input('Enter character of your programming language: ')


# a1 = language.index(a)
# b1 = a.index(b)
# print('value is ',language[a1],' & index is',a1)

# print('value is ',language[a1][b1],' & index is',a1,b1)


try :
    a1 = language.index(a) # a1 index of language list will be 5 if entered react
    b1 = a.index(b) # b1 index of language character will be 2 if entered a from react
    print('Your programming language is (',language[a1],') found in list')
    print('Your character of language is (',language[a1][b1],') found in list')
    print('After your entered character language is: ',language[a1][b1:]) #here a1 will be the index of our language and b1: will print the characters from which we will tell in b
    print('Displaying languages after (',a,') are: ',language[a1:]) #it will display all the languages after the input given in a. for eg if we give input c++ then it will print all languages from c++
    
except (ValueError, IndexError) :
    print('')
    print('Your programming language is not found in the list')
    
    
