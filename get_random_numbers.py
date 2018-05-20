import requests

'''
Makes a HTTP GET Request to random.org.
Returns a list of numbers of size 'numbers', each from the range of 0 to maximum inclusive.
Each number will be in the form of a string.
'''
def generate_random_numbers(numbers, maximum):
	r = requests.get('https://www.random.org/quota/?format=plain')

	if r.status_code != 200:
		print("The IP address used here has exceeded its quota for retrieving random bits for today. Please check back after 0000 GMT to see if the quota for random bits is positive.")
		exit()
	print("Quota is still positive. Retrieving random bits...")

	# Gets the random numbers in a single column
	payload = {'num': numbers, 'min': 0, 'max': maximum, 'col': 1, 'base': 10, 'format': 'plain', 'rnd': 'new'}
	r = requests.get('https://www.random.org/integers/', params=payload)

	# Removes last empty space entry
	return r.text.split('\n')[:-1]

# print(get_random_numbers(3,5))

'''
Same as generate_random_numbers, but makes multiple GET Requests if necessary,
as max number of integers that can be requested at one go is 10,000.
'''
def generate_all_random_numbers(number_to_generate):
	random_num_strings = []
	while number_to_generate > 10000:
		random_num_strings += generate_random_numbers(10000, 255)
		number_to_generate -= 10000
	return random_num_strings + generate_random_numbers(number_to_generate, 255)