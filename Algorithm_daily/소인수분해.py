x = int(input("?"))
d = 2

while d <= x:
    if x % d == 0:
        print(d)
        x = x / d
    else:
        d = d + 1

# 소인수분해할 숫자를 입력받아 정수로 바꾼다.
# 가장 작은 소수인 2부터 나눈다.

# 반복 과정은 나뉘는 수가 나누는 수보다 크거나 같을 때까지 이다.
# x가 d로 나누어지면(나머지가 0이면)
# d는 x의 약수이므로 출력한다.
# x를 d로 나눠서 다시 x에 저장한다.

# 나누어지지 않으면 1을 더해서 반복한다.
