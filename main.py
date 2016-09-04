from maze import Maze
from copy import deepcopy

def learnTask(env, Q):
	grid_size = len(Q)
	num_actions = env.num_actions

	## Learning source task

	tot_step = 0 # to count total no. of steps
	episode = 0 # to count total no. of episodes
	not_change_count = 0 # to check if Q function is changed or not
	change_no = 5 # required number of episodes for which Q function should be unchanged before stopping

	while (True):
		env.reset()
		game_over = False
		max_step = 100  # max number of steps for an episode, after max_iter steps, the episode ends
		step = 0
		episode += 1
		Q2 = deepcopy(Q)
		while not (game_over or step > max_step):
			step += 1
			curr_state = env.state()
			if np.random.rand() <= epsilon:  # epsilon-greedy policy
				action = np.random.randint(0, num_actions)
			else:
				if(max(Q[curr_state[0]][curr_state[1]]) == min(Q[curr_state[0]][curr_state[1]])):
					action = -1
					# if Q[] function is unable to select action, then no action taken
				else:
					action = np.argmax(Q[curr_state[0]][curr_state[1]])
					# best action from Q table
			next_state, reward, game_over = env.act(action)
			# Q-learning update
			Q[curr_state[0]][curr_state[1]][action] = Q[curr_state[0]][curr_state[1]][action] + alpha*(reward + discount*max(Q[next_state[0]][next_state[1]]) - Q[curr_state[0]][curr_state[1]][action])
		tot_step += step
		if (step > max_step):
			not_change_count = 0
		elif not change(Q, Q2, env):
			not_change_count += 1
			if(not_change_count == change_no):
				break
		else:
			not_change_count = 0

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