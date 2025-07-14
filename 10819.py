import sys
from itertools import combinations

input = sys.stdin.readline

T = int(input())
nums = []
sum_lis = []

for _ in range(T):
    num = int(input())
    nums.append(num)


# # for 조합별변수 in combination(리스트, 조합할 개수)
# for case in combinations(nums, T):
#     #가능한 모든 경우의수를 리스트업해야 그중에 가장 큰 수를 찾을 수 있잖아?
#     sum_lis.append(sum(case))
# print(max(sum_lis))

#제너레이 표현식
#list.nums에서 T개로 배열했을 때 가능한 모든경우의수 case를 반복하면서 그 값을 case에 넣고 그 case중에 가장 큰 값을 찾는다
max_sum = max(sum(case) for case in combinations(nums, T))
print(max_sum)
