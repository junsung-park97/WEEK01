#알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
# 단, 중복된 단어는 하나만 남기고 제거해야 한다.

# 첫째 줄에 단어의 개수 N이 주어진다.
# (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다.
# 주어지는 문자열의 길이는 50을 넘지 않는다.

import sys

n = int(sys.stdin.readline())
lst = []

#입력받은 케이스만큼 반복하면서 문자를 입력받음
for i in range(n):
    lst.append(sys.stdin.readline().strip())

#입력받은 문자열의 중복이 있는지 확인? ㄴㄴ 제거
# 자료형중 하나인 집합을 만드는 함수다 okey
# 주요기능으로는 중복을 제거하고, 순서를 무시한 고유한 값들의 모음을 만든다 NO!!!!!

set_lst = set(lst)

#set()힘수를 거치고 나온 중복이 없는 문자열을 리스트화?해서 리스트에 다시 집어넣는다?
lst = list(set_lst)

#그리고 그 문자열을 오름차순으로 다시 정렬한다
lst.sort()

# 왜 굳이 ? 위에서 길이와 오름차순을 정렬하면 되는거 아닌가? 왜 한번 더 정렬하지?
#정렬된 문자열의 길이를 기준으로 재정렬한다?
lst.sort(key = len)

for i in lst:
    print(i) 


