import numpy as np

if __name__ == "__main__":
    size = int(raw_input())
    matrix = list(
        list(float(_1) for _1 in raw_input().split(' ')) for _ in range(size)
    )
    print round(np.linalg.det(matrix), 2)
