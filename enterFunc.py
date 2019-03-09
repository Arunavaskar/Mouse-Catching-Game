def still_need_to_clean():
    print("It's still not clean enough to work on setting up traps!")
    while True:
        i = input("type 'clean' to clean room and proceed \n>>>...".title().lower())
        if i ==  "clean":
            print("Perfect! room is now clean enough to set up traps!")
            break
        else:
            print("Nope! you need to ")
            continue


def found_wallet(money):
    print("You found a Wallet".title())
    print(f"You found {money}R in it".title())
                            
    print("There is a kitchen and you can go to store outside to buy things with the money you found.".title())


def k_s(k, m, c):
    kitchen_store = k
    money = m
    cheeze_available = c
    print("how many cheeze would you like to buy?")
    print(f"each cheeze costs you 2R, you have {money}R.")
    cheeze_price = 2 #R
    cheeze_available = 0


    while True:
        cheeze = input("vaaxs>>>...")
        if cheeze.isdigit():    # if cheeze input is a digit
            cheeze_brought = int(cheeze) # convert that to int
            while True: # while loop always running
                if cheeze_brought <= 4 and cheeze_brought > 0:            # if cheeze brought is 4 or less
                    print(f"you just brought {cheeze_brought} cheezes.")
                    cheeze_available += cheeze_brought
                    money -= cheeze_price * cheeze_brought
                    print(f"Now you have {cheeze_available} cheezes")
                    print(f"{money}R in wallet.")
                    print("Now would you like to buy a 88R priced trap before leaving the store?")
                    trap_price = 88 #R
                    while True:
                        trap_yes_no = input(">>>...").lower() # cheeze brought 4 or less and asking for trap

                        if trap_yes_no == "yes": # cheeze brought 4 or less and buys a trap
                            money -= trap_price
                            print(f"you have {money}R in you wallet.")
                            print("would like to buy anything else of your choice?")
                            print("*Type the item you think could help you catch a mouse and check if it's available in the store or not!*")

                            item = input(">>>...").lower()

                            if item == "poison": # cheeze brought 4 or less and buys a trap and buys poison
                                print("Wow! you just brought poison for 5R")
                                print("CLick enter to setup the total trap in the room!")
                                input()
                                print("wow! you've got the mouse!")
                                print("You Win!")
                                exit()
                            else:
                                print("item not available!")
                                print("CLick enter to setup the total trap in the room!")
                                input()
                                print("wow! you've got the mouse!")
                                print("You Win")
                                exit()

                        elif trap_yes_no == "no":
                            print("You are a dumb fucking asshole. to catch a mouse you absolutely need to buy a trap.!!!!")
                            exit()
                        else:
                            print("You need to choose and type out the option down there and click enter to proceed!")

                elif cheeze_brought > 4: # cheeze brought more than 4
                    print("OOPS! store holder says that you they only have 4 cheezes to sell.")
                    print("Would you like to buy 4 cheezes?")
                    print("Type if yes to buy or no to check out Traps to buy.") # not happening more thn 4
                    while True:
                        yes_no = input(">>>...").lower() # if yes then buys 4 cheeze else no then checks out traps instead

                        if yes_no == "yes": # buyz 4 cheeze
                            cheeze_brought = 4 # assigns 4 to the variable means user brought 4 cheezes
                            break # break leads to quiting this current while loop and go back to the father of this loop. line 34
                        elif yes_no == "no": # says no and buyz no cheeze at all and checks out traps to buy
                            print("trap costs 88R, would you like to buy a trap?")
                            print("Type yes or no to continue")
                            while True:
                                trap_yes_no == input(">>>...")

                                if trap_yes_no == "yes": # if types yes . user buys a trap but no cheeze 
                                    money -= trap_price
                                    print(f"you have {money}R in you wallet.")
                                    print("would like to buy anything else of your choice?")
                                    print("*Type the item you think could help you catch a mouse and check if it's available in the store or not!*")

                                    item = input(">>>...").lower()

                                    if item == "poison": # here user buys poison as optional but no cheeze, have trap atleast
                                        print("Wow! you just brought poison for 5R")
                                        print("Now click enter to setup the trap to catch the mouse.")
                                        input()
                                        print("You are a dumb fucking asshole. to catch a mouse you absolutely need to get that mouse out of the hole. no cheeze no nothing!!!!")
                                        print("Game Over!")
                                        exit() # exits as its a game over
                                    else: # if users guess dosnt match with poison.
                                        print("item not available")
                                        print("Now click enter to setup the trap to catch the mouse.")
                                        input()
                                        print("You are a dumb fucking asshole. to catch a mouse you absolutely need to get that mouse out of the hole. no cheeze no nothing!!!!")
                                        print("Game Over!")
                                        exit() # these lines runs and exits

                                elif trap_yes_no == "no": # here user chooses to buy no traps even.. so no traps and no cheese
                                    print(f"you have {money}R in you wallet.")
                                    print("would like to buy anything else of your choice?")
                                    print("*Type the item you think could help you catch a mouse and check if it's available in the store or not!*")

                                    item = input(">>>...").lower()

                                    if item == "poison": # if users choice matches to poison these lines runs and exits
                                        print("Wow! you just brought poison for 5R")
                                        print("Now click enter to setup the trap to catch the mouse.")
                                        input()
                                        print("You are a dumb fucking asshole. to catch a mouse you absolutely need to get that mouse out of the hole. no cheeze, no trap, no nothing!!!!")
                                        print("Game Over!")
                                        exit()
                                    else: # if dosnt match same again.. these lines runs and game over
                                        print("item not available")
                                        print("Now click enter to setup the trap to catch the mouse.")
                                        input()
                                        print("You are a dumb fucking asshole. to catch a mouse you absolutely need to get that mouse out of the hole. no cheeze, not trap, no nothing!!!!")
                                        print("Game Over!")
                                        exit()
                                else:
                                    print("You need to choose and type out the option down there and click enter to proceed!")
                                

                        else:
                            print("You need to choose and type out the option down there and click enter to proceed!")

                elif cheeze_brought == 0:
                    print("zero?? seriously?? be mature.. try again..")
                    break

                else:
                    print(" ass You need to choose and type out the option down there and click enter to proceed!")
                    continue
                
        elif cheeze == "quite":
            exit()    
        else:
            print("You need to choose and type out the option down there and click enter to proceed!")
            continue
                            
                        
                    
                    
                
def kitchen_store(kitchen_store, money): #************
    if kitchen_store == "kitchen":
        print("Here you found 1 cheeze!")
        print("Now we need to go to store to buy some more!")
        cheeze_available = 1 #cheeze

        print("Click enter to go to store:")
        input()

        k_s(kitchen_store, money, cheeze_available)
    elif kitchen_store == "store":
        cheeze_available = 1 #cheeze
        k_s(kitchen_store, money, cheeze_available) 


#####################################################################################################################################

def store(c, m, ch):
    cheeze = c
    money = m
    chance = ch
    print("Now you are in the store!")
    print("again as for reminder..")
    print("You have ")
    print(f"{cheeze} cheezes, {money}R money in wallet an till now {chance}% chance of catching the mouse.")
    print("choose things wisely based on this stat carefully")
    print()
    print()
    print("Now what do you think can be usefull for catching a mouse?")
    print("Type in something that you think can be usefull and see if that is available to buy or not")
    mouse_trap_chance = 25 #%   #MOUSE TRAP
    mouse_trap_price = 100 #R   #MOUSE TRAP
    mouse_trap = 0
    poison_price = 21 #R       #POISON
    poison_chance = 7.5 #%     #POISON
    while True:
        ask = input(">>>...").lower()

        if ask == "poison":
            print(f"Great. you are lucky! {ask} is available in store")
            print(f"Store keeper says one {ask} costs {poison_price}R")
            print("How many you would like to buy?")
            while True:
                b = input(">>>...").lower()
                if b.isdigit():
                    brought = int(b)
                    money -= poison_price * brought
                    chance += poison_chance * brought
                    while True:
                        if brought == 0:
                            print(f"seriously? 0? nope.. type no and click enter to say that you dont wanna buy any {ask} at all..")
                            break
                        elif money <= 0:
                            print(f"CAUTION! {(150 - money) - 150}R to buy anything. do the math and change the number of things you buy. try again..")
                            break
                        elif money > 0: #******************************************************
                            print(f"well you successfully brought {brought} {ask}s and have {money}R in the wallet left.")
                            print("")
                elif b == "quite":
                    exit()
                elif b == "no": ###########################
                    pass
                else:
                    print(f"please enter how many {ask} you want to buy..")

                    



        elif ask == "trap":
            print(f"Great. you are lucky! {ask} is available in store")
            print(f"Store keeper says one {ask} costs {mouse_trap_price}R")
            print("How many you would like to buy?")
            while True:
                b = input(">>>...").lower()
                if b.isdigit():
                    brought = int(b)
                    money -= mouse_trap_price * brought
                    chance += mouse_trap_chance * brought
                    while True:
                        if brought == 0:
                            print(f"seriously? 0? nope.. type no and click enter to say that you dont wanna buy any {ask} at all..")
                            break
                        elif money <= 0:
                            print(f"CAUTION! {(150 - money) - 150}R to buy anything. do the math and change the number of things you buy. try again..")
                            break
                        elif money > 0: #******************************************************
                            print(f"well you successfully brought {brought} {ask}s and have {money}R in the wallet left.")

                elif b == "quite":
                    exit()
                elif b == "no": #############################
                    pass
                else:
                    print(f"please enter how many {ask} you want to buy..")




        elif ask == "quite":
            exit()
        else:
            print(f"Sorry you are out of luck. {ask} isn't available in store according to the keeper! try other staff...")
            continue
            
            
def ass():
    print("my ass is fucked!")
    
ass()
print("asssss hole")
