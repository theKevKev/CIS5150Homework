import numpy as np
import matplotlib.pyplot as plt
from bspline2b import bspline2b

def interpatxy(x: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    This version uses the natural end condition
    Uses numpy.linalg.solve to solve both coordinate systems together.
    Input points: two column vectors of x and y coordinates of dim N+1
    
    This version uses x_0, x_1, ..., x_{N-1}, x_N to compute the Bezier
    points and the subdivision version of the de Casteljau algorithm
    to plot the Bezier segments (bspline2b and drawbezier_dc)
    
    This version outputs the x and y coordinates dx and dy of the de Boor control
    points d_{-1}, d_0, d_1, ..., d_{N+1} as 1D arrays
    and the x and y coordinates of the Bezier control polygons
    Bx and By
    """

    points = np.column_stack((x, y))
    
    N = len(x) - 1
    A = 4 * np.eye(N - 1)
    A += np.diag(np.ones(N - 2), 1) + np.diag(np.ones(N - 2), -1)
    rhs = 6 * points[1:-1].copy()
    rhs[0] -= points[0]
    rhs[-1] -= points[-1]
    interior = np.linalg.solve(A, rhs)

    control = np.empty((N + 3, 2))
    control[0] = points[0]
    control[-1] = points[-1]
    control[2:-2] = interior
    control[1] = (2 * points[0] + interior[0]) / 3
    control[-2] = (interior[-1] + 2 * points[-1]) / 3
    dx, dy = control[:, 0], control[:, 1]

    # Plots the spline
    Nx = len(dx)-1
    print(f"Nx = {Nx}")
    nn = 6 # Subdivision level
    drawb = True
    Bx, By = bspline2b(dx,dy,Nx,nn,drawb) # Copy your version of bspline2b into bspline2b.py
    plt.ion()
    plt.plot(x, y, 'b+')
    plt.ioff()

    return (dx, dy, Bx, By)
