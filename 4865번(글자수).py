# 문제 해결 전략은 비교 글자를 한글자씩 하면 최대로 포함된 글자 수를 구할 수 있다.
# 예를 들어, str1에는 "aaabb" 문자열이 있고 str2에는 "abababab"가 있다고 가정한다면
# str2에 포함되는 str1의 문자열은 "ab" 와 문자 "a", "b"다. 즉 3가지이다.
# 이 3가지 중에서 "ab"는 str2에서 4개가 들어있음을 알 수 있고
# a 또한 4개가 들어 있음을 알 수 있다.
# 즉, 문자열 길이가 2인 문자열이 최대로 포함되어 있는 값과
# 하나의 문자가 최대로 포함되어 있는 값이 같다는 의미이다.

# 이 문제의 핵심은 포함되는 글자를 확인 시, 가장 길이가 작은 문자로 확인하면
# 가장 큰 결과를 얻을 수 있으므로, 한글자 씩 str1 리스트에서 문자를 추출해
# str2에 포함되어 있는 갯수를 리스트 s에 저장하고 max 함수를 사용하여
# 가장 큰 수를 출력하면 된다.


T = int(input())            # 테스트 케이스 수 T 입력
s = []                      # 각 문자가 str2에 포함되어 있는 개수를 저장할 리스트
for i in range(1, T+1):     # 테스트 케이스 수 만큼 반복.
    str1 = list(input())
    str2 = list(input())
    for j in str1:          # str1에서 한글자씩 추출해서 str2에 포함되어있는 개수를 리스트 s에 저장
        s.append(str2.count(j))
    print("#"+str(i)+ " "+str(max(s)))  # 리스트 s에서 최댓 값을 출력
    s.clear()               # 다시 for문을 돌려야 하므로, 이전 결과가 저장된 리스트 값을 지움.