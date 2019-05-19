# Conway's Game of Life
# Two dimentions
# http://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

"""
Given a 2D array and a number of generations, compute n timesteps of Conway's Game of Life.

The rules of the game are:

Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
Any live cell with more than three live neighbours dies, as if by overcrowding.
Any live cell with two or three live neighbours lives on to the next generation.
Any dead cell with exactly three live neighbours becomes a live cell.
Each cell's neighborhood is the 8 cells immediately around it (i.e. Moore Neighborhood). The universe is infinite in both the x and y dimensions and all cells are initially dead - except for those specified in the arguments. The return value should be a 2d array cropped around all of the living cells. (If there are no living cells, then return [[]].)
"""

def get_generation(cells, generations):
    print(cells)
    data = [[x for x in row] for row in cells]
    for n in range(generations):
        cells_with_border = with_border_dead(data)
        new_cells = []
        for i in range(len(cells_with_border)):
            new_cells.append([])
            for j in range(len(cells_with_border[i])):
                count_lives = get_neighbours_alives(cells_with_border, i, j)
                if cells_with_border[i][j] and count_lives < 2: new_cells[i].append(0)
                elif cells_with_border[i][j] and count_lives > 3: new_cells[i].append(0)
                elif cells_with_border[i][j] and (count_lives == 2 or count_lives == 3): new_cells[i].append(1)
                elif not cells_with_border[i][j] and count_lives == 3: new_cells[i].append(1)
                else: new_cells[i].append(0)
        data = array_cropped(new_cells)
    print(cells)
    return data

def get_neighbours_alives(cells, i, j):
    neighbours = [
        0 if i - 1 < 0 or j - 1 < 0 else cells[i - 1][j - 1], # northwest
        0 if i - 1 < 0 else cells[i - 1][j], # north
        0 if i - 1 < 0 or j + 1 == len(cells[i]) else cells[i - 1][j + 1], # northest
        0 if j + 1 == len(cells[i]) else cells[i][j + 1], # est
        0 if i + 1 == len(cells) or j + 1 == len(cells[i]) else cells[i + 1][j + 1], # southest
        0 if i + 1 == len(cells) else cells[i + 1][j], # south
        0 if i + 1 == len(cells) or j - 1 < 0 else cells[i + 1][j - 1], # southwest
        0 if j - 1 < 0 else cells[i][j - 1], # west
    ]
    return neighbours.count(1)

def with_border_dead(arr):
    result = [row for row in arr]
    for i in range(len(result)):
        result[i].insert(0, 0)
        result[i].append(0)
    zeros_row = [0 for _ in result[0]]
    result.insert(0, zeros_row)
    result.append(zeros_row)
    return result

def first_index_of_1(row):
    return -1 if not row.count(1) else row.index(1)

def last_index_of_1(row):
    return -1 if not row.count(1) else len(row) - row[::-1].index(1) - 1

def array_cropped(cells):
    first_x = min([first_index_of_1(row) for row in cells if first_index_of_1(row) != -1])
    last_x = max([last_index_of_1(row) for row in cells if last_index_of_1(row) != -1])
    first_y = 0
    while not cells[first_y].count(1) : first_y += 1
    last_y = len(cells) - 1
    while not cells[last_y].count(1) : last_y -= 1
    return [] if not last_y else [row[first_x: last_x + 1] for row in cells[first_y: last_y + 1] ]
    
 #Testing:
 # -*- coding: utf-8 -*-
def htmlize(array):
    s = []
    for row in array:
        for cell in row:
            s.append('▓▓' if cell else '░░')
        s.append('\n')
    return ''.join(s)

start = [[1,0,0],
         [0,1,1],
         [1,1,0]]
end   = [[0,1,0],
         [0,0,1],
         [1,1,1]]

resp = get_generation(start, 1)
print(htmlize(resp))# Conway's Game of Life
# Two dimentions
# http://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

"""
Given a 2D array and a number of generations, compute n timesteps of Conway's Game of Life.

The rules of the game are:

Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
Any live cell with more than three live neighbours dies, as if by overcrowding.
Any live cell with two or three live neighbours lives on to the next generation.
Any dead cell with exactly three live neighbours becomes a live cell.
Each cell's neighborhood is the 8 cells immediately around it (i.e. Moore Neighborhood). The universe is infinite in both the x and y dimensions and all cells are initially dead - except for those specified in the arguments. The return value should be a 2d array cropped around all of the living cells. (If there are no living cells, then return [[]].)
"""

def get_generation(cells, generations):
    print(cells)
    data = [[x for x in row] for row in cells]
    for n in range(generations):
        cells_with_border = with_border_dead(data)
        new_cells = []
        for i in range(len(cells_with_border)):
            new_cells.append([])
            for j in range(len(cells_with_border[i])):
                count_lives = get_neighbours_alives(cells_with_border, i, j)
                if cells_with_border[i][j] and count_lives < 2: new_cells[i].append(0)
                elif cells_with_border[i][j] and count_lives > 3: new_cells[i].append(0)
                elif cells_with_border[i][j] and (count_lives == 2 or count_lives == 3): new_cells[i].append(1)
                elif not cells_with_border[i][j] and count_lives == 3: new_cells[i].append(1)
                else: new_cells[i].append(0)
        data = array_cropped(new_cells)
    print(cells)
    return data

def get_neighbours_alives(cells, i, j):
    neighbours = [
        0 if i - 1 < 0 or j - 1 < 0 else cells[i - 1][j - 1], # northwest
        0 if i - 1 < 0 else cells[i - 1][j], # north
        0 if i - 1 < 0 or j + 1 == len(cells[i]) else cells[i - 1][j + 1], # northest
        0 if j + 1 == len(cells[i]) else cells[i][j + 1], # est
        0 if i + 1 == len(cells) or j + 1 == len(cells[i]) else cells[i + 1][j + 1], # southest
        0 if i + 1 == len(cells) else cells[i + 1][j], # south
        0 if i + 1 == len(cells) or j - 1 < 0 else cells[i + 1][j - 1], # southwest
        0 if j - 1 < 0 else cells[i][j - 1], # west
    ]
    return neighbours.count(1)

def with_border_dead(arr):
    result = [row for row in arr]
    for i in range(len(result)):
        result[i].insert(0, 0)
        result[i].append(0)
    zeros_row = [0 for _ in result[0]]
    result.insert(0, zeros_row)
    result.append(zeros_row)
    return result

def first_index_of_1(row):
    return -1 if not row.count(1) else row.index(1)

def last_index_of_1(row):
    return -1 if not row.count(1) else len(row) - row[::-1].index(1) - 1

def array_cropped(cells):
    first_x = min([first_index_of_1(row) for row in cells if first_index_of_1(row) != -1])
    last_x = max([last_index_of_1(row) for row in cells if last_index_of_1(row) != -1])
    first_y = 0
    while not cells[first_y].count(1) : first_y += 1
    last_y = len(cells) - 1
    while not cells[last_y].count(1) : last_y -= 1
    return [] if not last_y else [row[first_x: last_x + 1] for row in cells[first_y: last_y + 1] ]
    
 #Testing:
 # -*- coding: utf-8 -*-
def htmlize(array):
    s = []
    for row in array:
        for cell in row:
            s.append('▓▓' if cell else '░░')
        s.append('\n')
    return ''.join(s)

start = [[1,0,0],
         [0,1,1],
         [1,1,0]]
end   = [[0,1,0],
         [0,0,1],
         [1,1,1]]

resp = get_generation(start, 1)
print(htmlize(resp))
