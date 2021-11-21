# 1. 1193 - 분수찾기 (https://www.acmicpc.net/problem/1193)
"""
문제 설명
무한히 큰 배열에 다음과 같이 분수들이 적혀있다.
이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과
같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.
"""

# Case Study
n = int(input())

li = 0
max_n = 0
while n > max_n :
    li += 1  
    max_n += li  

gap = max_n - n 
if li % 2 == 0 :
    top = li - gap
    under = gap + 1
else :
    top = gap + 1
    under = li - gap

print(f'{top}/{under}')

"""
insight 정리
1. 원리는 알아냈는데, 이를 실제 코드로 구현하는 과정에서 계속 실패했던 사례.
2. Task를 세부적으로 나누었을 때, 가장 먼저 주어진 수가 대각선을 기준으로 어느 라인에 위치하는지를 알아냈어야 했다.
3. 2는 어렵지 않게 구현했는데, 라인의 위치 값이 홀수이냐 짝수이냐에 따른 계산 로직을 다양화하는 부분이 의외로 어려웠다.
"""