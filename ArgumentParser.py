"""
Arguments Parser (Python3)

This is more of a module than a python script file. In this module, we define the function (parse) to fetch and filter the argument entered by the user upon launching any python script. This python file is still in developement, thus there will be more updates coming to this file. Currently uses only one method (algorithms) of parsing arguments.

Author : Rishav Das (https://github.com/rdofficial/)
Created on : May 21, 2021

Last modified by : Rishav Das (https://github.com/rdofficial/)
Last modified on : May 23, 2021

Changes made in last modification:
1. Updated the commented docs as well as the __doc__ for the function parse().
2. Updated the feature to parse user input paramters as well as flags too.
3. Removed some futuristic errors from the source code.
4. Added the __main__ execution, if the script file is launched directly. For the default launch, the module works as a script file and then iterates and parses all the arguments which come under flags --about, --help, --doc, -h.
"""

# Importing the required functions and modules
from sys import argv

def parse(arguments = argv, parameters = [], flags = []):
	""" This function parses and filters the arguments using the user specified flags. The function takes 3 arguments : arguments, parameters, flags.

	1. arguments -> The arguments is the actual arguments that are entered by the user during the calling of the script. We can just directly pass the sys.argv list into this function.
	2. parameters -> The parameters argument takes in those specific defined arguments (in a list) that include user entered values. e.g, --username test100. Then, the values arranged are {"--username" : "test100"}. By default, the parameter assigns an empty list to itself, but it is required to be specified. All those in-built arguments should be specified in this in the form of a list. Shown in the example syntax below.
	3. flags -> The flags argument takes in those specifically defined arguments which are just need to be present in the arguments list, and they do no intake any values from the user. e.g., --about, --help. The parsed token which is returned looks like this {"--help" : True}. If the flag is matched, then states True, else False. Shown in the example syntax below.

	Example : parse(arguments = sys.argv, paramters = ['--file'], flags = ['--help', '--about']) """

	# Declaring the list to store the parsed arguments (in each item of dict type)
	# ----
	# tokens = {"--argument" : "value"}
	# ----
	tokens = {}

	for index, argument in enumerate(arguments):
		# Iterating through each of the arguments

		# The argument recognized conditions
		argumentMatched = False
		flagMatched = False

		# Matching the currently iterated argument with the parameters
		for parameter in parameters:
			# Iterating through each parameter as per mentioned in the function's parameter

			if argument == parameter:
				# If the parameter matches the argument, then we mark the argument as matched

				argumentMatched = True
			else:
				# If the parameter does not matches argument, then we skip the current iteration

				continue

		# Matching the currently iterated argument with the flags
		for flag in flags:
			# Iterating through each flag as per mentioned in the function's parameter

			if argument == flag:
				# If the flag matches the argument, then we mark the argument as matched

				flagMatched = True
			else:
				# If the flag does not matches argument, then we skip the current iteration

				continue

		if argumentMatched:
			# If the arguments matches, then we continue

			try:
				# Checking on the next argument for being the value
				if (arguments[index+1] in flags) or (arguments[index+1] in parameters):
					# If the next argument specified is a flag or parameter itself, then we mark the value for the current argument as empty and continue

					tokens[f"{argument}"] = ''
					continue
				else:
					# If the next argument specified is not a flag, then we continue append the values to the token

					tokens[f"{argument}"] = f'{arguments[index+1]}'
			except IndexError:
				# If the next argument does not exists, then we mark the value as empty string

				tokens[f"{argument}"] = ''
		elif flagMatched:
			# If the argument matches with a flag, then we assign true and continue

			tokens[f"{argument}"] = True
		else:
			# If the argument does not matches either with flag or with a parameter, then we skip the current argument

			continue

	# Returning all the parsed arguments back
	return tokens

if __name__ == '__main__':
	# If the script is executed directly, then we do the below stuff

	# Reading the arguments entered by the user
	arguments = parse(argv, ['--doc', '--about', '--help', '-h'])

	# Printing the parsed arguments and their entered values on the console screen
	for key, value in arguments.items():
		print(f'{key}\t->\t{value}')