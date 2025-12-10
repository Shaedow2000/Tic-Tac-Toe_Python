def place_symbol( symbol: str, placement: int, cells: list[ list[ str ] ] ) -> list:
    index: list[ int ] = []

    for i, row in enumerate( cells ):
        if str( placement ) in row:
            index.append( i )
            index.append( row.index( str( placement ) ) )

            cells[ index[ 0 ] ][ index[ 1 ] ] = symbol
            return [ True, cells ] 
        
    return [ False, cells ] 
