"""
Consider the one-dimentional cellular automaton, consisting of a array of cells.
Each cell contains an integer, 1 or 0.
A cell containing a 1 means occupied, and a 0 means unoccupied. 
On each time step, we update each cell according to the following table of rules,
one for each combination of a current cell and it left and right neighbors.
Left neighbor | Current cell | Right neighbor | New cell
      1       |      1       |       1        |    0
      1       |      1       |       0        |    1
      1       |      0       |       1        |    1
      1       |      0       |       0        |    0
      0       |      1       |       1        |    1
      0       |      1       |       0        |    1
      0       |      0       |       1        |    1
      0       |      0       |       0        |    0
The cells at each end of the array have only one neighbor each and are not updated.
A good website on cellular automata may be found in Wolfram's website:
http://mathworld.wolfram.com/CellularAutomaton.html
"""
"""
Example #1:
$ python3 ca.py
Welcome to the cellular automaton simulation!
Enter number of cells, C: (<= 80): 10
Enter number of time steps, N: 10
Enter the indices of occupied cells (space-separated): 4 6
"""
"""
Example #2:
$ python3 ca.py
Welcome to the cellular automaton simulation!
Enter number of cells, C: (<= 80): 40
Enter number of time steps, N: 30
Enter the indices of occupied cells (space-separated): 38
"""

# Cellular Automata
print('Welcome to the cellular automaton simulation!')

# Prompt the user to enter the number of cells, C
C = input('Enter number of cells, C: (<= 80): ')
# Prompt the user to enter time steps, N
N = input('Enter number of time steps, N: ')
# Prompt the user to enter the list index of cells that initially contain 1 (space-separed)
occupieds = input('Enter the indices of occupied cells (space-separated): ')

def updateCells(cells):
    newList = []
    for i in range(len(cells)):
        if i == 0 or i == len(cells) - 1:
            newList.append(cells[i])
        else:
            left, right = cells[i - 1], cells[i + 1]
            current = cells[i]
            if left == 1 and current == 1 and right == 1:
                newList.append(0)
            elif left == 1 and current == 0 and right == 0:
                newList.append(0)
            elif left == 0 and current == 0 and right == 0:
                newList.append(0)
            else:
                newList.append(1)
    return newList

def displayCells(cells):
    result = ''
    for cell in cells:
        result += '#' if cell else ' '
    print(result)

cells = [0 for _ in range(int(C))]
indices = [int(char) for char in occupieds.split(' ')]
for index in indices:
    cells[index] = 1

lastDigits = ''.join(str(n)[-1] for n in range(int(C)))
print(lastDigits)
displayCells(cells)
for i in range(int(N)):
    cells = updateCells(cells)
    displayCells(cells)
