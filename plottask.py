# Plotting histogram of a normal distribution of a 1000 values with mean of 5 and standard deviation of 2.
# Plot h(x) = x^3
# Author Justyna Pinkowska

import numpy as np
import matplotlib.pyplot as plt

# Plot histogram of a normal distribution

norm_dist = np.random.normal(5, 2, 1000)
plt.hist(norm_dist, alpha=0.5, label='Normal distribution')

# Plot h(x) = x^3
xpoints = np.array(range(1,11))
ypoints = xpoints ** 3
cube= plt.plot(xpoints, ypoints, color ='red', label='h(x) = x^3')


# Add title
plt.title("Normal distribution and Cube of x")

# Add title
plt.xlabel('xpoints')
plt.ylabel('h(x)')

# Add legend
plt.legend()

# Saving the plot (.png file)
plt.savefig('plot.png')

plt.show()