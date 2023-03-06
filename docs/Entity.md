# Entity

## Define a new Entity
Define a new entity like this
```py
# imports
from tiles import Grid, Entity, FILLED, NULL

# define grid
my_grid = Grid(10, 10, NULL)

# define entity
my_entity = Entity(tile=FILLED, grid=my_grid, x=0, y= 0)
```

## move
You can use this method to move the player in a direction
```py
# imports
from tiles import Grid, Entity, FILLED, NULL

# define grid
my_grid = Grid(10, 10, NULL)

# define entity
my_entity = Entity(tile=FILLED, grid=my_grid, x=0, y= 0)

my_entity.move(right=True)

print(my_grid.create(show_nums=True))
```
Output:
```
   0 1 2 3 4 5 6 7 8 9
0  ◻ ◼ ◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻
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


## move_loop
This starts the player movement loop
```py
# imports
from tiles import Grid, Entity, FILLED, NULL, clear

# define grid
grid = Grid(10, 10, NULL)

# define player
player = Entity(FILLED, grid, 0, 0)

while True:
    # clear screen
    clear()
    # prints grid
    print(grid.create(show_nums=True))
    # allows you to use arrow keys to move
    player.move_loop()
```