#Maze Task - Reinforcement Learning
This repo contains my reinforcement learning experiment on the maze task domain.  
A reinforcement learning agent is learned to reach a given goal position in a maze.  
Tabular **Q-learning** is used for learning the policy. 

## Description of Maze Task
A maze of size nXn, with one goal position, starting from any random position in the maze, an agent has to reach to the goal position.  
See the image given below -- grey cells are the feasible states to the agent, white cell is the goal position. Action allowed in the feasible states are - up, right, bottom, left with action should lead to an another feasible state.  

![alt tag](https://raw.githubusercontent.com/vikasjiitk/Maze-Reinforcement-Learning/master/task/maze.png)

## Running the code
Dependencies:  
1. python3  
2. numpy  
3. matplotlib

Run from the root of the directory:
```
python main.py 
```
It will plot the final policy in the policies folder. The policies folder contains policies after every 50 episoded, it can be obtained by turning variable FLAG_policy in main.py True.  
The gif of policy leaned is:

![alt tag](https://raw.githubusercontent.com/vikasjiitk/Maze-Reinforcement-Learning/master/result_policies.gif)
