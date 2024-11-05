from collections import deque

#Define the starting capacities of the jugs and the goal
start_state = (8, 0, 0)
goal = 4

def get_possible_ways(state):
    """
    Generating all possible ways by transferring water between jugs.
    Each state is represented as a tuple (8-pint jug, 5-pint jug, 3-pint jug).
    """
    a, b, c = state
    ways = []

    #Pour from the 8-pint jug to the 5-pint jug
    if a + b <= 5:
        ways.append((0, a + b, c))  #Fill the 5-pint jug
    else:
        ways.append((a - (5 - b), 5, c))  #Fill the 5-pint jug to the top

    #Pour from the 8-pint jug to the 3-pint jug
    if a + c <= 3:
        ways.append((0, b, a + c))  #Fill the 3-pint jug
    else:
        ways.append((a - (3 - c), b, 3))  #Fill the 3-pint jug to the top

    #Pour from the 5-pint jug to the 8-pint jug
    if a + b <= 8:
        ways.append((a + b, 0, c))  # Fill the 8-pint jug
    else:
        ways.append((8, b - (8 - a), c))  #Fill the 8-pint jug to the top

    #Pour from the 5-pint jug to the 3-pint jug
    if b + c <= 3:
        ways.append((a, 0, b + c))  #Fill the 3-pint jug
    else:
        ways.append((a, b - (3 - c), 3))  # Fill the 3-pint jug to the top

    # Pour from the 3-pint jug to the 8-pint jug
    if a + c <= 8:
        ways.append((a + c, b, 0))  # Fill the 8-pint jug
    else:
        ways.append((8, b, c - (8 - a)))  # Fill the 8-pint jug to the top

    #Pour from the 3-pint jug to the 5-pint jug
    if b + c <= 5:
        ways.append((a, b + c, 0))  #Fill the 5-pint jug
    else:
        ways.append((a, 5, c - (5 - b)))  #Fill the 5-pint jug to the top

    return ways

def bfs_solve():
    """
    Solves the Three Jugs Problem using Breadth-First Search with deque.
    Returns the sequence of states leading to the goal.
    """
    queue = deque([(start_state, [])])  #create a deque to serve as a queue
    visited = set([start_state])  #Track visited states to avoid loops

    while queue:
        #Dequeue from the front of the deque
        current_state, path = queue.popleft()  #Efficiently remove from the front
        
        #Check if we've reached the goal in any of the jugs
        if goal in current_state:
            return path + [current_state]  #Return path to the solution

        #Explore all possible ways from the current state
        for way in get_possible_ways(current_state):
            if way not in visited:
                visited.add(way)
                queue.append((way, path + [current_state]))  #Enqueue with path

    return None  #If no solution is found 

#Main
if __name__ == "__main__":
    solution = bfs_solve()
    if solution:
        print("The way of getting exactly 4 pints of water in one of the jugs is as follows:")
        for step in solution:
            print(step)
    else:
        print("No solution found.")
