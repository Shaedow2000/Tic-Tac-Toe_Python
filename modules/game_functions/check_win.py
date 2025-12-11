def check_win( cells: list[ list[ str ] ] ) -> bool:
    row1: list[ str ] = cells[ 0 ]
    row2: list[ str ] = cells[ 1 ]
    row3: list[ str ] = cells[ 2 ]

    column1: list[ str ] = [ cells[ 0 ][ 0 ], cells[ 1 ][ 0 ], cells[ 2 ][ 0 ] ]
    column2: list[ str ] = [ cells[ 0 ][ 1 ], cells[ 1 ][ 1 ], cells[ 2 ][ 1 ] ]
    column3: list[ str ] = [ cells[ 0 ][ 2 ], cells[ 1 ][ 2 ], cells[ 2 ][ 2 ] ]

    diagonal1: list[ str ] = [ cells[ 0 ][ 0 ], cells[ 1 ][ 1 ], cells[ 2 ][ 2 ] ]
    diagonal2: list[ str ] = [ cells[ 0 ][ 2 ], cells[ 1 ][ 1 ], cells[ 2 ][ 0 ] ]

    # the first if statement, checks the rows.
    # the second one, checks the columns.
    # the third one, checks the diagonals.
    # the last one just returns False after checking every cell.
    
    if ( row1[ 0 ] == row1[ 1 ] and row1[ 0 ] == row1[ 2 ] and row1[ 1 ] == row1[ 2 ] ) or ( row2[ 0 ] == row2[ 1 ] and row2[ 0 ] == row2[ 2 ] and row2[ 1 ] == row2[ 2 ] ) or ( row3[ 0 ] == row3[ 1 ] and row3[ 0 ] == row3[ 2 ] and row3[ 1 ] == row3[ 2 ] ):
        return True
    elif ( column1[ 0 ] == column1[ 1 ] and column1[ 0 ] == column1[ 2 ] and column1[ 1 ] == column1[ 2 ] ) or ( column2[ 0 ] == column2[ 1 ] and column2[ 0 ] == column2[ 2 ] and column2[ 1 ] == column2[ 2 ] ) or ( column3[ 0 ] == column3[ 1 ] and column3[ 0 ] == column3[ 2 ] and column3[ 1 ] == column3[ 2 ] ):
        return True
    elif ( diagonal1[ 0 ] == diagonal1[ 1 ] and diagonal1[ 0 ] == diagonal1[ 2 ] and diagonal1[ 1 ] == diagonal1[ 2 ] ) or ( diagonal2[ 0 ] == diagonal2[ 1 ] and diagonal2[ 0 ] == diagonal2[ 2 ] and diagonal2[ 1 ] == diagonal2[ 2 ] ):
        return True
    else: 
        return False
