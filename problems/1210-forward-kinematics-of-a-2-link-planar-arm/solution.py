import numpy as np
from math import sin, cos

def forward_kinematics(l1, l2, theta1, theta2):
    
    x = l1 * cos(theta1) + l2 * cos(theta1 + theta2)
    y = l1 * sin(theta1) + l2 * sin(theta1 + theta2)
    pos = [x, y]

    dxd1 = l1 * (-sin(theta1)) + l2 * (-sin(theta1 + theta2))
    dxd2 = l2 * (-sin(theta1 + theta2))
    dyd1 = l1 * (cos(theta1)) + l2 * (cos(theta1 + theta2))
    dyd2 = l2 * (cos(theta1 + theta2))
    jacobian = [[dxd1, dxd2], [dyd1, dyd2]]

    return pos, jacobian