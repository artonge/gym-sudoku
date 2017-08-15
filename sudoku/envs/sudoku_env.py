import gym
from gym import spaces
import logging
import random
import numpy as np
import time

logger = logging.getLogger(__name__)

resolved = 0
unfinished = 1
error = 2


def checkSolution(grid):
	N = len(grid)

	for i in range(N):
		for j in range(N):
			# If a case is not filled, the sudoku is not finished
			if grid[i][j] == 0:
				return unfinished

			n = N/3
			iOffset = i/n*n
			jOffset = j/n*n
			square = grid[ iOffset:iOffset + n , jOffset:jOffset + n].flatten()
			# Check uniqueness
			uniqueInRow    = countItem(grid[i], grid[i, j])  == 1
			uniqueInCol    = countItem(grid[:,j:j+1].flatten(), grid[i, j]) == 1
			uniqueInSquare = countItem(square, grid[i, j]) == 1

			if not (uniqueInRow and uniqueInCol and uniqueInSquare):
				return error

	return resolved


def countItem(vector, item):
	count = 0
	for item2 in vector:
		if item2 == item: count += 1
	return count


def getSolutions(grid, stopAt=1):
	N = len(grid)
	check = checkSolution(grid)
	# Check if grid is resolve or if there is an error
	if check == resolved:
		return np.array([grid], dtype=int)
	if check == error:
		return np.empty(shape=(0,N,N), dtype=int)

	# Get the first empty spot and start backtracking from it
	solutions = np.empty(shape=(0,N,N), dtype=int)
	for i in range(N):
		for j in range(N):
			# If not empty spot continue
			if grid[i, j] != 0:
				continue
			# Randomize possible values
			values = np.arange(1, N+1)
			np.random.shuffle(values)
			# Try all possiblity from those values
			for value in values:
				cGrid = np.copy(grid)
				cGrid[i, j] = value
				subSolutions = getSolutions(cGrid, stopAt=stopAt-len(solutions))
				solutions = np.concatenate((solutions, subSolutions))
				if len(solutions) >= stopAt:
					return solutions
			return solutions
	return solutions


class SudokuEnv(gym.Env):
	metadata = {'render.modes': ['human']}

	def __init__(self):
		self.observation_space = spaces.Box(low=1, high=9, shape=(9, 9))
		self.action_space = spaces.Tuple((spaces.Discrete(9), spaces.Discrete(9), spaces.Discrete(9)))
		self.grid = []


	def _step(self, action):
		i = action[0]
		j = action[1]
		value = action[2]

		oldGrid = np.copy(self.grid)
		self.grid[i, j] = value

		stats = checkSolution(self.grid)
		# If grid is complet or correct, return positive reward
		if stats == resolved:
			return np.copy(self.grid), 1, True
		elif stats == unfinished:
			return np.copy(self.grid), 1, False
		elif stats == error:
			# If move is wrong, return to old state, and return negative reward
			self.grid = oldGrid
			return np.copy(self.grid), -1, False


	def _reset(self):
		# Get a random solution for an empty grid
		self.grid = getSolutions(np.zeros(shape=(9,9)), 1)[0]

		# Remove some values randomly
		# Always check that the nb of solution is still 1
		count = 0
		while count < 30:
			i = random.randint(0, 8)
			j = random.randint(0, 8)
			oldValue = self.grid[i, j]
			self.grid[i, j] = 0
			nbSolutions = len(getSolutions(self.grid, 2))
			if nbSolutions != 1:
				self.grid[i, j] = oldValue
			else:
				count +=1


	def _render(self, mode='human', close=False):
		for i in range(len(self.grid)):
			print str(self.grid[i, 0:3]) + str(self.grid[i, 3:6]) + str(self.grid[i, 6:9])
			if i % 3 == 2 and i != len(self.grid):
				print '---------------------'



env = SudokuEnv()
env._reset()
