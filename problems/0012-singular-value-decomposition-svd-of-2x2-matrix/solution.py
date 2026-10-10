import numpy as np
import math
def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    """
    Compute SVD of a 2x2 matrix using one Jacobi rotation.
    
    Args:
        A: A 2x2 numpy array
    
    Returns:
        Tuple (U, S, Vt) where A ≈ U @ diag(S) @ Vt
        - U: 2x2 orthogonal matrix
        - S: length-2 array of singular values
        - Vt: 2x2 orthogonal matrix (transpose of V)
    """

    V = None

    a1, a2 = A[:, 0], A[:, 1]
    p = np.dot(a1.T, a1).item(0)
    q = np.dot(a2.T, a2).item(0)
    r = np.dot(a1.T, a2).item(0)

    if r == 0: V = np.identity(2)
    else:
        tau = (p - q) / (2 * r)
        sign_tau = 1 if tau >= 0 else -1
        t = sign_tau / (np.abs(tau) + math.sqrt(1 + tau**2))
        c = 1 / math.sqrt(1 + t**2)
        s = c * t
        V = np.array([[c, -s], [s, c]])
   

    v1, v2 = V[:, 0], V[:, 1]
    as1 = v1[0] * a1 + v1[1] * a2
    as2 = v2[0] * a1 + v2[1] * a2

    o1 = math.sqrt(np.dot(as1.T, as1).flat[0])
    o2 = math.sqrt(np.dot(as2.T, as2).flat[0])

    u1 = as1/o1
    u2 = as2/o2

    if o2 > o1:
        return (np.stack([u2, u1], axis=1), np.array([o2, o1]), np.stack([v2, v1], axis=1).T)
    else:
        return (np.stack([u1, u2], axis=1), np.array([o1, o2]), V.T)
