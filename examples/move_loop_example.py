from tiles import Grid, Entity, FILLED, NULL, clear

grid = Grid(10, 10, NULL)

player = Entity(FILLED, grid, 0, 0)



while True:
    clear()
    print(grid.create(show_nums=True))
    player.move_loop()
