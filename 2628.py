import sys,math

wid, hei = map(int, sys.stdin.readline().strip())
cutting_case = int(sys.stdin.readline().strip())
cutting_place = list(int(sys.stdin.readline().strip()))

# 자를떄마다 리흐트업 -> 그렇게 하면 너부 복잡하다
# 갭차이를 구해서 그 차이가 가장 큰 값을 x,y축 각각 구하면 가장 갭이 큰값이 나오게되겠네
