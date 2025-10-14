'''
Write a program that that allows people to add, drop, and change classes in a mod.

Then, build a larger program around it that builds the schedule for a whole year.
'''

d_block = {
    "Fall": "",
    "Winter": "",
    "Spring": ""
}

mod1 = {
    "A Block": "",
    "B Block": "",
    "C Block": "",
    "D Block": "",
    "E Block": ""
}

mod2 = {
    "A Block": "",
    "B Block": "",
    "C Block": "",
    "D Block": "",
    "E Block": ""
}

mod3 = {
    "A Block": "",
    "B Block": "",
    "C Block": "",
    "D Block": "",
    "E Block": ""
}

mod4 = {
    "A Block": "",
    "B Block": "",
    "C Block": "",
    "D Block": "",
    "E Block": ""
}

mod5 = {
    "A Block": "",
    "B Block": "",
    "C Block": "",
    "D Block": "",
    "E Block": ""
}

mod6 = {
    "A Block": "",
    "B Block": "",
    "C Block": "",
    "D Block": "",
    "E Block": ""
}

mod7 = {
    "A Block": "",
    "B Block": "",
    "C Block": "",
    "D Block": "",
    "E Block": ""
}

year = {
    "Mod 1": mod1,
    "Mod 2": mod2,
    "Mod 3": mod3,
    "Mod 4": mod4,
    "Mod 5": mod5,
    "Mod 6": mod6,
    "Mod 7": mod7
    }

#sets the initial value of fall, winter, and spring d blocks
def set_dblocks():
    #global variables can be seen but not touched by every function
    #to be able to edit global variables inside of functions, use the global keyword
    global d_block, mod1, mod2, mod3, mod4, mod5, mod6, mod7
    seasons = ["Fall","Winter","Spring"]
    for season in seasons:
        d_block[season] = input(f"What is your {season} season D Block? ")
    mod1["D Block"] = d_block["Fall"]
    mod2["D Block"] = d_block["Fall"]
    mod3["D Block"] = d_block["Winter"]
    mod4["D Block"] = d_block["Winter"]
    mod5["D Block"] = d_block["Winter"]
    mod6["D Block"] = d_block["Spring"]
    mod7["D Block"] = d_block["Spring"]

#schedule is a dictionary that represents one mod of classes
#it has a key for each block including D and E blocks
def add_change_class(schedule):
    valid_options = schedule.keys() #generates a list of the keys in my dict, in this case the block names
    print("Please pick:")
    for choice in valid_options:
        print(f"- {choice}")
    block = input("Which block? ").title() #all my keys are written in title case

    while block not in valid_options: #error handling
        print("Error. Please pick:")
        for choice in valid_options:
            print(f"- {choice}")
        block = input("Which block? ").title()

    new_class = input("What class do you want to take? ")
    schedule[block] = new_class #the same command gets used for adding and changing info
    print(f"You have added {schedule[block]}") #direct addressing confirmation
    print(f"New schedule: {schedule}") #check local copy of schedule
    return schedule #update in the main code

#this is basically the same function as above except instead of adding a new class
#it resets the value at the given key to an empty string to "drop" a class
def drop_class(schedule):
    valid_options = schedule.keys() #same as add_change function
    print("Please pick:")
    for choice in valid_options:
        print(f"- {choice}")
    block = input("Which block? ").title()

    while block not in valid_options: #error handling
        print("Error. Please pick:")
        for choice in valid_options:
            print(f"- {choice}")
        block = input("Which block? ").title()
    
    print(f"You have dropped {schedule[block]}") #direct addressing confirmation
    schedule[block] = "" #clearing the info without removing the key from the dict
    print(f"New schedule: {schedule}") #check local copy
    return schedule #update in main code

#this is for editing individual blocks within individual mods
#changes made to d blocks only reflect that specific mod, not the whole season
def make_a_mod(mod):
    valid_actions = ["add","change","drop","exit"]
    for choice in valid_actions:
        print(f"- {choice}")
    user_choice = input("What would you like to do? ").lower()
    
    while user_choice not in valid_actions:
        print("Error. Please pick:")
        for choice in valid_actions:
            print(f"- {choice}")
        user_choice = input("What would you like to do? ").lower()
    
    while user_choice != "exit":

        if user_choice in ["add","change"]:
            mod = add_change_class(mod)
        else:
            mod = drop_class(mod)

        print("Change successful.")

        for choice in valid_actions:
            print(f"- {choice}")
        user_choice = input("Anything else? ").lower()

        while user_choice not in valid_actions:
            print("Error. Please pick:")
            for choice in valid_actions:
                print(f"- {choice}")
            user_choice = input("Anything else? ").lower()

    return mod

#prints every key-value pair in a given mod dictionary
def see_a_mod(mod):
    print(f"{mod}: ")
    for block in mod:
        print(f"{block}: {mod[block]}")

#prints every key-value pair in the year global variable
def see_a_year():
    for mod in year:
        print(f"{mod}: ")
        for block in year[mod]:
            print(f"   {block}: {year[mod][block]}")

def main():
    global mod1, mod2, mod3, mod4, mod5, mod6, mod7
    running = True
    print("Welcome to Mrs. Carroll's office.")
    while running:

        #error handling for first input
        first_options = ["view","edit","exit"]
        print("Please pick:")
        for choice in first_options:
            print(f"- {choice}")
        first_input = input("What would you like to do? ").lower()
        while first_input not in first_options:
            print("Error. Please pick:")
            for choice in first_options:
                print(f"- {choice}")
            first_input = input("What would you like to do? ").lower()
        
        #if they want to view the schedule without changing it
        if first_input == "view":

            #error handling for the view functionality
            view_options = ["mod","year"]
            view_input = input("Do you want to see the whole year or just one mod? ")
            while view_input not in view_options:
                print("Error. Please pick:")
                for choice in view_options:
                    print(f"- {choice}")
                    view_input = input("Do you want to see the whole year or just one mod? ")
            
            #displaying just one mod
            if view_input == "mod":
                mod_input = input("Which mod do you want to see? ").capitalize()
                mod_options = year.keys()
                while mod_input not in mod_options:
                    print("Error. Please pick:")
                    for choice in mod_options:
                        print(f"- {choice}")
                    mod_input = input("Which mod do you want to see? ").capitalize()
                #mod_input --> key from the user, which is then used to directly access the matching value in the "year" dict
                see_a_mod(year[mod_input])

            #displaying the whole year
            else:
                see_a_year()
            #so that the user knows why it repeats
            print("Returning to main menu...")

        #if they want to change the schedule
        elif first_input == "edit":
            edit_dblock_input = input("Do you want to edit a specific mod or your D Blocks? ").lower()
            edit_dblock_options = ["d block", "mod"]
            while edit_dblock_input not in edit_dblock_options:
                print("Error. Please pick:")
                for choice in edit_dblock_options:
                    print(f"- {choice}")
                edit_dblock_input = input("Do you want to edit a specific mod or your D Blocks? ").lower()
            if edit_dblock_input == "d block":
                set_dblocks()
            else:
                edit_mod_input = input("Which mod do you want to edit? ").capitalize()
                edit_mod_options = year.keys()
                while edit_mod_input not in edit_mod_options:
                    print("Error. Please pick:")
                    for choice in edit_mod_options:
                        print(f"- {choice}")
                    edit_mod_input = input("Which mod do you want to edit? ").capitalize()
                year[edit_mod_input] = make_a_mod(year[edit_mod_input])

        #thanks to error handling, we know that by here they've said exit
        else:
            running = False
    print("Thanks for stopping by!")

main()
