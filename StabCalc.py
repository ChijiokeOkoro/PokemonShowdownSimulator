import PokemonMoveTyping

def stab(myType, move):
    # checks to see if pokemon typing and moves match for stab calculation
    # 1.5 = STAB
    # 1 = non-STAB

    if len(myType) == 2:
        if PokemonMoveTyping.typing(move) == myType[1]:
            stabboost = 1.5
        else:
            stabboost = 1
    else:
        if PokemonMoveTyping.typing(move) == myType[1] or PokemonMoveTyping.typing(move) == myType[2]:
            stabboost = 1.5
        else:
            stabboost = 1

    return stabboost