from maze import Maze
from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plt

FLAG_policy = True
# FLAG_policy = True
# flag to plot polciy after each episode

def plot_policy(Q, num):
	plt.figure(1)
	plt.clf()
	grid_size = len(Q)
	plot =  [[max(Q[i][j]) for i in range(grid_size)] for j in range(grid_size)]
	plt.imshow(plot, interpolation='none', cmap='gray')
	if num == 0:
		plt.savefig("policies/base_policy.png")
	else:
		plt.savefig("policies/policy_%d.png" % (num))

def change(Q1, Q2, env):
	thres = 0.0 
	for i in env.free_states:
		prev_val = sum(Q1[i[0]][i[1]])
		new_val = sum(Q2[i[0]][i[1]])
		if(abs(prev_val - new_val) > thres):
			change = 1
			break
		else:
			change = 0
	return change

def learnTask(env, Q, epsilon = 0.3, alpha = 0.6, discount = 0.9):
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

		if FLAG_policy == True:
			if (episode-1)%50 == 0:
				plot_policy(Q, episode)
	print("Total no. of episodes: %d" %episode)
	print("Total no. of steps: %d" %tot_step)

if __name__ == "__main__":

	print("Initializing")

	grid_size = 11
	# gridsize defines the area of the maze (gridsize X gridsize)
	# number of states in the maze are (gridsize X gridsize)

	free_states = [[ 1,7 ] , [ 0,7 ] , [ 0,6 ] , [ 0,5 ] , [ 0,4 ] , [ 0,3 ] , [ 1,3 ] , [ 2,1 ] , [ 2,2 ] , [ 2,3 ] , [ 2,4 ] , [ 3,8 ] , [ 3,7 ] , [ 3,6 ] , [ 3,5 ] , [ 3,4 ] , [ 4,4 ] , [ 0,10 ] , [ 1,10 ] , [ 2,10 ] , [ 3,10 ] , [ 4,10 ] , [ 5,10 ] , [ 5,9 ] , [ 5,8 ] , [ 5,7 ] , [ 5,6 ] , [ 5,5 ] , [ 5,4 ] , [ 6,4 ] , [ 7,4 ] , [ 8,4 ] , [ 7,10 ] , [ 8,10 ] , [ 9,10 ] , [ 10,10 ] , [ 10,9 ] , [ 10,8 ] , [ 10,7 ] , [ 10,6 ] , [ 8,5 ] , [ 9,6 ] , [ 8,6 ] , [ 8,7 ]]
	# free states define the set of states which are accessible to the agent.

	goal = [8,8]
	# goal defines the state which is the goal position of the maze task

	Q = [[[0,0,0,0] for i in range(grid_size)] for j in range(grid_size)]
	# Q table for storing value corresponing to each action-state pair

	print("Creating Maze Environment")
	env = Maze(grid_size, free_states, goal)
	# creating an instance of maze class

	print("Drawing the Maze Task")
	env.draw("task/")
	# plot the maze with the specified free_states and goal positions
	# in task folder

	print("Learning the policy")
	learnTask(env, Q)
	#learn the policy using Q-learning

	print("Plotting the learned policy")
	plot_policy(Q, 0)
	# plot the action-value function 

	print("Done! checkout task and policies folders")