from modules.game_functions.place import place_symbol
from data.global_vars import players_symbol as symbols
from modules.methods.methods import clear

def start( table: str ) -> None:
    print( table )
    current_player: int = 0

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
                placement: list = place_symbol( symbols[ current_player ], sqr, table )
                if placement[ 0 ]:
                    table = placement[ 1 ]
                    print( table )
                else:
                    print( '!> Enter an empty cell.' )
                    continue
