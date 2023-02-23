
# Ultimate Battleships

def print_ships_to_be_placed():
    print("Ships to be placed:", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Ships to be placed: ")


# elem expected to be a single list element of a primitive type.
def print_single_element(elem):
    print(str(elem), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write(str(elem) + " ")


def print_empty_line():
    print()
    if FILE_OUTPUT_FLAG:
        f.write("\n")


# n expected to be str or int.
def print_player_turn_to_place(n):
    print("It is Player {}'s turn to place their ships.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to place their ships.\n".format(n))


def print_to_place_ships():
    print("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) : \n")
        # There is a \n because we want the board to start printing on the next line.


def print_incorrect_input_format():
    print("Input is in incorrect format, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Input is in incorrect format, please try again.\n")


def print_incorrect_coordinates():
    print("Incorrect coordinates given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect coordinates given, please try again.\n")


def print_incorrect_ship_name():
    print("Incorrect ship name given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect ship name given, please try again.\n")


def print_incorrect_orientation():
    print("Incorrect orientation given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect orientation given, please try again.\n")


# ship expected to be str.
def print_ship_is_already_placed(ship):
    print(ship, "is already placed, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " is already placed, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_outside(ship):
    print(ship, "cannot be placed outside the board, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed outside the board, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_occupied(ship):
    print(ship, "cannot be placed to an already occupied space, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed to an already occupied space, please try again.\n")


def print_confirm_placement():
    print("Confirm placement Y/N :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Confirm placement Y/N : \n")


# n expected to be str or int.
def print_player_turn_to_strike(n):
    print("It is Player {}'s turn to strike.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to strike.\n".format(n))


def print_choose_target_coordinates():
    print("Choose target coordinates :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Choose target coordinates : ")


def print_miss():
    print("Miss.")
    if FILE_OUTPUT_FLAG:
        f.write("Miss.\n")


# n expected to be str or int.
def print_type_done_to_yield(n):
    print("Type done to yield your turn to player {} :".format(n), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Type done to yield your turn to player {} : \n".format(n))


def print_tile_already_struck():
    print("That tile has already been struck. Choose another target.")
    if FILE_OUTPUT_FLAG:
        f.write("That tile has already been struck. Choose another target.\n")


def print_hit():
    print("Hit!")
    if FILE_OUTPUT_FLAG:
        f.write("Hit!\n")


# n expected to be str or int.
def print_player_won(n):
    print("Player {} has won!".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("Player {} has won!\n".format(n))


def print_thanks_for_playing():
    print("Thanks for playing.")
    if FILE_OUTPUT_FLAG:
        f.write("Thanks for playing.\n")


# my_list expected to be a 3-dimensional list, formed from two 2-dimensional lists containing the boards of each player.
def print_3d_list(my_list):
    first_d = len(my_list[0])
    for row_ind in range(first_d):
        second_d = len(my_list[0][row_ind])
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[0][row_ind][col_ind], end=' ')
        print("\t\t\t", end='')
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[1][row_ind][col_ind], end=' ')
        print()
    print("", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\t\t", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\nPlayer 1\t\t\t\t\t\tPlayer 2")
    print()

    if FILE_OUTPUT_FLAG:
        first_d = len(my_list[0])
        for row_ind in range(first_d):
            second_d = len(my_list[0][row_ind])
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[0][row_ind][col_ind] + " ")
            f.write("\t\t\t")
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[1][row_ind][col_ind] + " ")
            f.write("\n")
        f.write("   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\t\t   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\nPlayer 1\t\t\t\t\t\tPlayer 2\n")
        f.write("\n")


def print_rules():
    print("Welcome to Ultimate Battleships")
    print("This is a game for 2 people, to be played on two 10x10 boards.")
    print("There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).")
    print("First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.")
    print("Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.")
    print("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.")
    print("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.")
    print("Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.")
    print("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.")
    print("The last player to have an unsunk ship wins.")
    print("Have fun!")
    print()

    if FILE_OUTPUT_FLAG:
        f.write("Welcome to Ultimate Battleships\n")
        f.write("This is a game for 2 people, to be played on two 10x10 boards.\n")
        f.write(
            "There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).\n")
        f.write(
            "First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.\n")
        f.write(
            "Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.\n")
        f.write("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.\n")
        f.write("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.\n")
        f.write(
            "Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.\n")
        f.write("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.\n")
        f.write("The last player to have an unsunk ship wins.\n")
        f.write("Have fun!\n")
        f.write("\n")


# Create the game
board_size = 10
f = open('UltimateBattleships.txt', 'w')
FILE_OUTPUT_FLAG = True  # You can change this to True to also output to a file so that you can check your outputs with diff.

print_rules()

# Remember to use list comprehensions at all possible times.
# If we see you populate a list that could be done with list comprehensions using for loops, append/extend/insert etc. you will lose points.

# Make sure to put comments in your code explaining your approach and the execution.

# We defined all the functions above for your use so that you can focus only on your code and not the formatting.
# You need to call them in your code to use them of course.

# If you have questions related to this homework, direct them to utku.bozdogan@boun.edu.tr please.

# Do not wait until the last day or two to start doing this homework, it requires serious effort.

try:  # The entire code is in this try block, if there ever is an error during execution, we can safely close the file.
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE


#Firstly, I created my lists that I need.
    # Actually 4 list was enough but while I wrote the code, I create I empty list so that I won't be confused.
    #Also I create a dcitionary because when I wrote the error of ship is occupied, I should write the ship name again, because it is not located.
    # That's why, I create a dictionary with ship names and their lenghts. When I need it I call this dictionary and its keys or values.
    #Lastly I create a list for players. Because I wrote this code in while loops, I create a list to call the player that I need.
    ikincinin_birinciye_goruneni= [["-" for i in range(board_size)] for j in range(board_size)]
    birincinin_ikinciye_goruneni = [["-" for i in range(board_size)] for j in range(board_size)]
    dolu_1= [["-" for i in range(board_size)] for j in range(board_size)]
    dolu_2 = [["-" for i in range(board_size)] for j in range(board_size)]
    bos_liste= [["-" for i in range(board_size)] for j in range(board_size)]
    ships = ["Carrier","Battleship","Cruiser","Submarine","Destroyer"]
    ship_name = {"Carrier": 5, "Battleship": 4, "Cruiser": 3, "Submarine": 3, "Destroyer": 2}
    user= [1, 2]
    elma = True
    # When we come here, we see that I define 2 variables, which count the number of ! to stop the code when the number of ! reach 17.
    birinciunlem= 0
    ikinciunlem = 0
    # First of all, you want us to create a 2 dimensional 2 lists so I wrote them.
    # Because I want to turn the loop for every ship that I define, I wrote these in a while loop.
    # I define while loop depending on a variable (elma) so that I can break the loop on the correct position to run my code correctly.
    while elma:
        dolu_1 = [["-" for i in range(board_size)] for j in range(board_size)]
        dolu_2 = [["-" for i in range(board_size)] for j in range(board_size)]
        bos_liste = [["-" for i in range(board_size)] for j in range(board_size)]
        ships = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
        ship_name = {"Carrier": 5, "Battleship": 4, "Cruiser": 3, "Submarine": 3, "Destroyer": 2}
        # I use another while loop because I want to turn this while loop depending on the number of my ship so that I create a list which is ships.
        while 0<len(ships):
            print_3d_list([dolu_1,dolu_2])

            print_ships_to_be_placed()
            for i in ships:
                print_single_element(i)
            print_empty_line()
            print_player_turn_to_place(user[0])

            print_to_place_ships()
            # Here, I want an input to my player. I use strip to remove whitespaces.
            # after that I cover my input to lower because it can be case insensitive.
            # Lastly I use split to separate my elements in my input.
            #also split is very useful method for my code because I can call teh elements of this new list by indexing.
            a = input().strip().lower().split()
            a[0] = a[0].capitalize()
            #isdigit is other method which controls my element whether it contains an non integer.
            if a[1].isdigit() == False:
                print_incorrect_input_format()
                continue
            elif a[2].isdigit() == False:
                print_incorrect_input_format()
                continue
            #if my input contains more than 4 element then my code should give an error, so I call this function.
            elif len(a) < 4:
                print_incorrect_input_format()
                continue
            #if my player give a number which is outside the board I should give a incorrect coordinate error so I call this function.
            if int(a[1])>10 or int(a[1])<=0:
                print_incorrect_coordinates()
                continue
            elif int(a[2]) > 10 or int(a[2])<=0:
                print_incorrect_coordinates()
                continue
            #if my ship is already placed which means that it is not in ships but it is in my dictionary (ship_name) then I should give an error.
            if a[0] not in ships and a[0] in ship_name.keys() :
                print_ship_is_already_placed(a[0])
                continue
            #if my player give a ship name which is not in my original ship name, then the system should give an error.
            if a[0] not in ships:
                print_incorrect_ship_name()
                continue
            # if I want to place my ship horizontally then I should think an equation. Because on my board I change "-"'s with "#"'s, I should calculate the total max length correctly when I place my ships.
            #That's why, I should add my ship length to my location. Because I start to my given number,(I place it too I cannot skip it.) I should add 1 to my equation but the other side.
            if a[3] == "h" and ship_name[a[0]] + int(a[1]) > 11:
                print_ship_cannot_be_placed_outside(a[0])
                continue
            # if I want to place my ship vertically then I should think an equation. Because on my board I change "-"'s with "#"'s, I should calculate the total max length correctly when I place my ships.
            # That's why, I should add my ship length to my location. Because I start to my given number,(I place it too I cannot skip it.) I should add 1 to my equation but the other side.
            if a[3] == "v" and ship_name[a[0]] + int(a[2]) > 11:
                print_ship_cannot_be_placed_outside(a[0])
                continue

            # I defined a variable so that ı can use it when I take an error.
            is_occupied = False
            # When I look horizontally, if there is one # which is occupied with another # then the value of my variable will cahnge and it will be True.
            if a[3] == 'h':
                for i in range(ship_name[a[0]]):
                    if dolu_1[int(a[2]) - 1][int(a[1]) - 1 + i] == "#":
                        is_occupied = True
                        break
            # When I look vertically, if there is one # which is occupied with another # then the value of my variable will cahnge and it will be True.
            elif a[3]== "v":
                for i in range(ship_name[a[0]]):
                    if dolu_1[int(a[2]) - 1 + i][int(a[1]) - 1] == "#":
                        is_occupied = True
                        break

            loop = False
            for m in range(ship_name[a[0]]):

                if a[3] == 'h':
                    # when we come here, I will place my ships, but there is an important part, which is being occupied with another ship.
                    # I will use the value of my variable(is_occupied). If it is True which means that my # is occupied with another # so my ship cannot be placed.
                    # If it is False then I can place my ship the given coordinates.
                     if is_occupied:
                        print_ship_cannot_be_placed_occupied(a[0])
                        break
                     else:
                        dolu_1[int(a[2]) - 1][int(a[1]) - 1 + m] = "#"
                        if a[0] in ships:
                            ships.remove(a[0])




                elif a[3] == 'v':
                    # when we come here, I will place my ships, but there is an important part, which is being occupied with another ship.
                    # I will use the value of my variable(is_occupied). If it is True which means that my # is occupied with another # so my ship cannot be placed.
                    # If it is False then I can place my ship the given coordinates.
                    if is_occupied:
                        print_ship_cannot_be_placed_occupied(a[0])
                        break
                    else:
                        dolu_1[int(a[2]) - 1 + m][int(a[1]) - 1] = "#"
                        if a[0] in ships:
                            ships.remove(a[0])


                else:
                    #If player wrote another thing except v and h, then my loop should be broken and I should change my variable (loop) to continue to run the code.
                    loop = True
                    break
            if loop:
                #When the system continue to run the code it should write the error name which is incorrect orientation and it should continue to take the value up to the user wrote v or h.
                print_incorrect_orientation()
                continue




        print_3d_list([dolu_1, bos_liste])
        # when player place the ships, the system should take an confirm.
        print_confirm_placement()
        b = input()
        while (b.upper() != "N" and b.upper() != "Y"):
            print_confirm_placement()
            b = input()
        # If player's answer is no, then the system should take all the values again.
        if b.upper() == "N":
            continue
        # If player's answer is yes, then the system continue with the other player.
        elif b.upper() == "Y":


            muz = True
            while muz:
                bos_liste = [["-" for i in range(board_size)] for j in range(board_size)]
                dolu_2 = [["-" for i in range(board_size)] for j in range(board_size)]
                ships = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
                ship_name = {"Carrier": 5, "Battleship": 4, "Cruiser": 3, "Submarine": 3, "Destroyer": 2}
                user = [1, 2]
                while 0 < len(ships):
                    print_3d_list([bos_liste, dolu_2])

                    print_ships_to_be_placed()
                    for i in ships:
                        print_single_element(i)
                    print_empty_line()
                    print_player_turn_to_place(user[1])
                    # Here, I want an input to my other player. I use strip to remove whitespaces.
                    # after that I cover my input to lower because it can be case insensitive.
                    # Lastly I use split to separate my elements in my input.
                    # also split is very useful method for my code because I can call the elements of this new list by indexing.
                    print_to_place_ships()
                    a = input().strip().lower().split()
                    a[0] = a[0].capitalize()
                    # isdigit is other method which controls my element whether it contains an non integer.
                    if a[1].isdigit() == False:
                        print_incorrect_input_format()
                        continue
                    elif a[2].isdigit() == False:
                        print_incorrect_input_format()
                        continue
                    # if my input contains more than 4 element then my code should give an error, so I call this function.
                    elif len(a) < 4:
                        print_incorrect_input_format()
                        continue

                    # if my player give a number which is outside the board I should give a incorrect coordinate error so I call this function.
                    if int(a[1]) > 10 or int(a[1])<=0:
                        print_incorrect_coordinates()
                        continue
                    elif int(a[2]) > 10 or int(a[2])<=0:
                        print_incorrect_coordinates()
                        continue
                    # if my ship is already placed which means that it is not in ships but it is in my dictionary (ship_name) then I should give an error.
                    if a[0] not in ships and a[0] in ship_name.keys() :
                        print_ship_is_already_placed(a[0])
                        continue
                    # if my player give a ship name which is not in my original ship name, then the system should give an error.
                    if a[0] not in ships:
                        print_incorrect_ship_name()
                        continue

                    # if I want to place my ship horizontally then I should think an equation. Because on my board I change "-"'s with "#"'s, I should calculate the total max length correctly when I place my ships.
                    # That's why, I should add my ship length to my location. Because I start to my given number,(I place it too I cannot skip it.) I should add 1 to my equation but the other side.
                    if a[3] == "h" and ship_name[a[0]] + int(a[1]) > 11:
                        print_ship_cannot_be_placed_outside(a[0])
                        continue
                    # if I want to place my ship vertically then I should think an equation. Because on my board I change "-"'s with "#"'s, I should calculate the total max length correctly when I place my ships.
                    # That's why, I should add my ship length to my location. Because I start to my given number,(I place it too I cannot skip it.) I should add 1 to my equation but the other side.
                    if a[3] == "v" and ship_name[a[0]] + int(a[2]) >11:
                        print_ship_cannot_be_placed_outside(a[0])
                        continue
                    # I defined a variable so that ı can use it when I take an error.
                    is_occupied = False
                    # When I look horizontally, if there is one # which is occupied with another # then the value of my variable will cahnge and it will be True.
                    if a[3] == 'h':
                        for i in range(ship_name[a[0]]):
                            if dolu_2[int(a[2]) - 1][int(a[1]) - 1 + i] == "#":
                                is_occupied = True
                                break
                    # When I look vertically, if there is one # which is occupied with another # then the value of my variable will cahnge and it will be True.
                    elif a[3] == "v":
                        for i in range(ship_name[a[0]]):
                            if dolu_2[int(a[2]) - 1 + i][int(a[1]) - 1] == "#":
                                is_occupied = True
                                break

                    loop = False
                    for m in range(ship_name[a[0]]):

                        if a[3] == 'h':
                            # when we come here, I will place my ships, but there is an important part, which is being occupied with another ship.
                            # I will use the value of my variable(is_occupied). If it is True which means that my # is occupied with another # so my ship cannot be placed.
                            # If it is False then I can place my ship the given coordinates.

                            if is_occupied:
                                print_ship_cannot_be_placed_occupied(a[0])
                                break
                            else:
                                dolu_2[int(a[2]) - 1][int(a[1]) - 1 + m] = "#"
                                if a[0] in ships:
                                    ships.remove(a[0])

                        elif a[3] == 'v':
                            # when we come here, I will place my ships, but there is an important part, which is being occupied with another ship.
                            # I will use the value of my variable(is_occupied). If it is True which means that my # is occupied with another # so my ship cannot be placed.
                            # If it is False then I can place my ship the given coordinates.
                            if is_occupied:
                                print_ship_cannot_be_placed_occupied(a[0])
                                break
                            else:
                                dolu_2[int(a[2]) - 1 + m][int(a[1]) - 1] = "#"
                                if a[0] in ships:
                                    ships.remove(a[0])


                        else:
                            # If player wrote another thing except v and h, then my loop should be broken and I should change my variable (loop) to continue to run the code.
                            loop = True
                            break
                    if loop:
                        # When the system continue to run the code it should write the error name which is incorrect orientation and it should continue to take the value up to the user wrote v or h.
                        print_incorrect_orientation()
                        continue

                print_3d_list([bos_liste, dolu_2])
                # when player place the ships, the system should take an confirm.
                print_confirm_placement()
                b = input()
                while b.upper() != "N" and b.upper() != "Y":
                    print_confirm_placement()
                    b = input()
                # If player's answer is no, then the system should take all the values again.
                if b.upper() == "N":
                    continue
                ## If player's answer is yes then the system will start the hit.
                elif b.upper() == "Y":
                    armut= True
                    while armut:
                        f_user = [1, 2]
                        t = True
                        while t:
                            print_3d_list([dolu_1, ikincinin_birinciye_goruneni])
                            #Firstly, the first player will start the game. dolu1 is a list that the system stocked the ships, and ikincininbirinciyegoruneni is another list which is stored the hit and miss at the 2nd player board.
                            print_player_turn_to_strike(f_user[0])
                            print_choose_target_coordinates()
                            # I take the input from my player after that I strip it to remove white spaces and I split it to store it in a list one by one.
                            m=input().strip().split()
                            # if my player enter a number of input less than 2 then my sistem will give an error.
                            if len(m) != 2:
                                 print_incorrect_input_format()
                                 continue
                            # if my player enter numbers in the type of string or float then my system should give an error.
                            if m[0].isdigit() == False:
                                print_incorrect_input_format()
                                continue
                            elif m[1].isdigit() == False:
                                print_incorrect_input_format()
                                continue
                            # If my player enter a number which is less or equal to 0 or more than 10 then my system should give an error.
                            if int(m[0]) > 10 or int(m[0])<=0:
                                print_incorrect_coordinates()
                                continue
                            elif int(m[1]) > 10 or int(m[1])<=0:
                                print_incorrect_coordinates()
                                continue

                            input_y = int(m[0]) - 1
                            input_x = int(m[1]) - 1
                            #If the given coordinates == #, it means that you hit. During you hit the ship you should continue the game while you miss so I use continue.
                            if dolu_2[input_x][input_y] == "#":
                                print_hit()
                                # The system wrote ! when the player hit the ship. Also, the system should wrote ! both my list because I use these list when the game continue.
                                dolu_2[input_x][input_y] = "!"
                                ikincinin_birinciye_goruneni[input_x][input_y] = "!"
                                #Here, I define a variable which allow the system to count the number of !.
                                # I wrote it here because I have to look the number of ! before player changing to finish the game in correct time.
                                ikinciunlem += 1
                                if ikinciunlem == 17:
                                    print_3d_list([dolu_1, ikincinin_birinciye_goruneni])
                                    print_player_won(f_user[0])
                                    print_thanks_for_playing()
                                    # I change the value of all of my variables because if the game finish, the system should stop correct place.
                                    elma= False
                                    armut= False
                                    muz = False
                                    t = False
                                    n = False
                                    ships = []
                                    break
                                continue
                            elif dolu_2[input_x][input_y] == "-":
                                #if the given coordinates == - then player miss.
                                print_miss()

                                while True:
                                    print_type_done_to_yield(f_user[1])
                                    #the system want the player to write done to continue with other player. If the player 1 cannot write done correctly then the system continue to want the player to write done.
                                    b=input()
                                    b= b.lower()
                                    if b == "done":
                                        break

                                # when the player miss then system change # to 0.
                                # The system wrote 0 when the player miss the ship. Also, the system should wrote 0 both my list because I use these list when the game continue.
                                dolu_2[input_x][input_y] = "O"
                                ikincinin_birinciye_goruneni[input_x][input_y] = "O"
                                break
                            # if the given strike numbers equals the ! or 0 from before, then the system write tile is already struck and it wants to take strike numbers again.
                            elif dolu_2[input_x][input_y] == "!" or dolu_2[input_x][input_y] == "O":
                                print_tile_already_struck()



                        n = True
                        # In the same way, if ikinciunlemsayisi == 17 then the game finish and the system is closed.
                        if ikinciunlem == 17:

                            n= False
                        while n:
                            print_3d_list([birincinin_ikinciye_goruneni, dolu_2])
                            #Firstly, the first player will start the game. dolu2 is a list that the system stocked the ships, and birincininikinciyegoruneni is another list which is stored the hit and miss at the 2nd player board.
                            print_player_turn_to_strike(f_user[1])
                            print_choose_target_coordinates()
                            # I take the input from my player after that I strip it to remove white spaces and I split it to store it in a list one by one.
                            v = input().strip().split()
                            #if my player enter a number of input less than 2 then my sistem will give an error.
                            if len(v) != 2:
                                print_incorrect_input_format()
                                continue
                            #if my player enter numbers in the type of string or float then my system should give an error.
                            if v[0].isdigit() == False:
                                print_incorrect_input_format()
                                continue
                            elif v[1].isdigit() == False:
                                print_incorrect_input_format()
                                continue
                            #If my player enter a number which is less or equal to 0 or more than 10 then my system should give an error.
                            if int(v[0]) > 10 or int(v[0])<=0:
                                print_incorrect_coordinates()
                                continue
                            elif int(v[1]) > 10 or int(v[1])<=0:
                                print_incorrect_coordinates()
                                continue

                            input_y = int(v[0]) - 1
                            input_x = int(v[1]) - 1
                            #If the given coordinates == #, it means that you hit. During you hit the ship you should continue the game while you miss so I use continue.
                            if dolu_1[input_x][input_y] == "#":
                                print_hit()
                                # The system wrote ! when the player hit the ship. Also, the system should wrote ! both my list because I use these list when the game continue.
                                dolu_1[input_x][input_y] = "!"
                                birincinin_ikinciye_goruneni[input_x][input_y] = "!"
                                # Here, I define a variable which allow the system to count the number of !.
                                # I wrote it here because I have to look the number of ! before player changing to finish the game in correct time.
                                birinciunlem += 1
                                if birinciunlem == 17:
                                    print_3d_list([birincinin_ikinciye_goruneni, dolu_2])
                                    print_player_won(f_user[1])
                                    print_thanks_for_playing()
                                    # I change the value of all of my variables because if the game finish, the system should stop correct place.
                                    elma = False
                                    armut= False
                                    muz = False
                                    n = False
                                    t = False
                                    ships=[]
                                    break
                                continue
                            elif dolu_1[input_x][input_y] == "-":
                                #if the given coordinates == - then player miss.
                                print_miss()
                                while True:

                                    print_type_done_to_yield(f_user[0])
                                    #the system want the player to write done to continue with other player. If the player 1 cannot write done correctly then the system continue to want the player to write done.
                                    b = input()
                                    b = b.lower()
                                    if b == "done":
                                        break
                                # when the player miss then system change # to 0.
                                # The system wrote 0 when the player miss the ship. Also, the system should wrote 0 both my list because I use these list when the game continue.
                                dolu_1[input_x][input_y] = "O"
                                birincinin_ikinciye_goruneni[input_x][input_y] = "O"
                                break
                            # if the given strike numbers equals the ! or 0 from before, then the system write tile is already struck and it wants to take strike numbers again.
                            elif dolu_1[input_x][input_y] == "!" or dolu_1[input_x][input_y] == "O":
                                print_tile_already_struck()



                        n = False



    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
except:
    f.close()

