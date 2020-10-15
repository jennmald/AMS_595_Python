## Monte Carlo Integration ##
## Author: Jennefer Maldonado
## Date Due: October 16, 2020
import math
import numpy as np

## Resources Used:
## https://en.wikipedia.org/wiki/Monte_Carlo_integration
## Used to understand what the Monte Carlo Method is

# Create a class and call it Numerical Integrator
# It has two instance variables
# Objective - function we are trying to integrate
# Scenarios - how many draws to complete
# Both initially set to None type to wait for initialization
class NumericalIntegrator:
	def __init__(self):
		self.objective = None
		self.scenarios = None
	# When called in test file sets the correct
	# objective function
	def set_objective(self, function):
		self.objective = function
	# When called in test file set the correct
	# number of scenarios
	def set_scenarios(self, n):
		self.scenarios = n
	# Integration occurs here
	# Params:
	# low - lower bound of the integral
	# high - upper bound of the integral
	# Returns:
	# I - the average for the integration
	def integrate(self, low, high):
		frac = (high-low)/self.scenarios
		sigma = 0
		for i in range(1, self.scenarios):
			x = low + (high-low) * np.random.uniform(0,1)
			sigma = sigma + math.sin(x)
		I = frac * sigma
		return I
