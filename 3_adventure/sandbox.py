# Bank Robbing Game
import random, sys
import polars as pl
import pyttsx3
engine = pyttsx3.init()

print("Hello! You must steal the crown jewels or else.")
jewels = random.randint(500000,90000000)
jewels
print(f"The crown jewels are worth £{jewels}")
print("You are at the enterance of the kings vault. There are 2 guards with big fuck off guns and they look a little nasty. There's also a large hound sleeping at their feet.")

backpack = {'item':'','quantity':0}
backpack
backpack = pl.DataFrame(backpack)
backpack

while True: 
    print("You go: (l)eft, (r)ight, (d)ig a hole, or (c)heck backpack or (q)uit but pls don't this is my first game just play it pls :()")
    user_input = input("-")
    user_input
    if user_input == 'q':
        print("Fuck you it hadn't even gotten to the good bit i'm crying now cheers")
        sys.exit()
    elif user_input == 'l':
        print("There is a small bunny, he whispers 'hey kid, stealing that old cunts jewels? banging. Take this shrinking potion and get through the crack in the wall.")
        print("(\__/)")
        print("(='.'=)")
        print("('')_(')") 
        print("Do you (t)ake or (l)eave the bunnies item?") 
        user_input = input("-")
        if user_input == 't':
            backpack = backpack.with_columns(pl.col('item') + 'shrinking potion')
            backpack = backpack.with_columns(pl.col('quantity') + 1)
            print(f"In your backpack, you have {backpack.select('quantity').item(0,'quantity')} {backpack.select('item').item(0,'item')}")
        continue
    elif user_input == 'r':
        print("You see the vault, the doors are made of thick metal and there's some scary looking laser beams ouchie. You hear a dalek screaming.")
        engine.setProperty('rate',125)
        engine.say('Take one step closer and we will blow your head off')
        engine.runAndWait()
        engine.stop() 
        continue
    elif user_input == 'd':
        print("You dig through the wet earth with your bare hands. You dig up a bone. Will you (t)ake or (l)eave the item?")
        user_input = input("-")
        if user_input == 't':
            backpack = backpack.with_columns(pl.col('item') + 'bone') 
            backpack = backpack.with_columns(pl.col('quantity') + 1)
            print(f"In your backpack, you have {backpack.select('quantity').item(0,'quantity')} {backpack.select('item').item(0,'item')}")
            

# engine.say('Take one step closer and we will blow your head off')
# engine.runAndWait()
# engine.stop()
# rate = engine.getProperty('rate')   # getting details of current speaking rate
# print (rate)                        #printing current voice rate
# engine.setProperty('rate', 125)     # setting up new voice rate
 

