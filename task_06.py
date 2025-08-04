class WrongNumberOfPlayersError(Exception):
    pass


class NoSuchStrategyError(Exception):
    pass


def rps_game_winner(list):
    if len(list) != 2:
        raise WrongNumberOfPlayersError

    newdict = dict(list)
    rules = {"R": "S", "P": "R", "S": "P"}

    for move in newdict.values():
        if move not in {"R", "P", "S"}:
            raise NoSuchStrategyError

    (player1, move1), (player2, move2) = newdict.items() # i added this because from what i understand the player name can be changed 

    if move1 == move2:
        return f"{player1} {move1}"
    elif rules[move1] == move2:
        return f"{player1} {move1}"
    else:
        return f"{player2} {move2}"




print(rps_game_winner([['player1', 'P'], ['player2', 'S']]))

print(rps_game_winner([['ss', 'P'], ['hh', 'P']]))
