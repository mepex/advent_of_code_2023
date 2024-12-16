import matplotlib.pyplot as plt
import numpy as np

# Create a character array
char_array = np.array([['#', '.', '@'], ['[', ']', '.']])

# Convert character array to numerical representation
num_array = np.array([[ord(char) for char in row] for row in char_array])

# Display the array as an image
plt.imshow(num_array, cmap='viridis')
plt.colorbar()  # Add a colorbar to interpret values
plt.show()