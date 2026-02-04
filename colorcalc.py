import numpy as np
from scipy.optimize import nnls

# v1 through v4 represent process CMYK colors
v1 = np.array([0, 159, 223])
v2 = np.array([212, 15, 125])
v3 = np.array([250, 225, 0])
v4 = np.array([44, 42, 41])
print(v1, v2, v3, v4)

# x is the color to approximate using our process CMYK colors
x = np.array([40, 189, 164])
print("x=", x);

# The positive span of v1 through v4 is the space of vectors
# we can create by combining v1 through v4, but restricted so
# that we can only add vectors and never subtract them.
def project_onto_positive_span(x, v1, v2, v3, v4):
    V = np.column_stack([v1, v2, v3, v4])
    c, _ = nnls(V, x)
    proj_x = V @ c
    return proj_x, c

proj_x, c = project_onto_positive_span(x, v1, v2, v3, v4)
print("proj_x=", proj_x)

# scale up the coefficients to 255 to create our own CMYK conversion
scaled_c = 255 * c / np.max(np.abs(c))
print(scaled_c)

# This outputs [255, 0, 70, 0]
# Compare this to the typical CMYK conversion [79, 0, 13, 26]
