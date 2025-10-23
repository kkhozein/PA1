#my_schedule = open("schedule.txt") #by default opens in read mode, can open in write or append mode


#my_schedule = open("schedule.txt", "w") #write mode...
#my_schedule.write("Changing content!") #...overwrites all files contents.

my_schedule = open("schedule.txt", "a") #append mode...
my_schedule.write("\nLOOK AT THIS NEW CONTENT") #...adds to the end of the file contents.

'''
To create a new file in Python, just open one that doesn't exist in an edit mode or "x" mode.
'''

#new_file = open("new_file.txt","x") #just creates new file
#new_file.write("HI")

new_file = open("new_file.txt","a") #creates new file or adds if already exists
new_file.write("YO")

new_file.close()

new_file.write("Hello?")
"""
#write a while loop that looks for "Mod 2"
#then write a for loop that prints out Mod 2 schedule

line = my_schedule.readline() #control variable for while loop

while line != "Mod: 2\n":
    line = my_schedule.readline() #advances cursor until we find Mod: 2

print(line) #print the Mod 2 label

for i in range(3): #now we are at the right place so
    print(my_schedule.readline()) #print the next 3 lines"""

