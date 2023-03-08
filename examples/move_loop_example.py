from tiles import Grid, Entity, FILLED, NULL, clear

grid = Grid(10, 10, NULL)

player = Entity(FILLED, grid)

grid.draw_entity(0, 0, player)

while True:
    clear()
    print(grid.create(show_nums=True))
    player.move_loop()
