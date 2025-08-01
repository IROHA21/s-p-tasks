def rps_game_winner(list):
    if not list :
        pass

    for elem in list :
        print(elem)
        print(type(elem))


    return len(list)



print(rps_game_winner([['player1','P'],['player2','S']]))