import numpy as np
"""
To display a curve obtained using de Casteljau subdivision
Used by run_decas-subdiv_g1 (or g2)
returns the x and y coordinates of the sequence of points
as row vectors
The polyline is not plotted by this function
n = level of recursion

 cpoly is a 2 x (m+1) matrix whose first row consists of x-coordinates
 and second row of y-coordinates of m + 1 control points
"""
def show_decas_subdiv2(cpoly: np.ndarray, n: int) -> tuple[np.ndarray, np.ndarray]:
    r = 0; s = 1
    lpoly = itersubdiv(cpoly, n)
    lnodes = makelist(lpoly)
    x = lnodes[0, :]
    y = lnodes[1, :]
    return (x, y)

def itersubdiv(cpoly: np.ndarray, n: int) -> np.ndarray:
    """
    Args:
        cpoly (np.ndarray): shape 2 x 4
        n (int): number of iters

    Returns:
        np.ndarray: shape 2 x 4 x 2^n
    """
    cpoly = np.expand_dims(cpoly, axis=-1)
    for _ in range(n):
        cpoly = subdivstep(cpoly)
    return cpoly

def makelist(lpoly: np.ndarray) -> np.ndarray:
    """
    Flattens and deduplicates

    Args:
        lpoly (np.ndarray): shape 2 x 4 x 2^M

    Returns:
        np.ndarray: shape 2 x (3 x 2^M + 1)
    """
    return np.concat([lpoly[:, :, 0]] + [lpoly[:, 1:, i] for i in range(1, lpoly.shape[2])], axis=1)

def subdecas(cpoly: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Args:
        cpoly (np.ndarray): shape 2 x 4

    Returns:
        tuple[np.ndarray, np.ndarray]: each of shape 2 x4
    """
    t = 0.5
    layers = {}
    layers[0] = cpoly
    for i in range(cpoly.shape[1] - 1):
        curr = layers[i]
        layers[i+1] = (1 - t) * curr[:, :-1] + t * curr[:, 1:]
        
    ud = []
    ld = []
    for layer, points in layers.items():
        ud.append(points[:, 0])
        ld.append(points[:, -1])

    return np.array(ud).T, np.array(ld[::-1]).T

def subdivstep(lpoly: np.ndarray) -> np.ndarray:
    """
    Args:
        lpoly (np.ndarray): 2 x 4 x l

    Returns:
        np.ndarray: 2 x 4 x 2l
    """
    x, y, z = lpoly.shape
    curr = np.zeros(shape=(x, y, 2*z))
    for index in range(lpoly.shape[2]):
        ud, ld = subdecas(lpoly[:, :, index])
        curr[:, :, 2 * index] = ud
        curr[:, :, 2 * index + 1] = ld
    return curr
    
if __name__ == "__main__":
    points = np.array([[1, 2, 3, 4, 5, 6], [0, 4, 3, 6, 4, 0]])
    # print(points)
    # print(subdivstep(points)) 
    # print(subdivstep(points).shape) 
    # print(itersubdiv(points, 1))
    # print(itersubdiv(points, 2).shape)
    # print(itersubdiv(points, 2))
    print(makelist(itersubdiv(points, 1)))
    # print(p := show_decas_subdiv2(points, 2))
    import matplotlib.pyplot as plt
    # # plt.plot(p[0], p[1])
    # # plt.show()
    for i in range(0, 2):
        x, y = show_decas_subdiv2(points, i)
        plt.plot(x, y, label=f"{i}")
    plt.legend()
    plt.show()

    # print(show_decas_subdiv2(points, 2))

    # points = np.array([[[0, 1, 2, 3], [0, 4, 5, 0]], [[0, 1, 2, 3], [0, 4, 5, 0]], [[0, 1, 2, 3], [0, 4, 5, 0]]]).transpose((1, 2, 0))
    # print(points.shape)
    # print(subdivstep(points).shape) 


