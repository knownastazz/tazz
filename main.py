print("Welcome to the game TAZZ FIGHTING SIMULATOR. In this game, you will breach all of tazz's bodyguards, and break through their rooms to eventually fight the renown tazz.")
gaming = True

while gaming:

    import playerdata

    def Inventory():

        weapon = playerdata.data["weapon"]

        done = False
        while done == False:

            print("")
            print("-------- Inventory --------")
            pdata = sorted(playerdata.data)
            print("- 0: Exit inventory")
            print("------- Items -------")

            for index, key in enumerate(playerdata.data["Inventory"]):
                suffix = ""
                if (weapon == key):
                    suffix = " (Equipped)"
                print("- " + str(index + 1) + ": " + key + suffix)
            print("------- Consumables -------")

            for index, key in enumerate(playerdata.data["Consumables"]):
                if (key[1] != 0):
                    print(str(key[0]) + "( " + str(key[1]) + "x )" )
            print("-----------------------")
            action = input("Choose your action.")
            if action.isdigit() and len(action) == 1 and int(action) <= len(playerdata.data["Inventory"]):
                if playerdata.data["Inventory"][int(action) - 1] == weapon:
                    print("Weapon already equipped. Retry")
                else:
                    playerdata.data["weapon"] = playerdata.data["Inventory"][int(action) - 1]
                    print("Equipped " + playerdata.data["Inventory"][int(action) - 1])
                    done = True
            else:
                print("Invalid input. Reselect.")

    def GameMenu():

        selecting = True
        while selecting:
            print("")
            print("-------- Choose your action --------")
            print("- 1: Challenge room 1. (NAV)")
            print("- 2: Challenge room 2. (Mr. Simonsen)")
            print("- 3: Challenge room 3. (Walter White)")
            print("- 4: Challenge room 4. (Tazz)")
            print("---------------")
            print("- 5: Open inventory")
            print("- 6: Save, and quit.")
            print("------------------------------------")
            action = input("Choose your action.")
            if action.isdigit() and len(action) == 1 and int(action) < 6:
                print("You chose " + action)
                selecting = False
                if action == "5":
                    Inventory()
            else:
                print("Invalid input. Reselect.")

    GameMenu();