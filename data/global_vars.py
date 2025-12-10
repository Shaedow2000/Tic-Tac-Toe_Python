menu: str = '\t1: play | c: clear screen | q: quit'

table: str = """
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
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
