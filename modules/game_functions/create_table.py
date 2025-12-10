def create_table( cells: list[ list[ str ] ] ) -> str:
    return f"""
 { cells[ 0 ][ 0 ] } | { cells[ 0 ][ 1 ] } | { cells[ 0 ][ 2 ] }
-----------
 { cells[ 1 ][ 0 ] } | { cells[ 1 ][ 1 ] } | { cells[ 1 ][ 2 ] }
-----------
 { cells[ 2 ][ 0 ] } | { cells[ 2 ][ 1 ] } | { cells[ 2 ][ 2 ] }
"""
