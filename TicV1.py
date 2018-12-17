import os

game = []
gridsize = 3
total_moves = 0
num_players = 1
again = True
won = False


def check_winner(game_map):
    # Used to check each row for a winning line.

    for row in game_map:
        if row.count(row[0]) == len(row) and row[0] != 0:
            # We have a winner
            return True

    return False


def check_board(game_map, player):
    ''' Run through each row, column and diagonal and send to test for a
        winning line. '''
    
    alt_map = []
    
    # Start with the rows, no alteration required.
    if check_winner(game_map):
        return True
        

    # Now do columns.
    for column in range(len(game_map)):
        alt_map.append([row[column] for row in game_map])
    if check_winner(alt_map):
        return True

    # Now for diagonals, top to bottom first.
    alt_map = []
    for idx in range(len(game_map)):
        alt_map.append(game_map[idx][idx])
    if alt_map.count(alt_map[0]) == len(alt_map) and alt_map[0] != 0:
        return True

    # Now bottom to top.
    alt_map = []
    for col, row in enumerate(reversed(range(len(game_map)))):
        alt_map.append(game_map[row][col])
    if alt_map.count(alt_map[0]) == len(alt_map) and alt_map[0] != 0:
        return True

    return False

def player_move(game_map, player):
    # Asks the player where they would like to go.
    # Validates the move as well.

    valid = False
    r = '0 to ' + str(gridsize - 1) +': '

    print()
    print('Player: ' + str(player))
    print()
	
    while True:
        while not valid:
            srow = input('Which row would you like to select, ' + r)
            if srow.isnumeric():
                irow = int(srow)
                if irow >= 0 and irow < gridsize:
                    valid = True
            else:
                print('Invalid entry!')

        valid = False
        
        while not valid:
            scol = input('Which column would you like to select, ' + r)
            if scol.isnumeric():
                icol = int(scol)
                if icol >= 0 and icol < gridsize:
                    valid = True
            else:
                print('Invalid entry!')
                
        # Now we know where they want to go lets check its free.
        if game_map[irow][icol] == 0:
            print('You can go there')
            game_map[irow][icol] = player
            return game_map
        valid = False
        print('Sorry....Location taken.')
		

def draw_board(game_map):
    # Displays the game board on screen.

    _ = os.system('cls')
    tl = '    '
    print()
    for x in range(gridsize):
        tl += str(x) + '  '
    print(tl)

    for count, row in enumerate(game_map):
        print(str(count) + '  ' + str(row))
        
        
# Start of main loop
            
while again:
    again = True
    won = False
    total_moves = 0
    valid = False
	
    while not valid:
        x = input('How many columns would you like? 3 - 10: ')
        if x.isnumeric():
            if int(x) >= 3 and int(x) <= 10:
                gridsize = int(x)
                game = [[0 for row in range(gridsize)] for col in range(gridsize)]
                valid = True
    draw_board(game)
	
    while not won:
        game = player_move(game, num_players)  
        draw_board(game)
        won = check_board(game, num_players)
        if won:
            print()
            print('Congratulations player ' + str(num_players) + ' you have won!!!')
            opt = input('Would you like to play again? y or n: ')
            if opt.lower() != 'y':
                again = False
                
        # Change player before next move and increment move counter.
        if num_players == 1:
            num_players = 2
        else:
            num_players = 1
        total_moves += 1
        if total_moves == gridsize * gridsize:
            print()
            print('Nobody won this game...')
            opt = input('Would you like to play again? y or n: ')
            if opt.lower() != 'y':
                again = False
