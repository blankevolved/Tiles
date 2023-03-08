# Grid

## Defining a grid
This is how you define a grid
```py
# import NULL tile and Grid
from tiles import Grid, NULL

my_grid = Grid(x=10, y=10, background_tile=NULL)
```

## create
You can create with the 'Grid.create()' method
```py
# import Grid
from tiles import Grid

# print grid out
print(Grid.create(x=5, y=5, show_nums=False))
```
Output
```py
◻ ◻ ◻ ◻ ◻ 
◻ ◻ ◻ ◻ ◻
◻ ◻ ◻ ◻ ◻
◻ ◻ ◻ ◻ ◻
◻ ◻ ◻ ◻ ◻
```
With 'show_nums' set to true, it will show numbers
```py
# import Grid
from tiles import Grid

# print grid w nums
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

## draw_tile
You can use this method to draw a tile to a pos on the grid
```py
# import Grid, NULL and FILLED tiles
from tiles import Grid, NULL, FILLED, F_RESET

# make new grid
my_grid = Grid(10, 10, NULL)

# change tile
my_grid.draw_tile(0, 0, FILLED, fore_color=F_RESET)

# print out
print(my_grid.create())

```

Output:
```py
   0  1 2  3 4  5 6  7 8  9  
0  ◼ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻  
1  ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻  
2  ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻  
3  ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻  
4  ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻  
5  ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻  
6  ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻  
7  ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻  
8  ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻  
9  ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻  
```

## draw_entity
You can use this method to draw an entity to the grid
```py
# import Grid, NULL and FILLED tiles
from tiles import Grid, NULL, FILLED, F_RESET, Entity

# make new grid
my_grid = Grid(10, 10, NULL)

# new entity
my_entity = Entity(tile=FILLED, grid=my_grid, fore_color=F_RESET)

# change tile
my_grid.draw_entity(0, 0, entity=my_entity)

# print out
print(my_grid.create())

```

Output:
```py
   0  1 2  3 4  5 6  7 8  9  
0  ◼ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻  
1  ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻  
2  ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻  
3  ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻  
4  ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻  
5  ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻  
6  ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻  
7  ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻  
8  ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻  
9  ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻  
```