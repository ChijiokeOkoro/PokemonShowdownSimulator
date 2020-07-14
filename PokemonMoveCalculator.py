from selenium import webdriver
import PokemonMovePower
import StabCalc
import TypeCalc

# power calculation = stab x type x basePower-
# does not include weather abilities or BST in power calculation

def calcpower(moves, types, monStr, choice):
    # moves = list of moves
    # types = list of list of typings
    # mons = list of mons
    # choice = string containing your mon

    # determines the name & type of your pokemon & opponents
    if choice == monStr[0]:
        mystab = types[0]
        oppotype = types[1]
    else:
        mystab = types[1]
        oppotype = types[0]

    # gets the stab value of each move
    if len(moves) == 1:  # 1 move
        return 0
    elif len(moves) == 2:  # 2 moves
        # stores each move name in a string
        move1 = moves[0].get_attribute("data-move")
        move2 = moves[1].get_attribute("data-move")

        # checks to see if a move is the same typing as the pokemon using it (STAB)
        stab1 = StabCalc.stab(mystab, move1)
        stab2 = StabCalc.stab(mystab, move2)

        if len(oppotype) == 2: # if a pokemon has only one typing
            power1 = stab1 * PokemonMovePower.basePower(move1) * TypeCalc.detEff(oppotype[1], move1)
            power2 = stab2 * PokemonMovePower.basePower(move2) * TypeCalc.detEff(oppotype[1], move2)
            print(move1 + ': Power = ' + str(stab1) + ' * ' + str(PokemonMovePower.basePower(move1)) + ' * ' + str(TypeCalc.detEff(oppotype[1], move1)) + ' = ' + str(power1))
            print(move2 + ': Power = ' + str(stab2) + ' * ' + str(PokemonMovePower.basePower(move2)) + ' * ' + str(TypeCalc.detEff(oppotype[1], move2)) + ' = ' + str(power2))
            if power1 >= power2: # index of strongest powered move is selected. Order of priority is 0 -> 1 -> 2 -> 3
                return 0
            else:
                return 1
        else: # pokemon has two typings or the typing repeats
            power1 = stab1 * PokemonMovePower.basePower(move1) * TypeCalc.detEff(oppotype[1], move1) * TypeCalc.detEff(oppotype[2], move1)
            power2 = stab2 * PokemonMovePower.basePower(move2) * TypeCalc.detEff(oppotype[1], move2) * TypeCalc.detEff(oppotype[2], move2)
            print(move1 + ': Power = ' + str(stab1) + ' * ' + str(PokemonMovePower.basePower(move1)) + ' * ' + str(TypeCalc.detEff(oppotype[1], move1)) + ' * ' + str(TypeCalc.detEff(oppotype[2], move1)) + ' = ' + str(power1))
            print(move2 + ': Power = ' + str(stab2) + ' * ' + str(PokemonMovePower.basePower(move2)) + ' * ' + str(TypeCalc.detEff(oppotype[1], move2)) + ' * ' + str(TypeCalc.detEff(oppotype[2], move2)) + ' = ' + str(power2))
            if power1 >= power2:
                return 0
            else:
                return 1


    elif len(moves) == 3:  # 3 total moves
        move1 = moves[0].get_attribute("data-move")
        move2 = moves[1].get_attribute("data-move")
        move3 = moves[2].get_attribute("data-move")

        stab1 = StabCalc.stab(mystab, move1)
        stab2 = StabCalc.stab(mystab, move2)
        stab3 = StabCalc.stab(mystab, move3)

        if len(oppotype) == 2:
            power1 = stab1 * PokemonMovePower.basePower(move1) * TypeCalc.detEff(oppotype[1], move1)
            power2 = stab2 * PokemonMovePower.basePower(move2) * TypeCalc.detEff(oppotype[1], move2)
            power3 = stab3 * PokemonMovePower.basePower(move3) * TypeCalc.detEff(oppotype[1], move3)
            print(move1 + ': Power = ' + str(stab1) + ' * ' + str(PokemonMovePower.basePower(move1)) + ' * ' + str(TypeCalc.detEff(oppotype[1], move1)) + ' = ' + str(power1))
            print(move2 + ': Power = ' + str(stab2) + ' * ' + str(PokemonMovePower.basePower(move2)) + ' * ' + str(TypeCalc.detEff(oppotype[1], move2)) + ' = ' + str(power2))
            print(move3 + ': Power = ' + str(stab3) + ' * ' + str(PokemonMovePower.basePower(move3)) + ' * ' + str(TypeCalc.detEff(oppotype[1], move3)) + ' = ' + str(power3))
            if power1 >= power2 and power1 >= power3:
                return 0
            elif power2 >= power1 and power2 >= power3:
                return 1
            else:
                return 2
        else:
            power1 = stab1 * PokemonMovePower.basePower(move1) * TypeCalc.detEff(oppotype[1], move1) * TypeCalc.detEff(oppotype[2], move1)
            power2 = stab2 * PokemonMovePower.basePower(move2) * TypeCalc.detEff(oppotype[1], move2) * TypeCalc.detEff(oppotype[2], move2)
            power3 = stab3 * PokemonMovePower.basePower(move3) * TypeCalc.detEff(oppotype[1], move3) * TypeCalc.detEff(oppotype[2], move3)
            print(move1 + ': Power = ' + str(stab1) + ' * ' + str(PokemonMovePower.basePower(move1)) + ' * ' + str(TypeCalc.detEff(oppotype[1], move1)) + ' * ' + str(TypeCalc.detEff(oppotype[2], move1)) + ' = ' + str(power1))
            print(move2 + ': Power = ' + str(stab2) + ' * ' + str(PokemonMovePower.basePower(move2)) + ' * ' + str(TypeCalc.detEff(oppotype[1], move2)) + ' * ' + str(TypeCalc.detEff(oppotype[2], move2)) + ' = ' + str(power2))
            print(move3 + ': Power = ' + str(stab3) + ' * ' + str(PokemonMovePower.basePower(move3)) + ' * ' + str(TypeCalc.detEff(oppotype[1], move3)) + ' * ' + str(TypeCalc.detEff(oppotype[2], move3)) + ' = ' + str(power3))
            if power1 >= power2 and power1 >= power3:
                return 0
            elif power2 >= power1 and power2 >= power3:
                return 1
            else:
                return 2

    else:  # 4 total moves
        move1 = moves[0].get_attribute("data-move")
        move2 = moves[1].get_attribute("data-move")
        move3 = moves[2].get_attribute("data-move")
        move4 = moves[3].get_attribute("data-move")

        stab1 = StabCalc.stab(mystab, move1)
        stab2 = StabCalc.stab(mystab, move2)
        stab3 = StabCalc.stab(mystab, move3)
        stab4 = StabCalc.stab(mystab, move4)

        if len(oppotype) == 2:
            power1 = stab1 * PokemonMovePower.basePower(move1) * TypeCalc.detEff(oppotype[1], move1)
            power2 = stab2 * PokemonMovePower.basePower(move2) * TypeCalc.detEff(oppotype[1], move2)
            power3 = stab3 * PokemonMovePower.basePower(move3) * TypeCalc.detEff(oppotype[1], move3)
            power4 = stab4 * PokemonMovePower.basePower(move4) * TypeCalc.detEff(oppotype[1], move4)
            print(move1 + ': Power = ' + str(stab1) + ' * ' + str(PokemonMovePower.basePower(move1)) + ' * ' + str(TypeCalc.detEff(oppotype[1], move1)) + ' = ' + str(power1))
            print(move2 + ': Power = ' + str(stab2) + ' * ' + str(PokemonMovePower.basePower(move2)) + ' * ' + str(TypeCalc.detEff(oppotype[1], move2)) + ' = ' + str(power2))
            print(move3 + ': Power = ' + str(stab3) + ' * ' + str(PokemonMovePower.basePower(move3)) + ' * ' + str(TypeCalc.detEff(oppotype[1], move3)) + ' = ' + str(power3))
            print(move4 + ': Power = ' + str(stab4) + ' * ' + str(PokemonMovePower.basePower(move4)) + ' * ' + str(TypeCalc.detEff(oppotype[1], move4)) + ' = ' + str(power4))
            if power1 >= power2 and power1 >= power3 and power1 >= power4:
                return 0
            elif power2 >= power1 and power2 >= power3 and power2 >= power4:
                return 1
            elif power3 >= power1 and power3 >= power2 and power3 >= power4:
                return 2
            else:
                return 3
        else:
            power1 = stab1 * PokemonMovePower.basePower(move1) * TypeCalc.detEff(oppotype[1], move1) * TypeCalc.detEff(oppotype[2], move1)
            power2 = stab2 * PokemonMovePower.basePower(move2) * TypeCalc.detEff(oppotype[1], move2) * TypeCalc.detEff(oppotype[2], move2)
            power3 = stab3 * PokemonMovePower.basePower(move3) * TypeCalc.detEff(oppotype[1], move3) * TypeCalc.detEff(oppotype[2], move3)
            power4 = stab4 * PokemonMovePower.basePower(move4) * TypeCalc.detEff(oppotype[1], move4) * TypeCalc.detEff(oppotype[2], move4)
            print(move1 + ': Power = ' + str(stab1) + ' * ' + str(PokemonMovePower.basePower(move1)) + ' * ' + str(TypeCalc.detEff(oppotype[1], move1)) + ' * ' + str(TypeCalc.detEff(oppotype[2], move1)) + ' = ' + str(power1))
            print(move2 + ': Power = ' + str(stab2) + ' * ' + str(PokemonMovePower.basePower(move2)) + ' * ' + str(TypeCalc.detEff(oppotype[1], move2)) + ' * ' + str(TypeCalc.detEff(oppotype[2], move2)) + ' = ' + str(power2))
            print(move3 + ': Power = ' + str(stab3) + ' * ' + str(PokemonMovePower.basePower(move3)) + ' * ' + str(TypeCalc.detEff(oppotype[1], move3)) + ' * ' + str(TypeCalc.detEff(oppotype[2], move3)) + ' = ' + str(power3))
            print(move4 + ': Power = ' + str(stab4) + ' * ' + str(PokemonMovePower.basePower(move4)) + ' * ' + str(TypeCalc.detEff(oppotype[1], move4)) + ' * ' + str(TypeCalc.detEff(oppotype[2], move4)) + ' = ' + str(power4))
            if power1 >= power2 and power1 >= power3 and power1 >= power4:
                return 0
            elif power2 >= power1 and power2 >= power3 and power2 >= power4:
                return 1
            elif power3 >= power1 and power3 >= power2 and power3 >= power4:
                return 2
            else:
                return 3
