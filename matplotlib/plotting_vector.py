import matplotlib.pyplot as plt

# Define vectors
c = (5, -4)  # fisrt vector
d = (-2, 3)  # second vector

# Resultant vector
result = (c[0] + d[0], c[1] + d[1])   # sum Of first and second vector

# Create figure
plt.figure()

# Draw vector c
plt.arrow(0, 0, c[0], c[1], length_includes_head=True, head_width=0.3)

# Draw vector d
plt.arrow(0, 0, d[0], d[1], length_includes_head=True, head_width=0.3)

# Draw parallelogram sides
plt.plot([c[0], result[0]], [c[1], result[1]])
plt.plot([d[0], result[0]], [d[1], result[1]])

# Draw resultant vector
plt.arrow(0, 0, result[0], result[1], length_includes_head=True, head_width=0.3)

# Axis settings
plt.axhline(0)
plt.axvline(0)
plt.gca().set_aspect('equal', 'box')
plt.grid(True)
plt.title("Parallelogram Rule for Vector Addition")
plt.xlabel("x")
plt.ylabel("y")

plt.show()
