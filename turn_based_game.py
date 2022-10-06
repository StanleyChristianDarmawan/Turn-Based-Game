class Hero:
    def __init__(self, name, damage, blood):
        self.name = name
        self.damage = damage
        self.blood = blood

    def attack(self, enemy):
        print("\n********ATTACK********")
        print(self.name + " attack " + enemy.name)
        enemy.blood -= self.damage
        if enemy.blood <= 0:
            enemy.blood = 0
        print(enemy.name + " blood = " + str(enemy.blood))
        if enemy.blood <= 0:
            enemy.blood = 0
        print("*****************************\n")
    
    def heal(self):
        print("\n++++++++HEAL++++++++")
        print(self.name + " Heal " + "50")
        self.blood += 10
        print(self.name + " blood: " + str(self.blood))
        print("\n+++++++++++++++++++++++++++++")

    # def reset_stat(self, name):
    #     player1_hero.blood = 


# Ryoshi = Hero("Ryoshi", 100, 500)
# Jadger = Hero("Jadger", 100, 500)

# MENU
def menu():
    # Reset Stats
    # Stats
    Ryoshi = Hero("Ryoshi", 100, 500)
    Jadger = Hero("Jadger", 100, 500)
    
    mode = int(input("""
    -----------------------------
    1. Single Player 
    2. Two Players
    Choose Mode(number): """))


    # Game Set
    if mode == 1:
        print("\nComing Soon")
        exit()
    elif mode == 2: #Two Players
        print("\n-----------------------------")

        player1_name = input("Enter Player 1 name: ")
        player2_name = input("Enter Player 2 name: ")

        print("\n-----------------------------")
        print(player1_name + " choose hero:")
        print("1. Ryoshi")
        print("2. Jadger")
        player1_hero = int(input("Choose Hero: "))

        print("-----------------------------")
        print(player2_name + " choose hero:")
        print("1. Ryoshi")
        print("2. Jadger")
        player2_hero = int(input("Choose Hero: "))
        print("-----------------------------")

        if player1_hero == 1:
            choosen_hero1 = Ryoshi
        elif player1_hero == 2:
            choosen_hero1 = Jadger

        if player2_hero == 1:
            choosen_hero2 = Ryoshi
        elif player2_hero == 2:
            choosen_hero2 = Jadger



        # GAME START
        print("\n-----------------------------")
        print("Game Started")
        # print(player1_name + " = " + str(choosen_hero1))
        # print(player2_name + " = " + str(choosen_hero2))
        print("-----------------------------")
        round = 1
        while int(choosen_hero1.blood) > 0 or int(choosen_hero2.blood) > 0:
            # if int(choosen_hero1.blood) <= 0:
            #     print(choosen_hero2.name + " Win")
            #     break
            # if int(choosen_hero2.blood) <= 0:
            #     print(choosen_hero1.name + " Win")
            #     break

            # ROUND
            print("===== Round " + str(round) + "=====")

            # Check player 1 blood
            if int(choosen_hero1.blood) <= 0:
                print("********** " + player2_name + " (" + choosen_hero2.name + ")" + " Win " + "**********")
                print("1. Back To Menu")
                print("2. Restart")
                next_input = int(input("Insert Number: "))
                if next_input == 1:
                    menu()
                if next_input == 2:
                    choosen_hero1 = player1_hero
                    choosen_hero2 = player2_hero
                    player1_name = player1_name
                    player2_name = player2_name
                    # player1.blood = 
                    menu()  

            # Player Turn
            print(player1_name + " (" + choosen_hero1.name + ") " + "Turn:")
            print("1. Attack")
            print("2. Heal")
            player1_attack = int(input("Enter Number: "))
            if player1_attack == 1:
                choosen_hero1.attack(choosen_hero2)
            elif player1_attack == 2:
                choosen_hero1.heal()
            else:
                print("Wrong number")
                exit()

            # Check player 2 blood
            if int(choosen_hero2.blood) <= 0:
                print("********** " + player1_name + " (" + choosen_hero1.name + ")" + " Win " + "**********")
                print("1. Back To Menu")
                print("2. Restart")
                next_input = int(input("Insert Number: "))
                if next_input == 1:
                    menu()
                    
            # Player Turn
            print(player2_name  + " (" + choosen_hero2.name + ") " + "Turn:")
            print("1. Attack")
            print("2. Heal")
            player2_attack = int(input("Enter Number: "))
            if player2_attack == 1:
                choosen_hero2.attack(choosen_hero1)
            elif player2_attack == 2:
                choosen_hero2.heal()

            round += 1

# Call Menu
menu()