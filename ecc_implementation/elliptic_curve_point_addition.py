"""
Elliptic Curve Point Addition with Reflection.
This script demonstrates the point addition operation on an elliptic curve and the reflection of the resulting point.
"""

import numpy as np
import matplotlib.pyplot as plt

# Define the elliptic curve: y^2 = x^3 + ax + b
a, b = -1, 1  # Coefficients for the elliptic curve
x = np.linspace(-2, 2, 500)
y_squared = x**3 + a*x + b

# Plot the elliptic curve
plt.figure(figsize=(8, 6))
plt.plot(x, np.sqrt(y_squared), label='y = +sqrt(x^3 - x + 1)', color='blue')
plt.plot(x, -np.sqrt(y_squared), label='y = -sqrt(x^3 - x + 1)', color='red')

# Define points P and Q on the curve
P = (-1, 1)
Q = (0, 1)

# Calculate R = P + Q on the elliptic curve
# The slope of the line connecting P and Q
m = (Q[1] - P[1]) / (Q[0] - P[0])
# x-coordinate of R
x_r = m**2 - P[0] - Q[0]
# y-coordinate of R
# y_r = m * (P[0] - x_r) - P[1]
y_r = m * (x_r - P[0]) + P[1]
R = (x_r, y_r)

# Mirror R across the x-axis for the final point R'
R_prime = (x_r, -y_r)
print(R_prime)
# Plot points P, Q, R, and R'
plt.scatter([P[0], Q[0], R[0], R_prime[0]], [P[1], Q[1], R[1], R_prime[1]], color='red', zorder=5)
plt.text(P[0], P[1], 'P', fontsize=12, color='red', ha='right')
plt.text(Q[0], Q[1], 'Q', fontsize=12, color='red', ha='left')
plt.text(R[0], R[1], "R", fontsize=12, color='red', ha='left')
plt.text(R_prime[0], R_prime[1], "R'", fontsize=12, color='red', ha='left')

# Plot the line connecting P and Q
line_x = np.linspace(P[0] - 0.5, Q[0] + 1.5, 100)
line_y = m * (line_x - P[0]) + P[1]
plt.plot(line_x, line_y, color='green', linestyle='--', label='Line through P and Q')

# Highlight the reflection of R to R'
plt.plot([R[0], R_prime[0]], [R[1], R_prime[1]], color='orange', linestyle='--', label="Reflection of R to R'")

# Customize the plot
plt.title('Elliptic Curve Point Addition with Reflection', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.grid(alpha=0.4)
plt.legend()
plt.ylim(-2, 2)
plt.xlim(-2, 2)

plt.savefig('../images/point_addition.png')

plt.show()
