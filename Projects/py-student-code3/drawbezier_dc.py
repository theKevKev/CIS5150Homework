import numpy as np
import matplotlib.pyplot as plt
from show_decas_subdiv2 import show_decas_subdiv2
"""
function to draw a Bezier segment
using de Casteljau subdivision
nn = level of subdivision
used by bspline4_dc
also plots the Bezier control polygons if drawb = 1
"""

def drawbezier_dc(B: np.ndarray, nn: int, drawb: bool):
    # nn is the subdivision level
    x, y = show_decas_subdiv2(B, nn)
    # === Draw curve here === #
    plt.plot(x, y, color=np.random.rand(3))
    # Plot the curve segment as a random color
    if drawb:
        # Plot bezier points and segments as red +
        plt.plot(B[0, :], B[1, :], 'r+-')
    else:
        # Plot bezier points as red +
        plt.plot(B[0, :], B[1, :], 'r+')