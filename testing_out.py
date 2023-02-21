# %%
from minesweeper import Minesweeper, Sentence
import random 

# %%
random.seed(42)

# %%
Minesweeper().print()

# %%
Minesweeper().nearby_mines((0,1))

# %%

knowledge = []
cell=(1,4)
new_sentence_cells = set()
height = 8
width = 8
safes = set()
mines = set()
count = 1

# %%

mines.update([(0,1), (0,3), (1,1), (1,2), (3,2), (3,3), (4,3), (6,0)])

# %%
for i in range(cell[0] - 1, cell[0] + 2):
    for j in range(cell[1] - 1, cell[1] + 2):

        # Ignore the cell itself
        if (i, j) == cell:
            continue

        if (i,j) in safes:
            continue

        if (i,j) in mines:
            count = count - 1 

        # Update count if cell in bounds and is mine
        if 0 <= i < height and 0 <= j < width:
            new_sentence_cells.add((i,j))

knowledge.append(Sentence(new_sentence_cells, count))

# %%

def mark_mine(cell):
    """
    Marks a cell as a mine, and updates all knowledge
    to mark that cell as a mine as well.
    """
    mines.add(cell)
    for sentence in knowledge:
        sentence.mark_mine(cell)

# %%

for sentence in knowledge:
    for cell in sentence.cells.copy(): 
        if cell in mines:
            mark_mine(cell)

# %%
