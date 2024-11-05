A. Three Jugs Problem Solution using Breadth-First Search (BFS)

This program solves the three jugs (8-pint jug full of water and a 5-pint and 3-pint empty jugs) problem using BFS and implemented using deque as a built-in data structure from collections. The goal is to obtain exactly 4 pints of water in one of the jugs by pouring water between the jugs using python as a programing language.

The code has two functions: get_possible_ways() that generates all possible states from a given state by  transfering water in the jugs and bfs_solve() that allows to explore all states until we reach the possibility of having a jug with exactly 4 pints using deque to make sure that the visited state does not come again.

B. Problem and solution description

1. Initial state is (8,0,0) in the format (8-pint jug, 5-pint jug, 3-pint jug).
2. The goal is to achieve exactly 4 pints in one of the jugs.

C. Solution process

1. Start with initial state: (8,0,0)
2. Pour water from the 8-pint jug in the 5-pint jug: (3,5,0)
3. Pour water from 5-pint jug in the 3-pint jug: (3,2,3)
4. Pour water from the 3-pint jug in the 8-pint jug: (6,2,0)
5. Pour water from the 5-pint jug in the 3-pint jug: (6,0,2)
6. Pour water from the 8-pint jug in the 5-pint jug: (1,5,2)
7. Pour water from the 5-pint jug in the 3-pint jug: (1,4,3) which is the solution we want.

D. Running the code

To run the code,follow the following steps:
1. Download the recent version of python if you don't have it on your computer.
2. Open the terminal 
3. Navigate towards the directory where you saved the code (threeJugs.py)
4. Type python3 threeJugs.py

E. Expected output is:
The way of getting exactly 4 pints of water in one of the jugs is as follows:
(8,0,0)
(3,5,0)
(3,2,3)
(6,2,0)
(6,0,2)
(1,5,2)
(1,4,3)


