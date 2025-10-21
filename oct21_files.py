my_schedule = open("schedule.txt")

#write a while loop that looks for "Mod 2"
#then write a for loop that prints out Mod 2 schedule

line = my_schedule.readline() #control variable for while loop

while line != "Mod: 2\n":
    line = my_schedule.readline() #advances cursor until we find Mod: 2

print(line) #print the Mod 2 label

for i in range(3): #now we are at the right place so
    print(my_schedule.readline()) #print the next 3 lines