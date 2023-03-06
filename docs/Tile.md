# Tile

## Defining a tile
You can create a new tile like this
```py
from tiles import Tile

# new tile
# Tile(name, icon)
Tile('hello', '!')
```
This new tile will appear in the 'Tile.list' variable

## list
You can access the tile list by using the variable 'Tile.list'

```py
# import Tile
from tiles import Tile

# print Tile.list
print(Tile.list)
```
Output
```
{'null': '◻', 'filled': '◼'}
```