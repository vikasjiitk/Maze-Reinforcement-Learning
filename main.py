from maze import Maze

if __name__ == "__main__":

	grid_size = 11
	# gridsize defines the area of the maze (gridsize X gridsize)
	# number of states in the maze are (gridsize X gridsize)

	free_states = [[ 1,7 ] , [ 0,7 ] , [ 0,6 ] , [ 0,5 ] , [ 0,4 ] , [ 0,3 ] , [ 1,3 ] , [ 2,1 ] , [ 2,2 ] , [ 2,3 ] , [ 2,4 ] , [ 3,8 ] , [ 3,7 ] , [ 3,6 ] , [ 3,5 ] , [ 3,4 ] , [ 4,4 ] , [ 0,10 ] , [ 1,10 ] , [ 2,10 ] , [ 3,10 ] , [ 4,10 ] , [ 5,10 ] , [ 5,9 ] , [ 5,8 ] , [ 5,7 ] , [ 5,6 ] , [ 5,5 ] , [ 5,4 ] , [ 6,4 ] , [ 7,4 ] , [ 8,4 ] , [ 7,10 ] , [ 8,10 ] , [ 9,10 ] , [ 10,10 ] , [ 10,9 ] , [ 10,8 ] , [ 10,7 ] , [ 10,6 ] , [ 8,5 ] , [ 9,6 ] , [ 8,6 ] , [ 8,7 ]]
	# free states define the set of states which are accessible to the agent.

	goal = [8,8]
	# goal defines the state which is the goal position of the maze task

	Q = [[[0,0,0,0] for i in range(grid_size)] for j in range(grid_size)]
	# Q table for storing value corresponing to each action-state pair

	env = Maze(grid_size, free_states, goal)
	# creating an instance of maze class

	env.draw()
	# plot the maze with the specified free_states and goal positions

	learnTask(env, Q)
	#learn the policy using Q-learning

	plotPolicy(Q)
	# plot the action-value function 