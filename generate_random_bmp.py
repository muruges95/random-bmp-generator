from PIL import Image
from get_random_numbers import generate_random_numbers, generate_all_random_numbers

def get_RGB_tuple(random_num_strings, index):
	r_val = int(random_num_strings[index])
	g_val = int(random_num_strings[index + 1])
	b_val = int(random_num_strings[index + 2])

	return (r_val, g_val, b_val)

# Generates 3 random numbers for every pixel in the result image, which in this case contains 128 * 128 pixels
number_to_generate = 128 * 128 * 3 
random_num_strings = generate_all_random_numbers(number_to_generate)

img = Image.new( 'RGB', (128,128), "black") # Create a new black image
pixels = img.load() # Create the pixel map
index = 0
for i in range(img.size[0]):    # For every pixel:
    for j in range(img.size[1]):
        pixels[i,j] = get_RGB_tuple(random_num_strings, index) # Set the colour accordingly
        index += 3 # We use 3 random numbers at a time

img.show()