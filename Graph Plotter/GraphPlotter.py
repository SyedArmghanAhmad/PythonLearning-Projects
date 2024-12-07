import matplotlib.pyplot as plt
import numpy as np

# Data
cities = ['Islamabad', 'Rawalpindi', 'Faislabad', 'Karachi', 'Lahore']
temperatures = [15, 22, 30, 35, 40]  # Temperatures corresponding to cities

# Normalize temperatures for colormap
norm = plt.Normalize(min(temperatures), max(temperatures))
sm = plt.cm.ScalarMappable(cmap='coolwarm', norm=norm)
colors = [sm.to_rgba(temp) for temp in temperatures]

# Plotting
fig, ax = plt.subplots()  # Create a figure and axis
bars = ax.bar(cities, temperatures, color=colors, edgecolor='black')

# Add colorbar
cbar = plt.colorbar(sm, ax=ax, label='Temperature (°C)')  # Attach colorbar to the same Axes
cbar.set_label('Temperature (°C)')

# Labeling and styling
ax.set_xlabel("Cities")
ax.set_ylabel("Temperature (°C)")
ax.set_title("Temperature by City")

plt.show()
