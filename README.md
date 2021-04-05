# Help Mario 👨⚠‼ Save the princess 👸
# Prerequisites:
* Conda 4.9.2
* JetBrains IDE
* If you don't have conda, then maybe you will need to install flask
# Installation
* Open a terminal in the folder named "a-star-mario-dussan"
* Write the following command: "python app.py"
* Click on the URL or open your localhost <div style="text-align:center"><img src="https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/instruccions.jpg" /></div>
# Project Description
_Is a basic web application where you can build your own board which includes pipelines 🏁, walls 🟥 and of course Mario 👨! The main objective of this application is to find the path to the closest pipe and mark the path using BFS and A *, make some comparisons, find the effective effective
branch factor and calculate the number of states. 

This web application has two basic interfaces:
1. Menú:  <div style="text-align:center"><img src="https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/menu.jpg" /></div>
2. Board:
* You can load a default board and have a fast view of the application:<div style="text-align:center"><img src="https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/default_board.jpg" /></div>
* You can create your own board with the dimensions that you want and play with the application options 😉: <div style="text-align:center"><img src="https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/created_map.jpg" /></div>
* Don't trap Mario 😂:<div style="text-align:center"><img src="https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/mario_trapped.jpg" /></div>
## Agent:
* **Formulation of the objective:** The objective is to mark the shortest distance from a pipeline in all the free spaces of the board, and find the shortest path from Mario's position
* **Problem formulation:**
    * **Initial state:** The initial state is a board without any distances marked
        * **Description of the actions:**
            * UP = Move up from the current position ⬆
            * DOWN = Move down from the current position ⬇
            * LEFT = Move left from the current position ⬅
            * RIGHT = Move right from the current position ➡
    * **Transitional model:**
        * UP: move("up", state.row, state.col) -> state: (row, col + 1)
        * DOWN: move("down", state.row, state.col) -> state: (row, col - 1)
        * LEFT: move("left", state.row, state.col) -> state: (row - 1, col)
        * RIGHT: move("right", state.row, state.col) -> state: (row - 1, col)
    * **Target test:**
        * In this case we don't have a target because this prophecy is working with a normal agent. We could
          say that the target test would be to mark all the free spaces with the correct distance to the closest pipeline
    * **Route cost:**
        * The route cost for each action is 1
    * **State space:** :<div style="text-align:center"><img src="https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/states_bfs.jpg" /></div>
* **Search:**
  The search algorithm BFS was used in this project, even though it uses more memory, its quantity of states is much
  lower than the quantity of states used in DFS. For example in the following image we can see how the dfs algorithm
  would mark all the free spaces on the board: <div style="text-align:center"><img src="https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/states using dfs.jpg" /></div>
  This quantity doesn't seam to high when we compare it with the same example using BFS: <div style="text-align:center"><img src="https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/states_bfs.jpg" /></div>
  But when the algorithm dfs is used on a 11x11 board with a pipeline at the
  position (6, 6), the program goes through 1043 states. <div style="text-align:center"><img src="https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/dfs in a 11x11 board.jpg" /></div>
  In the other hand, when a bfs algorithm is used for the same problem the program only goes through 121 states. <div style="text-align:center"><img src="https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/bfs in a 11x11 board.jpg" /></div>
  That's the main reason why we rather use bfs for this program.

## Heuristic functions used:
* Rect line: if the successor's grandfather, successor's father and successor share the same column or row, then the heuristic is lower
* Near borders 🧱: if the successor is in the border of the boar, then the heuristic is lower
* Radar 🔍: 
    * A fast search is made from marios position until a pipe it's found, in other words, the context it's found(this sear is only made at the beginning or when F cost is high)
    * Once we know the position of the closest pipe, that position is classified that position as:
        * right: In the same row, at right
        * left: In the same row, at left
        * up: In the same col, at up
        * down: In the same col, at down
        * upper_right: upper_right quadrant
        * upper_left: upper_left quadrant
        * down_right: down_right quadrant
        * down_left: down_left quadrant
    * Then a parse is made in order to get a cost from each classification
        * Lower heuristic: right, left, up and down
        * Higher heuristic: upper_right, upper_left, down_right and down_left

## Observations 👀:
* After several experiments, we got the following conclusions:
  * A*, using Radar heuristic, is the one that opens fewer states. However, the A* function is also the one that take more time to find the solution 
  * A*, using Rect line and Near borders Heuristic, have almost the same results in all the cases.
  * BFS, takes more time and also more states in almost all the cases
    
        
    
    