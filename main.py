#!/usr/bin/env python3

import sys
import os

from data.global_vars import *
from modules.game_functions.play import start
from modules.methods import clear 


def main() -> None:
    clear()
    print( menu )

    while True:
        choice: str = input( '==> ' ).replace( ' ', '' ).lower()


        if choice == 'q':
            print( '--> Exiting...' )
            break
        elif choice == 'c':
            clear()
            print( menu )
            continue
        elif choice == '1':
            clear()
            start( table ) 
        elif choice == '':
            continue
        else:
            print( f'!> Unknown command: { choice }' )
            continue

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print( '\n--> Exiting...' )
        sys.exit( 1 )
