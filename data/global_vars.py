menu: str = '\t1: play | c: clear screen | q: quit'

cells: list[ list[ str ] ] = [
    [ '1', '2', '3' ],
    [ '4', '5', '6' ],
    [ '7', '8', '9' ]
]

table: str = f"""
 { cells[ 0 ][ 0 ] } | { cells[ 0 ][ 1 ] } | { cells[ 0 ][ 2 ] }
-----------
 { cells[ 1 ][ 0 ] } | { cells[ 1 ][ 1 ] } | { cells[ 1 ][ 2 ] }
-----------
 { cells[ 2 ][ 0 ] } | { cells[ 2 ][ 1 ] } | { cells[ 2 ][ 2 ] }
"""

players_symbol: list[ str ] = [ 'X', 'O' ]

winning_positions: list[ list[ str ] ] = [
    [ '1', '2', '3' ],
    [ '4', '5', '6' ],
    [ '7', '8', '9' ],
    [ '1', '4', '7' ],
    [ '2', '5', '8' ],
    [ '3', '6', '9' ],
    [ '1', '5', '9' ],
    [ '3', '5', '7' ]
]
