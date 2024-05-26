filters = {
    '|': np.array([[0, 1, 0],
                   [0, 1, 0],
                   [0, 1, 0]]),
    '-': np.array([[0, 0, 0],
                   [1, 1, 1],
                   [0, 0, 0]]),
    '"': np.array([[1, 1, 1],
                   [0, 0, 0],
                   [0, 0, 0]]),
    '_': np.array([[0, 0, 0],
                   [0, 0, 0],
                   [1, 1, 1]]),
    '/': np.array([[0, 0, 1],
                   [0, 1, 0],
                   [1, 0, 0]]),
    '\\': np.array([[1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1]]),
    '^': np.array([[0, 1, 0],
                   [1, 0, 1],
                   [0, 0, 0]]),
    '>': np.array([[0, 1, 0],
                   [0, 0, 1],
                   [0, 1, 0]]),
    '<': np.array([[0, 1, 0],
                   [1, 0, 0],
                   [0, 1, 0]]),
    '+': np.array([[0, 1, 0],
                   [1, 1, 1],
                   [0, 1, 0]]),
    'X': np.array([[1, 0, 1],
                   [0, 1, 0],
                   [1, 0, 1]]),
    'o': np.array([[0, 1, 0],
                   [1, 0, 1],
                   [0, 1, 0]]),
    'O': np.array([[1, 1, 1],
                   [1, 0, 1],
                   [1, 1, 1]]),
    'L': np.array([[1, 0, 0],
                   [1, 0, 0],
                   [1, 1, 1]]),
    'J': np.array([[0, 0, 1],
                   [0, 0, 1],
                   [1, 1, 1]]),
    'T': np.array([[1, 1, 1],
                   [0, 1, 0],
                   [0, 1, 0]]),
    'U': np.array([[1, 0, 1],
                   [1, 0, 1],
                   [1, 1, 1]]),
    '7': np.array([[1, 1, 1],
                   [0, 0, 1],
                   [0, 0, 1]]),
    'Z': np.array([[1, 1, 0],
                   [0, 1, 0],
                   [0, 1, 1]]),
    'S': np.array([[0, 1, 1],
                   [0, 1, 0],
                   [1, 1, 0]]),
    ' ': np.array([[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]]),
    'V': np.array([[1, 0, 1],
                   [1, 0, 1],
                   [0, 1, 0]]),
    'A': np.array([[0, 1, 0],
                   [1, 0, 1],
                   [1, 1, 1]]),
    'H': np.array([[1, 0, 1],
                   [1, 1, 1],
                   [1, 0, 1]]),
    'K': np.array([[1, 0, 1],
                   [1, 1, 0],
                   [1, 0, 1]]),
    'C': np.array([[1, 1, 0],
                   [1, 0, 0],
                   [1, 1, 0]]),
    'Y': np.array([[1, 0, 1],
                   [0, 1, 0],
                   [0, 1, 0]])
}