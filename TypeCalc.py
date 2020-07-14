import PokemonMoveTyping

def detEff(oppoType, move):
    # returns the effectiveness value of a move on a pokemon
    # 0 = not effective
    # 0.5 = not very effective
    # 1 = effective
    # 2 = super effective

    eff = 1

    if oppoType == 'Normal':
        if PokemonMoveTyping.typing(move) == 'Ghost':
            eff = 0
    elif oppoType == 'Fire':
        if PokemonMoveTyping.typing(move) == 'Water' or PokemonMoveTyping.typing(move) == 'Rock' \
                or PokemonMoveTyping.typing(move) == 'Ground':
            eff = 2
        elif PokemonMoveTyping.typing(move) == 'Fire' or PokemonMoveTyping.typing(move) == 'Bug' \
                or PokemonMoveTyping.typing(move) == 'Grass' or PokemonMoveTyping.typing(move) == 'Steel' \
                or PokemonMoveTyping.typing(move) == 'Fairy' or PokemonMoveTyping.typing(move) == 'Ice':
            eff = 0.5
    elif oppoType == 'Water':
        if PokemonMoveTyping.typing(move) == 'Electric' or PokemonMoveTyping.typing(move) == 'Grass':
            eff = 2
        elif PokemonMoveTyping.typing(move) == 'Fire' or PokemonMoveTyping.typing(move) == 'Water' \
                or PokemonMoveTyping.typing(move) == 'Ice' or PokemonMoveTyping.typing(move) == 'Steel':
            eff = 0.5
    elif oppoType == 'Grass':
        if PokemonMoveTyping.typing(move) == 'Fire' or PokemonMoveTyping.typing(move) == 'Bug' \
                or PokemonMoveTyping.typing(move) == 'Flying' or PokemonMoveTyping.typing(move) == 'Ice' \
                or PokemonMoveTyping.typing(move) == 'Poison':
            eff = 2
        elif PokemonMoveTyping.typing(move) == 'Grass' or PokemonMoveTyping.typing(move) == 'Water' \
                or PokemonMoveTyping.typing(move) == 'Electric' or PokemonMoveTyping.typing(move) == 'Ground':
            eff = 0.5
    elif oppoType == 'Electric':
        if PokemonMoveTyping.typing(move) == 'Ground':
            eff = 2
        elif PokemonMoveTyping.typing(move) == 'Flying' or PokemonMoveTyping.typing(move) == 'Electric' \
                or PokemonMoveTyping.typing(move) == 'Steel':
            eff = 0.5
    elif oppoType == 'Ice':
        if PokemonMoveTyping.typing(move) == 'Fire' or PokemonMoveTyping.typing(move) == 'Fighting' \
                or PokemonMoveTyping.typing(move) == 'Rock' or PokemonMoveTyping.typing(move) == 'Steel':
            eff = 2
        elif PokemonMoveTyping.typing(move) == 'Ice':
            eff = 0.5
    elif oppoType == 'Fighting':
        if PokemonMoveTyping.typing(move) == 'Psychic' or PokemonMoveTyping.typing(move) == 'Fairy' \
                or PokemonMoveTyping.typing(move) == 'Flying':
            eff = 2
        elif PokemonMoveTyping.typing(move) == 'Dark' or PokemonMoveTyping.typing(move) == 'Bug' \
                or PokemonMoveTyping.typing(move) == 'Rock':
            eff = 0.5
    elif oppoType == 'Poison':
        if PokemonMoveTyping.typing(move) == 'Ground' or PokemonMoveTyping.typing(move) == 'Psychic':
            eff = 2
        elif PokemonMoveTyping.typing(move) == 'Grass' or PokemonMoveTyping.typing(move) == 'Poison' \
                or PokemonMoveTyping.typing(move) == 'Fairy' or PokemonMoveTyping.typing(move) == 'Fighting' \
                or PokemonMoveTyping.typing(move) == 'Bug':
            eff = 0.5
    elif oppoType == 'Ground':
        if PokemonMoveTyping.typing(move) == 'Ice' or PokemonMoveTyping.typing(move) == 'Water' \
                or PokemonMoveTyping.typing(move) == 'Grass':
            eff = 2
        elif PokemonMoveTyping.typing(move) == 'Rock' or PokemonMoveTyping.typing(move) == 'Poison':
            eff = 0.5
        elif PokemonMoveTyping.typing(move) == 'Electric':
            eff = 0
    elif oppoType == 'Flying':
        if PokemonMoveTyping.typing(move) == 'Electric' or PokemonMoveTyping.typing(move) == 'Ice' \
                or PokemonMoveTyping.typing(move) == 'Flying':
            eff = 2
        elif PokemonMoveTyping.typing(move) == 'Grass' or PokemonMoveTyping.typing(move) == 'Bug' \
                or PokemonMoveTyping.typing(move) == 'Fighting':
            eff = 0.5
        elif PokemonMoveTyping.typing(move) == 'Ground':
            eff = 0
    elif oppoType == 'Psychic':
        if PokemonMoveTyping.typing(move) == 'Ghost' or PokemonMoveTyping.typing(move) == 'Bug' \
                or PokemonMoveTyping.typing(move) == 'Dark':
            eff = 2
        elif PokemonMoveTyping.typing(move) == 'Fighting' or PokemonMoveTyping.typing(move) == 'Psychic':
            eff = 0.5
    elif oppoType == 'Bug':
        if PokemonMoveTyping.typing(move) == 'Fire' or PokemonMoveTyping.typing(move) == 'Flying' \
                or PokemonMoveTyping.typing(move) == 'Rock':
            eff = 2
        elif PokemonMoveTyping.typing(move) == 'Ground' or PokemonMoveTyping.typing(move) == 'Grass' \
                or PokemonMoveTyping.typing(move) == 'Fighting':
            eff = 0.5
    elif oppoType == 'Rock':
        if PokemonMoveTyping.typing(move) == 'Grass' or PokemonMoveTyping.typing(move) == 'Water' \
                or PokemonMoveTyping.typing(move) == 'Steel' or PokemonMoveTyping.typing(move) == 'Ground' \
                or PokemonMoveTyping.typing(move) == 'Fighting':
            eff = 2
        elif PokemonMoveTyping.typing(move) == 'Normal' or PokemonMoveTyping.typing(move) == 'Fire' \
                or PokemonMoveTyping.typing(move) == 'Flying' or PokemonMoveTyping.typing(move) == 'Poison':
            eff = 0.5
    elif oppoType == 'Ghost':
        if PokemonMoveTyping.typing(move) == 'Ghost' or PokemonMoveTyping.typing(move) == 'Dark':
            eff = 2
        elif PokemonMoveTyping.typing(move) == 'Poison' or PokemonMoveTyping.typing(move) == 'Bug':
            eff = 0.5
        elif PokemonMoveTyping.typing(move) == 'Normal' or PokemonMoveTyping.typing(move) == 'Fighting':
            eff = 0
    elif oppoType == 'Dragon':
        if PokemonMoveTyping.typing(move) == 'Dragon' or PokemonMoveTyping.typing(move) == 'Ice' \
                or PokemonMoveTyping.typing(move) == 'Fairy':
            eff = 2
        elif PokemonMoveTyping.typing(move) == 'Fire' or PokemonMoveTyping.typing(move) == 'Water' \
                or PokemonMoveTyping.typing(move) == 'Grass' or PokemonMoveTyping.typing(move) == 'Electric':
            eff = 0.5
    elif oppoType == 'Dark':
        if PokemonMoveTyping.typing(move) == 'Fairy' or PokemonMoveTyping.typing(move) == 'Bug' \
                or PokemonMoveTyping.typing(move) == 'Fighting':
            eff = 2
        elif PokemonMoveTyping.typing(move) == 'Ghost' or PokemonMoveTyping.typing(move) == 'Dark':
            eff = 0.5
        elif PokemonMoveTyping.typing(move) == 'Psychic':
            eff = 0
    elif oppoType == 'Steel':
        if PokemonMoveTyping.typing(move) == 'Fire' or PokemonMoveTyping.typing(move) == 'Ground' \
                or PokemonMoveTyping.typing(move) == 'Fighting':
            eff = 2
        elif PokemonMoveTyping.typing(move) == 'Normal' or PokemonMoveTyping.typing(move) == 'Grass' \
                or PokemonMoveTyping.typing(move) == 'Flying' or PokemonMoveTyping.typing(move) == 'Rock' \
                or PokemonMoveTyping.typing(move) == 'Steel' or PokemonMoveTyping.typing(move) == 'Dragon' \
                or PokemonMoveTyping.typing(move) == 'Bug' or PokemonMoveTyping.typing(move) == 'Psychic' \
                or PokemonMoveTyping.typing(move) == 'Ice' or PokemonMoveTyping.typing(move) == 'Fairy':
            eff = 0.5
        elif PokemonMoveTyping.typing(move) == 'Poison':
            eff = 0
    elif oppoType == 'Fairy':
        if PokemonMoveTyping.typing(move) == 'Steel' or PokemonMoveTyping.typing(move) == 'Poison':
            eff = 2
        elif PokemonMoveTyping.typing(move) == 'Fighting' or PokemonMoveTyping.typing(move) == 'Bug' \
                or PokemonMoveTyping.typing(move) == 'Dark':
            eff = 0.5
        elif PokemonMoveTyping.typing(move) == 'Dragon':
            eff = 0

    return eff
