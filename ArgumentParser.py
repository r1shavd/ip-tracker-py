"""
Arguments Parser (Python3)

This is more of a module than a python script file. In this module, we define the function (parse) to fetch and filter the argument entered by the user upon launching any python script. This python file is still in developement, thus there will be more updates coming to this file.

Author : Rishav Das (https://github.com/rdofficial/)
Created on : May 21, 2021

Last modified by : -
Last modified on : -
"""

def parse(arguments, flags):
	""" This function parses and filters the arguments using the user specified flags. The function takes 2 arguments : arguments, flags. """

	# Declaring the list to store the parsed arguments (in each item of dict type)
	# ----
	# token = {"--argument" : "value"}
	# ----
	tokens = {}

	if len(arguments) >= 2:
		# If the length of the arguments list is more than 2, then we continue

		for index, argument in enumerate(arguments):
			# Iterating through each of the arguments

			# The argument recognized conditions
			argumentMatched = False

			for flag in flags:
				# Iterating through each flags as per mentioned in the function's parameter

				if argument == flag:
					# If the flag matches the argument, then we mark the argument as matched

					argumentMatched = True
				else:
					# If the flag does not matches argument, then we skip the current iteration

					continue

			if argumentMatched:
				# If the arguments matches, then we continue

				if arguments[index+1] != None:
					# If the next argument exists, then we continue

					if arguments[index+1] in flags:
						# If the next argument specified is a flag itself, then we continue for parsing next argument (skipping this argument)

						continue
					else:
						# If the next argument specified is not a flag, then we continue append the values to the token

						tokens[f"{argument}"] = f'{arguments[index+1]}'
				else:
					# If the next argument does not exists, then we raise a syntax error with a custom message

					raise SyntaxError(f'Argument value not found for "{argument}"')
			else:
				# If the argument does not matches, then we skip the current iteration of the arguments loop

				continue
	else:
		# If the length of the arguments list is less than 2, then we raise index error with a custom message

		raise IndexError('No arguments specified')

	# Returning all the parsed arguments back
	return tokens