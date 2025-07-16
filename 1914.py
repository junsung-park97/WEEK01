import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 늘려줌


# 밑에 hanoi(N, 1, 2, 3)을 입력하면 start = 1, mid = 2, end = 3이 입력되잖아 .append를 star, end만 출력하는거면 계속 1 3, 1 3만 출력되는거 아니야?
def hanoi(n, start, mid, end):
    if n == 1:
        moves.append(f"{start} {end}")
        return
    hanoi(n - 1, start, end, mid)
    moves.append(f"{start} {end}")
    hanoi(n - 1, mid, start, end)

N = int(sys.stdin.readline())
print(2**N - 1)

if N <= 20:  # 이동 횟수가 너무 많으면 출력 안 함
    moves = []
    hanoi(N, 1, 2, 3)
    print('\n'.join(moves))