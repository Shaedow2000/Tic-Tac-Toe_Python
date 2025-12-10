from modules.game_functions.place import place_symbol
from data.global_vars import players_symbol as symbols

def start( table: str ) -> None:
    print( table )
    current_player: int = 0

    while True:
        sqr: str | int = input( '=> Enter number of the square: ' ).replace( ' ', '' )

        if not sqr.isdigit():
            print( '!> Enter a number that is in the table.' )
            continue
        else:
            sqr = int( sqr )
            if sqr >= 10 and sqr == 0:
                print( '!> Enter a number that is in the table.' )
                continue
            else:
                table = place_symbol( symbols[ current_player ], sqr, table )
                print( table )
