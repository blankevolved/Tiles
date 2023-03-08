# Variables
Heres a full list of all variables you can import and there values
```py
# Version
VERSION = 1.2

# Colors
F_RESET     = Fore.RESET
F_WHITE     = Fore.WHITE
F_BLACK     = Fore.BLACK
F_RED       = Fore.RED
F_BLUE      = Fore.BLUE
F_GREEN     = Fore.GREEN
F_YELLOW    = Fore.YELLOW
F_CYAN      = Fore.CYAN
F_MAGENTA   = Fore.MAGENTA

B_RESET = Back.RESET

# Game loop
START_TIME = time.time()

# the delay before the screen refreshes 
# when Entity.move_loop is called.
tick_speed = .3

# Error messages (You wont need)
DEP_ERROR = Error.create('This function is depreciated and will be removed in a later version')
MOVE_ERROR = Error.create('You cannot move that way')

# Tiles
NULL = Tile('null', '◻')
FILLED = Tile('filled', '◼')
```