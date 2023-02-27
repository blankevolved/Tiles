# Tiles

## Use Case
This module is used for creating tile sets where you can place custom tiles.

This can be used for map making, or just to create a grid.

## How to use

### Grid

#### create
You can create with the 'Grid.create()' method
```py
from tiles import Grid

Grid.create(x, y, show_nums)
```
This is how it looks with actual values
```py
from tiles import Grid

print(Grid.create(5, 5, False))
```
Output
```py
◻ ◻ ◻ ◻ ◻ 
◻ ◻ ◻ ◻ ◻
◻ ◻ ◻ ◻ ◻
◻ ◻ ◻ ◻ ◻
◻ ◻ ◻ ◻ ◻
```
With 'show_nums' set to true
```py
from tiles import Grid

print(Grid.create(5, 5, True))
```
Output
```py
  0  1 2  3 4 
0 ◻ ◻ ◻ ◻ ◻
1 ◻ ◻ ◻ ◻ ◻
2 ◻ ◻ ◻ ◻ ◻
3 ◻ ◻ ◻ ◻ ◻
4 ◻ ◻ ◻ ◻ ◻
```
### Tile

#### list
You can access the tile list by using the variable 'Tile.list'
```py
from tiles import Tile

Tile.list
```
Print it
```py
from tiles import Tile

print(Tile.list)
```
Output
```py
{'null': '◻', 'filled': '◼'}
```
#### create
You can create a new icon with the 'Tile.create()' method
```py
from tiles import Tile

Tile.create(name, icon)
```
Example
```py
from tiles import Tile

Tile.create('new', '!')
```
Once you call this method your new tile will be saved to the 'tiles.json' file, which looks like this
```json
{
    "null": "◻",
    "filled": "◼",
    "new": "!"
}
```
The 'Tile.list' variable will be updated as you create more variables
```py
from tiles import Tile

print(Tile.list)
```
Output
```py
{'null': '◻', 'filled': '◼','new': '!'}
```
#### remove
You can remove a tile from the 'tiles.json' file with the 'Tile.remove()' method
```py
from tiles import Tile

Tile.remove('hi')
```
Normal 'tiles.json'
```json
{
    "null": "◻",
    "filled": "◼",
    "hi": "!"
}
```
Updated 'tiles.json'
```json
{
    "null": "◻",
    "filled": "◼"
}
```
You cannot remove the 'null' or 'filled' icons with the 'Tile.remove()' method
### Color
#### fore
Use the 'fore' variable to access foreground colors (text changing colors)
```py
from tiles import Color

print(Color.fore)

print(Color.fore['red'] + 'hi')
```
Output 
```py
{'reset': '\x1b[39m', 'white': '\x1b[37m', 'red': '\x1b[31m', 'blue': '\x1b[34m'}

hi
# the 'hi' will show up red, but since this it github it will not
```
#### back
Use the 'back' variable to access foreground colors (background changing colors)
```py
from tiles import Color

print(Color.back)

print(Color.back['red'] + 'hi')
```
Output 
```py
{'reset': '\x1b[49m', 'white': '\x1b[47m', 'red': '\x1b[41m', 'blue': '\x1b[44m'}

hi
# the 'hi's background will show up red, but since this it github it will not
```