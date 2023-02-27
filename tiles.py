from colorama import Fore, Back
from mods.JSave.jsave import save_to_file, load_from_file

VERSION = 1.0


class Color:
    def hex_to_rgb(value):
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
    fore = {}
    back = {}
    try:
        fore = load_from_file('colors.json')['fore']
    except:
        fore = {
            'reset':    Fore.RESET,
            'white':    Fore.WHITE,
            'red':      Fore.RED,
            'blue':     Fore.BLUE
        }
    try:
        back = load_from_file('colors.json')['back']
    except:
        back = {
            'reset':    Back.RESET,
            'white':    Back.WHITE,
            'red':      Back.RED,
            'blue':     Back.BLUE
        }

class Tile:
    
    list = {}
    try:
        list = load_from_file('tiles.json')
    except:
        list = {
            'null':'◻',
            'filled':'◼'
        }
    def create(name:str, icon:str):
        Tile.list[name] = icon
        save_to_file('tiles.json', Tile.list)

    def remove(name:str):
        if name != 'null' or name != 'filled':
            Tile.list.pop(name)
            save_to_file('tiles.json', Tile.list)
        else:
            print('cannot remove ' + name)


class Grid:
    
    def create(x:int, y:int, show_nums:bool=False):
        x_range = range(0, x)
        y_range = range(0, y)
        cords = {}

        for xr in x_range:
            for yr in y_range:
                cords[xr, yr] = {'tile':Tile.list['null'],
                                'fore_color':Color.fore['reset'],
                                'back_color':Color.back['reset']}
        if show_nums == True:
            output = '  '
            for xr in range(0, x):
                if x <= 10:
                    output = output + f'{xr} '
                else:
                    output = f'  0 - {x - 1}'
            output = output + '\n'
        else:
            output = ''
        
        row = ''
        row_amt = 0
        for yr in y_range:
            for xr in x_range:
                
                if row_amt < x:
                    row_amt = row_amt + 1
                    row = row + f"{cords[xr, yr]['fore_color']}{cords[xr, yr]['back_color']}{cords[xr, yr]['tile']} "
                    row = row + f"{Color.fore['reset']}{Color.back['reset']}"
                if row_amt == x:
                    if show_nums == True:
                        output = output + str(yr) + ' ' + row + '\n'
                    else:
                        output = output + row + '\n'
                    row = ''
                    row_amt = 0
        

        return output
