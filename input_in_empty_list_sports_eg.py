# Sports List example to take value from user in empty list 

sports = [[],[]]       


num = int(input('Enter your number: '))

for i in range(0,num):
    sport_type = input('Enter sport name: ')
    player = input('Enter player name: ')
    sports[0].append(sport_type)
    sports[1].append(player)
print(sports)
        





