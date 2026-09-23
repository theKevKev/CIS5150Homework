import os
import numpy as np
import matplotlib.pyplot as plt
from typing import Iterable

from show_decas_subdiv2 import show_decas_subdiv2
from run_decas_subdiv_g2 import run_decas_subdiv_g2

def write_table(out: str, headers: list[str], dat: list[Iterable]):
    with open(out, "w") as outfile:
        outfile.writelines([",".join(headers) + "\n"])
        zipped = list(zip(*dat))
        outfile.writelines([",".join([str(x) for x in zipped[i]]) + "\n" for i in range(len(zipped))])

# Project 1A
# version in which Part ii has been moved outside of the for loop
# Python rewrite (SRM)

if not (os.path.exists('output') and os.path.isdir('output')):
    os.mkdir('output')
    # os.mkdir('output/part1')
    # os.mkdir('output/part2')
    # os.mkdir('output/part3')
    # os.mkdir('output/code')

cpoly: list[list[np.ndarray]] = [[np.zeros(0) for _ in range(5)] for _ in range(2)]
cpoly[0][0] = np.array([[0, 1, 2, 3],
                        [0, 4, 5, 0]])
cpoly[0][1] = np.array([[0, 1, 3, 4],
                        [-2, 2, -2, 0]])
cpoly[0][2] = np.array([[3, 0, 4, 1],
                        [0, 3, 3, 0]])
cpoly[0][3] = np.array([[4, 0, 4, 0],
                        [0, 1, 1, 0]])
cpoly[0][4] = np.array([[4, 0, 6, 2],
                        [0, 6, 6, 0]])

cpoly[1][0] = np.array([[1, 2, 3, 4, 5, 6],
                        [0, 4, 3, 6, 4, 0]])
cpoly[1][1] = np.array([[2.9255, 0.9333, 2.6161, 6.6779, 9.0571, 7.1809],
                        [1.7041, 3.9307, 7.2510, 7.7979, 4.4385, 2.0361]])
cpoly[1][2] = np.array([[1.3832, 9.7044, 4.9161, 1.6460, 7.2664, 8.9307, 7.2372, 3.8650],
                        [0.9768, 8.9458, 9.8064, 8.7565, 0.6325, 1.3554, 5.4174, 3.9716]])
cpoly[1][3] = np.array([[7.6168, 5.7044, 1.6606, 1.6168, 4.2445, 5.8212, 8.7847, 9.4124, 8.0693],
                        [1.8029, 1.3726, 2.6807, 6.0542, 9.0835, 6.4673, 4.6773, 7.2418, 9.3417]])
cpoly[1][4] = np.array([[7.1058, 9.7190, 7.3540, 4.2591, 8.6825, 4.7263, 0.8577, 3.9964, 2.9599, 1.5438, 5.2664],
                        [8.1196, 5.4002, 2.3881, 5.1936, 7.2590, 0.4088, 9.4621, 9.7031, 7.1386, 3.7478, 7.7926]])

M = 6
for p in range(2):
    for i in range(len(cpoly[0])):
        plt.ion()
        fig, ax = plt.subplots()
        ax.plot(cpoly[p][i][0, :], cpoly[p][i][1, :], "-g")
        for m in range(M):
            x, y = show_decas_subdiv2(cpoly[p][i], m+1)
            if m < M:
                # Plot intermediate polyline
                ax.plot(x, y)
            else:
                # Final polyline is read
                ax.plot(x, y, "r-")
            # Write table to text file
            write_table(os.path.join("output", f"proj1a_{p+1}i_{i+1}_{m+1}.txt"), ['x','y'], [x, y])
        
        plt.pause(0.5)
        fig.savefig(os.path.join("output", f"proj1a_{p+1}i_{i+1}.png"))
        plt.close(fig)
        plt.ioff()

# Run part ii of the code
run_decas_subdiv_g2(M, True)
plt.savefig(os.path.join("output", f"proj1a_{p+1}ii_1.png"))
plt.ion()
_ = plt.ginput(1)
plt.cla()
plt.draw()
plt.ioff()
run_decas_subdiv_g2(M, True)
plt.savefig(os.path.join("output", f"proj1a_{p+1}ii_2.png"))
_ = plt.ginput(1)