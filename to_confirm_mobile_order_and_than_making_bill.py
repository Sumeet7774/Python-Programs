# to confirm mobile order and then making bill

mobile = ['Apple','Mi','Vivo','Samsung','Nokia']
print(mobile)

mobile_name = input('Enter the mobile name: ')
model_num = int(input('Enter the model number for your mobile: '))
model_name = input('Enter the model name for your mobile: ')
model_year = int(input('Enter the model year for your mobile: '))
model_price = int(input('Enter the price for your mobile: '))
model_spec = input('Enter the specs for your mobile: ')

print('')


try:
    x = mobile.index(mobile_name)
    print('The name of mobile is: ',mobile_name)
    print('The model number of your mobile is: ',model_num)
    print('The model of mobile is: ',model_name)
    print('The model year is: ',model_year)
    print('The price of your mobile is: ',model_price)
    print('The model specs are: ',model_spec)
   
    q = input('Do you want to confirm your order? Then Type Yes else No: ')
    
    if q == 'yes':
        print('Your order is successfully placed')
    else : 
        print('Your order is cancelled')
        
        
except ValueError:
    print('The mobile is not found in the list of mobiles')        
    
    
    
    
    