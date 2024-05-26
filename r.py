filters = {
    ' ': np.array([[0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0]]),

    '|': np.array([[-1,  0, 2,  0, -1],
                   [-1,  0, 2,  0, -1],
                   [-1,  0, 2,  0, -1],
                   [-1,  0, 2,  0, -1],
                   [-1,  0, 2,  0, -1]]),

    '-': np.array([[-2, -2, -2, -2, -2],
                   [ 0,  0,  0,  0,  0],
                   [ 3,  3,  3,  3,  3],
                   [ 0,  0,  0, 0, 0 ],
                   [-2, -2, -2, -2, -2]]),

    '"': np.array([[1,   5,  5,  5,  1],
                   [-1, -1, -1, -1, -1],
                   [-1, -1, -1, -1, -1],
                   [-1, -1, -1, -1, -1],
                   [-2, -2, -2, -2, -2],]),

    '_': np.array([[-2, -2, -2, -2, -2],
                   [-1, -1, -1, -1, -1],
                   [-1, -1, -1, -1, -1],
                   [-1, -1, -1, -1, -1],
                   [3,  3 ,  3,  3,  3]]),

    '/': np.array([[-6, -3, -1,  1,  2],
                   [-3, -1,  1,  2,  1],
                   [-1,  1,  2,  1, -1],
                   [1,   2,  1, -1, -3],
                   [2,   1, -1, -3, -6]]),

    '\\': np.array([[ 2,  1, -1, -3, -6],
                    [ 1,  2,  1, -1, -3],
                    [-1,  1,  2,  1, -1],
                    [-3, -1,  1,  2,  1],
                    [-6, -3, -1,  1,  2]]),

     '^': np.array([[-2, 0,  3,  0,  -2],
                    [-2, 3,  0,  3,  -2],
                    [-1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1],
                    [-2, -2, -2, -2, -2]]),
     '>': np.array([[2, 1, -1, -2, -3],
                    [-2, 1, 2, -2, -2],
                    [-2, -1, 0, 1,  2],
                    [-2, 1, 2, -2, -2],
                    [2, 1, -1, -2, -3]]),
     '<': np.array([[-3, -2, -1, 1, 2],
                    [-2, -2, 2, 1, -2],
                    [2, 1, 0, -1,  -2],
                    [-2, -2, -2, 1,-2],
                    [-3, -2, -1, 1, 2]]),
     '+': np.array([[-2, -1, 2, -1, -2],
                    [-1, -1, 2, -1, -1],
                    [2 ,  2,  2,  2, 2],
                    [-1, -1, 2, -1, -1],
                    [-2, -1, 2, -1, -2]]),
     'X': np.array([[2, -1, -2, -1, 2],
                    [-1, 2, -3, 2, -1],
                    [-2, -3, 2, -3, -2],
                    [-1, 2, -3, 2, -1],
                    [2, -1, -2, -1, 2]]),
     'o': np.array([[-1, -1, -1, -1, -1],
                    [-1, 2, 2, 2, -1],
                    [-1, 2, -3, 2, -1],
                    [-1, 2, 2, 2, -1],
                    [-1, -1, -1, -1, -1]]),
     'O': np.array([[2, 2, 2, 2, 2],
                    [2, -2, -2, -2, 2],
                    [2, -2, -3, -2, 2],
                    [2, -2, -2, -2, 2],
                    [2, 2, 2, 2, 2]]),
     'L': np.array([[2, 0, -1, -2, -3],
                    [2, 0, -1, -2, -3],
                    [2, 0, -1, -2, -3],
                    [2, 0, -1, -1, -3],
                    [2, 2, 2, 2, 0]]),
     'J': np.array([[-3, -2, -1, 0, 2],
                    [-2, -2, -1, 0, 2],
                    [-1, -1, -1, 0, 2],
                    [0 , 0,  0,  0, 2],
                    [0, 2, 2 , 2,   2]]),
     'T': np.array([[2, 2, 2, 2, 2],
                  [-2.5, -1, 2, -1, -2.5],
                  [-2.5, -1, 2, -1, -2.5],
                  [-2.5, -1, 2, -1, -2.5],
                  [-2.5, -1, 2, -1, -2.5]]),
     'U': np.array([[2, -1.5, -3, -1.5, 2],
                    [2, -1.5, -3, -1.5, 2],
                    [2, -1.5, -3, -1.5, 2],
                    [2, -1.5, -1.5, -1.5, 2],
                    [2,  2,   2,   2,   2]]),
     '7': np.array([[0, 2, 2, 2, 2],
                    [-3, -2, -1, 2, -1],
                    [-2, -1, 2, -1, -2],
                    [-1, 2, -1, -2, -2],
                    [2, -1, -2, -2, -3]]),
     'V': np.array([[2, -2.5, 2, -2.5, 2],
                    [2, -2.5, 2, -2.5, 2],
                    [-2.5, 2, 2, 2, -2.5],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]]),
     'C': np.array([[2, 2, -2.5, -2.5, -2.5],
                    [2, -2.5, -2.5, -2.5, -2.5],
                    [2, 2, 2, 2, -2.5],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]]),
     'Y': np.array([[2.5, -2, 2.5, -2, 2.5],
                    [-2, 2.5, -2, 2.5, -2],
                    [-2, 2.5, -2, 2.5, -2],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]])
}