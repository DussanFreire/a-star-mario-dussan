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
* You can load maps with different difficulties 
* You can create your own board with the dimensions that you want and play with the application options 😉: <div style="text-align:center"><img src="https://github.com/joangerard/mario-map-dussan/blob/main/screenshots/created_map.jpg" /></div>
## Agent:
* **Formulation of the objective:** Find the closest pipeline using BFS and A* 
* **Problem formulation:**
    * **Initial state:** The initial state is a board without any value marked
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
        * Find a pipeline

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
  * A*, using Radar heuristic, is the one that opens fewer states. However, the A* function is also the one that take more time to find the solution. This heuristic has a much better performance when there is not obstacles 
  * A*, using Rect line and Near borders Heuristic, have almost the same results in all the cases.
  * BFS, takes more time and also more states in almost all the cases
  * The difference between A* and BFS are less, when the map has mane obstacles 
    
        
    
    