from modules.game_functions.check_win import check_win
from modules.game_functions.create_table import create_table
from modules.game_functions.place import place_symbol
from data.global_vars import players_symbol as symbols
from modules.game_functions.switch import switch
from modules.methods.methods import clear
from modules.game_functions.clear_board import clear_board

def play( table: str, cells: list[ list[ str ] ] ) -> None:
    print( table )
    current_player: int = 0

    cells = clear_board()

    while True:
        sqr: str | int = input( '=> Enter number of the square: ' ).replace( ' ', '' )

        if not sqr.isdigit():
            if sqr.lower() == 'c':
                clear()
                print( table )
                continue
            else:
                print( '!> Enter a number that is in the table.' )
                continue
        else:
            sqr = int( sqr )
            if sqr >= 10 and sqr == 0:
                print( '!> Enter a number that is in the table.' )
                continue
            else:
                placement: list = place_symbol( symbols[ current_player ], sqr, cells )
                if placement[ 0 ]:
                    cells = placement[ 1 ]
                    table = create_table( cells )
                    print( table )

                    if check_win( cells ):
                        print( f'--> { symbols[ current_player ] } Won !!!' )
                        break
                    else:
                        current_player = switch( current_player )
                        continue
                else:
                    print( '!> Enter an empty cell.' )
                    continue
