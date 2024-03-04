import matplotlib.pyplot as plt
import numpy as np

# Generate some sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a chart plot
plt.plot(x, y)
plt.title('Simple Data Visualization')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Display the plot
plt.show()