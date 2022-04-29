loot = []

while True:
    print("\n\n Choices: ")
    print("\t [1] Heave what you're hankerin'for in your clipper.")
    print("\t [2] Throw the dregs out of your scooner.")
    print("\t [3] Steal a peek at what's stowed already.")
    print("\t [4] Stop spending coins you ain't got.")
    user_choice = input("\nGive me the number of what you wanna' do: ")

    if user_choice == '1':
        add_item = input("\nWhat you lustin' after? ")
        loot.append(add_item)
        print(f"\n\n Well done! You've stashed {add_item} in your clipper.")
        

    elif user_choice == '2':
        remove_item = input("\n Having second thoughts, Skinflint? What you wanna throw overboard? ")
        remove_item = remove_item.lower()
        # misspelling code
        if remove_item in loot:
            loot.remove(remove_item.lower())
            print(f"\n\n Commendations. You didn't need no {remove_item} anyway.")
        elif remove_item not in loot:
            print(f"\n\nLunkhead, cain't you remember or spell nuthin'?")
            print(f"\n Now, whack in a 2, pick one of these here that's really in your boat, and spell it the same:")
            for i in loot:
                print(f"\t {i.title()}")
           
    elif user_choice == '3':
        print("\nThis is the bounty you got already, you greedy bilge-sucker: ")
        for i in loot:
            print(f"\t {i.title()}")

    elif user_choice == '4':
        print(f"\n\nRun out of dubloons, eh? Here's your final booty:")
        for i in loot:
            print(f"\t {i.title()}")
        break
        

    
