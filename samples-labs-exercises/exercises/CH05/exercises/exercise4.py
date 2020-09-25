Pt = tuple[int, int]

def queenss(n: int) -> list[list[Pt]]:
    def placeQueens(k: int) -> list[list[Pt]]:
        return [[]] if k == 0 \
                    else [[(k, column)] + queens
                             for queens in placeQueens(k - 1)
                                 for column in range(1, n + 1)
                                     if isSafe((k, column), queens)]
    return placeQueens(n)

def isSafe(queen: Pt, queens: list[Pt]) -> bool:
    return all(not inCheck(queen, q) for q in queens)

def inCheck(q1: Pt, q2: Pt) -> bool:
    return (q1[0] == q2[0] or # 同列
            q1[1] == q2[1] or # 同行
            abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])) # 對角線

def printQueens(qs: list[Pt]):
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]

    for q in qs:
        board[q[0] - 1][q[1] - 1] = 1

    for row in board:
        for p in row:
            print(' Q' if p else ' .', end = '')
        print()

for qs in queenss(8):
    printQueens(qs)
    print()