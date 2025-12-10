def place_symbol( symbol: str, placement: int, table: str ) -> list:
    if not str( placement ) in table:
        return [ False, table ]
    else:
        return [ True, table.replace( f'{ placement }', symbol ) ] 
