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

def drawbezier_dc(B: np.ndarray, nn: int, drawb: bool) -> None:
    """Draw a 2 x 4 Bezier control polygon subdivided nn times on the current axes."""
    x, y = show_decas_subdiv2(B, nn)
    # Plot the curve segment as a random color
    plt.plot(x, y, color=np.random.rand(3))
    if drawb:
        # Plot bezier points and segments as red +
        plt.plot(B[0, :], B[1, :], 'r+-')
    else:
        # Plot bezier points as red +
        plt.plot(B[0, :], B[1, :], 'r+')
