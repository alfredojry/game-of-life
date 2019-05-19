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
