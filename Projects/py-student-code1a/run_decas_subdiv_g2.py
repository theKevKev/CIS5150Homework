import numpy as np
import matplotlib.pyplot as plt

from get_points import get_points
from show_decas_subdiv2 import show_decas_subdiv2

# Function to display a curve obtained using de Casteljau subdivision
# depth of recursion n
# Maximum depth of recursion M
# show_decas_subdiv2 returns the coordinates of the points on each
# intermediate polyline; the intermediate polyline is plotted
# if parameter flag = 1 is passed
# bx and by are COLUMN vectors of x and y coordinates of control points
# cpoly is a 2 x (m+1) matrix whose first row consists of x-coordinates
# and second row of y-coordinates of m + 1 control points
def run_decas_subdiv_g2(M: int, flag: bool):
    bx, by = get_points()
    cpoly = np.zeros((2, len(bx))); cpoly[0, :] = bx; cpoly[1, :] = by
    m = cpoly.shape[1]-1
    print(f"m (degree of curve) = {m} \n")
    plt.ion()
    # Plots central polygon in green
    plt.plot(cpoly[0, :], cpoly[1, :], "-g")
    for n in range(M):
        x, y = show_decas_subdiv2(cpoly, n+1)
        if n < M:
            # plot intermediate polyline if flag = 1 is passed as a parameter
            if flag:
                plt.plot(x, y)
        else:
            # Final polyline in red
            plt.plot(x, y, "r-")
    
    plt.ioff()