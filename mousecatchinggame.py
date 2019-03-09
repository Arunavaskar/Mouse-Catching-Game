from enterFunc import still_need_to_clean, found_wallet, kitchen_store, store

print("Enter your name to continue!")
user_input = input(">>>... ").lower()
if user_input == "quite":
    print("Bye")
    exit()
else:
        while True:
            print(f"Hey there {user_input}!")
            
            print(f"Left or Right")

            while True:
                
                left_right = input(">>>... ").lower()

                if left_right == "left":                      # LEFT LEFT LEFT LEFT
                    print("You chosed Left!".title())
                    print("Room is dirty and smelling!".title())
                    
                    print("clean it, spray room freshner or use fregrance sticks".title())
                    while True:
                        clean_spray_sticks = input(">>>... ").lower()
                        
                        if clean_spray_sticks == "clean":          # CLEAN CLEAN CLEAN
                            money = 150 #R
                            found_wallet(money)
                            print("For cheeze you can either go to kitchen or go to store directly")
                            while True:
                                kitchen_store = input(">>>...").lower()

                                kitchen_store(kitchen_store, money)


                        elif clean_spray_sticks == "spray":           # SPRAY SPRAY SPRAY
                            print("Sprayed the room freshner!")
                            still_need_to_clean()
                            money = 150 #R
                            found_wallet(money)
                            print("For cheeze you can either go to kitchen or go to store directly")
                            while True:
                                kitchen_store = input(">>>...").lower()

                                kitchen_store(kitchen_store, money)
                        elif clean_spray_sticks == "fregrance" or "sticks": # STICKS STICKS STICKS
                            print("Used fregrance sticks!")
                            still_need_to_clean()
                            money = 150 #R
                            found_wallet(money)
                            print("For cheeze you can either go to kitchen or go to store directly")
                            while True:
                                kitchen_store = input(">>>...").lower()

                                kitchen_store(kitchen_store, money)
                        elif clean_spray_sticks == "quite":
                            exit()
                        else:
                            print("Nope! you need to choose from the given options and type one down, then click enter to continue")
                            continue

                elif left_right == "right":                   # RIGHT RIGHT RIGHT RIGHT
                    print("You chosed right!".title())
                    print("It's a blank room.".title())
                    money = 150 #R
                    found_wallet(money)
                    print("So. Do you want to go to kitchen first or go to the store?")

                    while True:
                        kitchen_store = input(">>>... ").lower()

                        if kitchen_store == "kitchen":  #kitchen
                            print("So i kitchen you found 1 cheeze!")
                            cheeze = 1 # cheeze
                            print("To catch a mouse you need to have 100% chances to catch it.")
                            print("1 cheeze gives you 15% chance to catch a mouse.")
                            cheeze_chance = 15 # chances per cheeze
                            chance = cheeze * cheeze_chance # chances available after finding a cheeze in the kitchen
                            cheeze_price = 2 #R
                            print("now obviously you need 100% chances to catch a mouse and that means more cheeze.")
                            print("To buy go to store for buying cheeze click enter!")
                            input()
                            print("15% chances you have means yo still need 100 - 15 = 75% chances more to get the mouse.")
                            print("How many cheeze you want buy? *per cheeze costs 2R if you do not want to buy cheeze type no and click enter!*")
                            while True:
                                c_b = input(">>>...").lower()
                                if c_b.isdigit():
                                    cheeze_brought = c_b
                                    while True:
                                        if cheeze_brought <= 4:
                                            cheeze += cheeze_brought
                                            money -= cheeze_brought * cheeze_price
                                            chance *= cheeze_brought
                                            print("stats:")
                                            print(f"cheeze= {cheeze} money= {money} chance you have to catch= {chance}")
                                            #STORE
                                            print("Now you need more staff to catch the mouse!")
                                            print("Click enter to go to store..")
                                            while True:
                                                i = input().lower()
                                                if i == "quite":
                                                    exit()
                                                else:
                                                    store(cheeze, money, chance)

                                        elif cheeze_brought == 0:
                                            print("seriously? 0?? if you dont wanna buy cheeze simply type no and click enter to continue!")
                                            break
                                        elif cheeze_brought > 4:
                                            print("sorry but store keeper says they only have 4 cheeze to sell.")
                                            print("What do you want to do?")
                                            print("Buy all 4 cheeze?")
                                            print("To buy buy all 4 cheeze at once type yes and click enter..")
                                            print("To try out custom ammount of cheeze numbers to buy, type no and click enter.")
                                            while True:
                                                yes_no = input(">>>...").lower()

                                                if yes_no == "no":
                                                    break
                                                elif yes_no == "yes":
                                                    cheeze += 4 #5
                                                    money -= 4 * cheeze_price #150 = 4 * 2 = 142
                                                    chance *= cheeze_brought # chance = 15 * 4 = 60
                                                    print("stats:")
                                                    print(f"cheeze= {cheeze} money= {money} chance you have to catch= {chance}")
                                                    #STORE
                                                    print("Now you need more staff to catch the mouse!")
                                                    print("Click enter to go to store..")
                                                    while True:
                                                        i = input().lower()
                                                        if i == "quite":
                                                            exit()
                                                        else:
                                                            store(cheeze, money, chance)
                                                elif yes_no == "quite":
                                                    exit()
                                                else:
                                                    print("You need to choose and type out the option down there and click enter to proceed!")
                                                    continue
                                        
                                elif c_b == "quite":
                                    exit()
                                elif c_b == "no":
                                    pass
                                else:
                                    print("You need to choose and type out the option down there and click enter to proceed!")
                                    continue


                        elif kitchen_store == "store":  #store
                            print("store".title())
                        elif kitchen_store == "quite":
                            exit()
                        else:
                            print("You have to choose either kitchen or store.".title())
                            continue

                elif left_right == "quite":
                        print("Bye")
                        exit()
                else:                                           # NEITHER LEFT NOR RIGHT   NEITHER LEFT NOR RIGHT
                    print("You have to choose either left or right.".title())
                    print("""*again
                                    `
                                      `
                                        `
                                          |
                                          *""")
                    continue