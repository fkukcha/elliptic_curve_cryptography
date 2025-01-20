# Done
import numpy as np
import matplotlib.pyplot as plt

# Define the elliptic curve: y^2 = x^3 + ax + b
a, b = -1, 1  # Coefficients for the elliptic curve
x = np.linspace(-2, 2, 500)
y_squared = x**3 + a*x + b

# Mask to avoid invalid values for sqrt (y^2 < 0)
valid = y_squared >= 0
x_valid = x[valid]
y_valid = np.sqrt(y_squared[valid])

# Define point P on the curve
P = (-0.5, 1.19)

# Compute the tangent slope at P for scalar multiplication (P + P)
m_tangent = (3 * P[0]**2 + a) / (2 * P[1])

# Compute coordinates of 2P (intersection of tangent and curve)
x_2P = m_tangent**2 - 2 * P[0]  # x-coordinate of 2P
y_2P = m_tangent * (x_2P - P[0]) + P[1]  # y-coordinate of 2P
R = (x_2P, y_2P)

# Reflect the point R across the x-axis to get 2P'
R_prime = (x_2P, -y_2P)

# Plot the elliptic curve
plt.figure(figsize=(10, 6))
plt.plot(x_valid, y_valid, label='y = +sqrt(x^3 + ax + b)', color='blue')
plt.plot(x_valid, -y_valid, label='y = -sqrt(x^3 + ax + b)', color='red')

# Plot the points P, 2P (R), and 2P' (R_prime)
plt.scatter([P[0], R[0], R_prime[0]], [P[1], R[1], R_prime[1]], color='red', zorder=5)
plt.text(P[0] - 0.05, P[1], 'P', fontsize=12, color='red', ha='right')
plt.text(R[0] + 0.05, R[1], 'R', fontsize=12, color='red', ha='left')
plt.text(R_prime[0] + 0.05, R_prime[1], "R' (2P)", fontsize=12, color='red', ha='left')

# Plot the tangent at P
tangent_x = np.linspace(P[0] - 0.5, P[0] + 2, 100)
tangent_y = m_tangent * (tangent_x - P[0]) + P[1]
plt.plot(tangent_x, tangent_y, color='green', linestyle='--', label='Tangent at P')

# Highlight the reflection from R to R'
plt.plot([R[0], R_prime[0]], [R[1], R_prime[1]], color='orange', linestyle='--', label="Reflection of R to R'")

# Customize the plot
plt.title('Elliptic Curve Scalar Multiplication (2P) and Reflection', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.grid(alpha=0.4)
plt.legend()
plt.ylim(-2, 2)
plt.xlim(-2, 2)

plt.savefig('../images/scalar_multiplication.png')

plt.show()
