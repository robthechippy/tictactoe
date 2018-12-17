#import numpy

#Tempory game grid size, to be manually entered
gridsize = 3

game = [[0 for row in range(gridsize)] for col in range(gridsize)]


def check_winner(game_map):
    # Used to check each row for a winning line.

    print(game_map)
    for row in game_map:
        #print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            # We have a winner
            return True

    return False


def check_board(game_map, player):
    ''' Run through each row, column and diagonal and send to test for a
        winning line. '''
    won = False
    alt_map = []
    
    # Start with the rows, no alteration required.
    if check_winner(game_map):
        print('Winner')
        won = True

    if not won:
        # Now do columns.
        for column in range(len(game_map)):
            alt_map.append([row[column] for row in game_map])
        if check_winner(alt_map):
            print('Winner')
            won = True

    if not won:
        # Now for diagonals, top to bottom first.
        alt_map = []
        for idx in range(len(game_map)):
            alt_map.append(game_map[idx][idx])
        print(alt_map)
        if alt_map.count(alt_map[0]) == len(alt_map) and alt_map[0] != 0:
            print('winner')
            won = True

        else:
            # Now bottom to top.
            alt_map = []
            for col, row in enumerate(reversed(range(len(game_map)))):
                alt_map.append(game_map[row][col])
            print(alt_map)
            if alt_map.count(alt_map[0]) == len(alt_map) and alt_map[0] != 0:
                print('winner')
                won = True


def player_move(game_map, player):
    # Asks the player where they would like to go.
    # Validates the move as well.

    valid = False
    r = '0 to ' + str(gridsize - 1) +': '

    while True:
        while not valid:
            srow = input('Which row would yoou like to select, ' + r)
            if srow.isnumeric():
                irow = int(srow)
                if irow >= 0 and irow < gridsize:
                    valid = True
            else:
                 print('Invalid entry!')
                 
        valid = False
        
        while not valid:
            scol = input('Which column would yoou like to select, ' + r)
            if scol.isnumeric():
                icol = int(scol)
                if icol >= 0 and icol < gridsize:
                    valid = True
                    print('Should be valid')
            else:
                print('Invalid entry!')
                
        # Now we know where they want to go lets check its free.
        if game_map[irow][icol] == 0:
            print('Can go here')
            game_map[irow][icol] = player
            return game_map

              
game = player_move(game, 1)  
check_board(game, 1)
