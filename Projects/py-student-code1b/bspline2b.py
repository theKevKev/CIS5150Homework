import numpy as np
import matplotlib.pyplot as plt
from typing import Iterable
from drawbezier_dc import drawbezier_dc
from numpy.lib.stride_tricks import sliding_window_view

"""
To display a cubic B-sline given by de Boor control points
d_0, ..., d_N  

Input points: left click for the d's then press enter (or return, or right click)  

Performs a loop from 1 to N - 2 to compute the Bezier
points using de Casteljau subdivision
nn is the subdivision level

This version also outputs the x-coodinates and the y-coordinates
of all the control points of the Bezier segments stored in
Bx(N-2,4) and By(N-2,4)
"""

def bspline2b(dx: np.ndarray|list[float], dy: np.ndarray|list[float], N: int, nn: int, drawb: bool) -> tuple[np.ndarray, np.ndarray]:
    # Works if N >= 4

    # === COMPUTE Bx AND By HERE ===
    dx_prime = np.array(dx, dtype=float).copy()
    dy_prime = np.array(dy, dtype=float).copy()
    
    dx_prime[0]  = 6*dx[0] - 6*dx[1] + dx[2]
    dy_prime[0]  = 6*dy[0] - 6*dy[1] + dy[2]
    dx_prime[1]  = 1.5*dx[1] - 0.5*dx[2]
    dy_prime[1]  = 1.5*dy[1] - 0.5*dy[2]

    dx_prime[-2] = 1.5*dx[-2] - 0.5*dx[-3]
    dy_prime[-2] = 1.5*dy[-2] - 0.5*dy[-3]
    dx_prime[-1] = 6*dx[-1] - 6*dx[-2] + dx[-3]
    dy_prime[-1] = 6*dy[-1] - 6*dy[-2] + dy[-3]
    
    W = np.array([
        [1/6, 4/6, 1/6, 0  ], 
        [0,   2/3, 1/3, 0  ],
        [0,   1/3, 2/3, 0  ],
        [0,   1/6, 4/6, 1/6]
    ])
    
    dx_window = sliding_window_view(dx_prime, 4)
    dy_window = sliding_window_view(dy_prime, 4)
    
    Bx = dx_window @ W.T
    By = dy_window @ W.T
    
    # nn is the subdivision level
    plt.figure()
    dim_data = 2
    B = np.zeros((dim_data, 4))
    plt.plot(dx, dy, 'or-')
    plt.ion()
    for i in range(N-2):
        B[0, :] = Bx[i,:]
        B[1, :] = By[i,:]
        drawbezier_dc(B, nn, drawb)
    plt.ioff()

    return (Bx, By)

if __name__ == "__main__":
    dx = [4.2173, 1.5849, 2.1301, 4.7625, 7.7531, 8.3606, 5.4322]
    dy = [1.8424, 3.2603, 6.0028, 7.6446, 6.3013, 2.5886, 4.0065]

    bx, by = bspline2b(dx, dy, 6, 3, False)
    print(bx)
    print(by)