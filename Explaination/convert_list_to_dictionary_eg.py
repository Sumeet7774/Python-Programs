# Converting list into dictionary

sports = ['Cricket',11,'Football',11,'Tennis',2,'Baseball',15]
length = len(sports)
dic = dict()


dic = {sports[i]:sports[i+1] for i in range(0,length,2)}

print(dic)










