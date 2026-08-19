import numpy as np

array = np.random.random((3, 3))

arrayr = [[0.5, 0.2],
         [0.8, 0.1]]

x = np.pi / 4

print(np.sin(x))   # 0.7071...
print(np.cos(x))   # 0.7071...
print(np.tan(arrayr))   # 1.0

print(np.log(array))


print(np.round(array))
# Common NumPy trigonometric functions
# Function	Meaning
# np.sin(x)	Sine
# np.cos(x)	Cosine
# np.tan(x)	Tangent
# np.arcsin(x)	Inverse sine
# np.arccos(x)	Inverse cosine
# np.arctan(x)	Inverse tangent
# np.deg2rad(x)	Degrees → radians
# np.rad2deg(x)	Radians → degrees