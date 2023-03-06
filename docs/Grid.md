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

## change_tile
You can use this method to change a specified tile
```py
# import Grid, NULL and FILLED tiles
from tiles import Grid, NULL, FILLED

# make new grid
my_grid = Grid(10, 10, NULL)

# change tile
my_grid.change_tile(0, 0, FILLED)

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