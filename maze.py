import numpy as np
import matplotlib.pyplot as plt

class Maze(object):
	def __init__(self, grid_size, free_states = [], goal = []):
		self.grid_size = grid_size
		self.num_actions = 4  
		# four actions in each state -- up, right, bottom, left
		self.free_states = free_states
		self.goal = goal
		self.maze = np.zeros((grid_size,grid_size))
		for i in self.free_states:
			self.maze[i[0]][i[1]] = 1

	def reset(self):
		# reset the environment
		self.start_index = np.random.randint(0,len(self.free_states))
		self.curr_state = self.free_states[self.start_index]

	def state(self):
		return self.curr_state

	def draw(self, path = ""):
		# draw the maze configiration
		self.grid = np.zeros((self.grid_size, self.grid_size))
		for i in self.free_states:
			self.grid[i[1]][i[0]] = 0.5
		self.grid[self.goal[1]][self.goal[0]] = 1
		plt.figure(0)
		plt.clf()
		plt.imshow(self.grid, interpolation='none', cmap='gray')
		plt.savefig(path + "maze.png")

	def act(self, action):
		if(action == -1):
			self.next_state = self.curr_state
		elif(action == 0):
			self.next_state = [self.curr_state[0]-1,self.curr_state[1]]
		elif(action == 1):
			self.next_state = [self.curr_state[0]+1,self.curr_state[1]]
		elif(action == 2):
			self.next_state = [self.curr_state[0],self.curr_state[1]+1]
		elif(action == 3):
			self.next_state = [self.curr_state[0],self.curr_state[1]-1]

		if ((self.next_state in self.free_states) or (self.next_state == self.goal)):
			self.curr_state = self.next_state
			self.reward = 0
		else:
			self.next_state = self.curr_state
			self.reward = 0

		if(self.next_state == self.goal):
			self.reward = 1
			self.game_over = True
		else:
			self.game_over = False

		return self.next_state, self.reward, self.game_over