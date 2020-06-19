import random

print('Gacha Box')

# Item inside Gacha Box 
# User will get item by using random function
gacha_item = ['Sword', 'Shield', 'Bow & Arrow', 'Axe', 'Staff', 'Dagger', 'Mace', 'Crossbow & Arrow', 'Whip', '100 Gold']


# User bought a gacha box for
# chance to get limited item 
gacha_box = int(input("How many Gacha Box thath you want to buy :  "))

# Number of chances to be given to 
# user to Open Gacha Box are same with
# Number of box that has already 
# bought by user 
chance = 0

# System will ask user to open the box 
Open_GBox = input("Open the Box(yes/no) : ")

# Compare the user entered answer
# by using if/else function 
if(Open_GBox == "y"):
    while chance < gacha_box:
        # random choice function to generate 
        # random item between "Sword" to "100 Gold"
        item_gacha = random.choice(gacha_item)
        print(item_gacha)
        chance += 1
else:
    print("Exit Dialog Box!")
