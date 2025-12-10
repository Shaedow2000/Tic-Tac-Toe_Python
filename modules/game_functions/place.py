def place_symbol( symbol: str, placement: int, table: str ) -> str:
    new_table: str = table.replace( f'{ placement }', symbol )

    return new_table
