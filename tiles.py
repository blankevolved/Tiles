from colorama import Fore, Back
from mods.JSave.jsave import save_to_file, load_from_file
import os
import time

try:
    from clear import clear
except:
    os.system('pip install clear')
finally:
    from clear import clear

try:
    import keyboard
except:
    os.system('pip install keyboard')
finally:
    import keyboard

try:
    from deprecation import deprecated
except:
    os.system('pip install deprecation')
finally:
    from deprecation import deprecated


class Error:
    def create(message):
        return f"{F_RED}ERROR: {message}{F_RESET}"


class Tile:
    list = {}
    def __init__(self, name, icon):
        self.name = name
        self.icon = icon
        Tile.list[name] = icon
    def __repr__(self) -> str:
        return self.icon


class Grid:
    def __init__(self, x:int, y:int, background_tile:Tile):
        self.x = x
        self.y = y
        self.x_range = range(0, x)
        self.y_range = range(0, y)
        self.cords = {}
        self.background_tile = background_tile

        for xr in self.x_range:
            for yr in self.y_range:
                self.cords[xr, yr] = {'tile':background_tile,
                                'fore_color':F_RESET,
                                'back_color':B_RESET}

    def create(self, show_nums:bool=False):

        if show_nums == True:
            output = '   '
            for xr in range(0, self.x):
                if self.x <= 10:
                    output = output + f'{xr} '
                else:
                    output = f'   0 - {self.x - 1}'
            output = output + '\n'
        else:
            output = ''
        
        row = ''
        row_amt = 0
        for yr in self.y_range:
            for xr in self.x_range:
                
                if row_amt < self.x:
                    row_amt = row_amt + 1
                    row = row + f"{self.cords[xr, yr]['fore_color']}{self.cords[xr, yr]['back_color']}{self.cords[xr, yr]['tile']} "
                    row = row + f"{F_RESET}{B_RESET}"
                if row_amt == self.x:
                    if show_nums == True:
                        if yr <= 9:
                            output = output + str(yr) + '  ' + row + '\n'
                        else:
                            output = output + str(yr) + ' ' + row + '\n'
                    else:
                        output = output + row + '\n'
                    row = ''
                    row_amt = 0
        

        return output
    
    def change_tile(self, x:int, y:int, new_tile_name:str):
        try:
            self.cords[x, y]['tile'] = new_tile_name
        except KeyError:
            print(Error.create(f"The ({x}, {y}) pair doesn't exist"))

class Entity:
    def __init__(self, tile:Tile, grid:Grid, x:int, y:int):
        self.tile = tile
        self.grid = grid
        self.x = x
        self.y = y
        grid.cords[x, y]['tile'] = tile
    def move(self, right=False, left=False, up=False, down=False):
        if right == True:
            plus_or_minus = '+'
            opp_plus_or_minus = '-'
            try:
                self.grid.cords[eval(f'{self.x} + {plus_or_minus} + 1'), self.y]['tile'] = self.tile
                self.x = self.x + 1
                self.grid.cords[eval(f'{self.x} + {opp_plus_or_minus} + 1'), self.y]['tile'] = self.grid.background_tile
            except:
                print(MOVE_ERROR)

        if left == True:
            plus_or_minus = '-'
            opp_plus_or_minus = '+'
            try:
                self.grid.cords[eval(f'{self.x} + {plus_or_minus} + 1'), self.y]['tile'] = self.tile
                self.x = eval(f'{self.x} + {plus_or_minus} + 1')
                self.grid.cords[eval(f'{self.x} + {opp_plus_or_minus} + 1'), self.y]['tile'] = self.grid.background_tile
            except:
                print(MOVE_ERROR)
        
        if up == True:
            plus_or_minus = '-'
            opp_plus_or_minus = '+'
            try:
                self.grid.cords[self.x, eval(f'{self.y} + {plus_or_minus} + 1')]['tile'] = self.tile
                self.y = eval(f'{self.y} + {plus_or_minus} + 1')
                self.grid.cords[self.x, eval(f'{self.y} + {opp_plus_or_minus} + 1')]['tile'] = self.grid.background_tile
            except:
                print(MOVE_ERROR)
        
        if down == True:
            plus_or_minus = '+'
            opp_plus_or_minus = '-'
            try:
                self.grid.cords[self.x, eval(f'{self.y} + {plus_or_minus} + 1')]['tile'] = self.tile
                self.y = eval(f'{self.y} + {plus_or_minus} + 1')
                self.grid.cords[self.x, eval(f'{self.y} + {opp_plus_or_minus} + 1')]['tile'] = self.grid.background_tile
            except:
                print(MOVE_ERROR)

    def move_loop(self):
        if keyboard.is_pressed("right"):
            self.move(right=True)
        if keyboard.is_pressed("left"):
            self.move(left=True)
        if keyboard.is_pressed("up"):
            self.move(up=True)
        if keyboard.is_pressed("down"):
            self.move(down=True)
            
        time.sleep(tick_speed - ((time.time() - START_TIME) % tick_speed))

        
        
# Version
VERSION = 1.1

# Colors
F_RESET = Fore.RESET
F_RED = Fore.RED

B_RESET = Back.RESET

# Error messages (You wont need)
DEP_ERROR = Error.create('This function is depreciated and will be removed in a later version')
MOVE_ERROR = Error.create('You cannot move that way')

# Tiles
NULL = Tile('null', '◻')
FILLED = Tile('filled', '◼')

# Game loop
START_TIME = time.time()
# the delay before the screen refreshes 
# when Entity.move_loop is called.
tick_speed = .3 

